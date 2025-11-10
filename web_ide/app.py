"""
Bayan Web IDE (standalone)
واجهة ويب لمحرر بيان — مشروع اللغة الهجينة الخالص (بدون LLM)

تشغيل محلي:
  python bayan_python/web_ide/app.py
  ثم افتح: http://127.0.0.1:5001/ide
"""
from __future__ import annotations

import io
import os
import re
import sys
import json
import traceback
from contextlib import redirect_stdout
from typing import List

from flask import Flask, jsonify, render_template, request, abort

# Ensure Bayan package is importable (bayan_python/bayan)
CUR_DIR = os.path.dirname(os.path.abspath(__file__))
PROJECT_ROOT = os.path.dirname(CUR_DIR)              # bayan_python/
BAYAN_PKG_DIR = os.path.join(PROJECT_ROOT, 'bayan')  # bayan_python/bayan
if BAYAN_PKG_DIR not in sys.path:
    sys.path.insert(0, BAYAN_PKG_DIR)

# Now we can import Bayan language components
from bayan.lexer import HybridLexer
from bayan.parser import HybridParser
from bayan.hybrid_interpreter import HybridInterpreter

app = Flask(__name__, template_folder=os.path.join(CUR_DIR, 'templates'))

SCRIPTS_DIR = os.path.join(CUR_DIR, 'user_scripts')
os.makedirs(SCRIPTS_DIR, exist_ok=True)

# -----------------------------
# Utilities: file validation
# -----------------------------
NAME_PATTERN = re.compile(r'^[A-Za-z0-9_\-.]+\.bayan$')

def _is_valid_script_name(name: str) -> bool:
    if not isinstance(name, str):
        return False
    if len(name) == 0 or len(name) > 100:
        return False
    if '/' in name or '\\' in name or name.startswith('.'):
        return False
    if not name.endswith('.bayan'):
        return False
    return NAME_PATTERN.fullmatch(name) is not None


def _script_path(name: str) -> str:
    if not _is_valid_script_name(name):
        abort(400, description='Invalid filename')
    return os.path.join(SCRIPTS_DIR, name)

# ----------------------------------
# Include-expansion (optional helper)
# ----------------------------------
INCLUDE_PREFIXES = ('include ', 'إدراج ', 'استيراد ')


def _expand_includes(code: str, *, visited: set[str] | None = None) -> str:
    """Very simple preprocessor: expands lines like
       include foo.bayan   | إدراج foo.bayan | استيراد foo.bayan
       by inlining file content from user_scripts.
       Prevents cycles using a visited set.
    """
    if visited is None:
        visited = set()

    out_lines: List[str] = []
    for raw_line in code.splitlines():
        line = raw_line.strip()
        matched = None
        for p in INCLUDE_PREFIXES:
            if line.startswith(p):
                matched = line[len(p):].strip()
                break
        if matched:
            # Allow quoted or unquoted names
            if matched.startswith(('"', "'")) and matched.endswith(("'", '"')):
                fname = matched[1:-1]
            else:
                fname = matched
            if not _is_valid_script_name(fname):
                # If not a valid script name, keep line as-is
                out_lines.append(raw_line)
                continue
            if fname in visited:
                # Skip to avoid circular includes
                continue
            visited.add(fname)
            fpath = _script_path(fname)
            if os.path.isfile(fpath):
                with open(fpath, 'r', encoding='utf-8') as f:
                    nested = f.read()
                out_lines.append(_expand_includes(nested, visited=visited))
            else:
                out_lines.append(f'# include missing: {fname}')
        else:
            out_lines.append(raw_line)
    return "\n".join(out_lines)


# -----------------------------
# Routes: pages
# -----------------------------
@app.route('/')
def index():
    return render_template('ide.html')


@app.route('/ide')
def ide():
    return render_template('ide.html')


@app.route('/healthz')
def healthz():
    return jsonify({'ok': True})


# -----------------------------
# Routes: IDE file APIs
# -----------------------------
@app.get('/api/ide/files')
def api_ide_files():
    files = []
    for name in os.listdir(SCRIPTS_DIR):
        if _is_valid_script_name(name):
            p = os.path.join(SCRIPTS_DIR, name)
            st = os.stat(p)
            files.append({'name': name, 'size': st.st_size, 'mtime': int(st.st_mtime)})
    files.sort(key=lambda x: x['name'].lower())
    return jsonify(files)


@app.get('/api/ide/file')
def api_ide_file_get():
    name = request.args.get('name')
    if not _is_valid_script_name(name or ''):
        abort(400, description='Invalid filename')
    path = _script_path(name)
    if not os.path.isfile(path):
        abort(404, description='File not found')
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    return jsonify({'name': name, 'content': content})


@app.post('/api/ide/file')
def api_ide_file_save():
    data = request.get_json(silent=True) or {}
    name = data.get('name')
    content = data.get('content', '')
    if not _is_valid_script_name(name or ''):
        abort(400, description='Invalid filename')
    path = _script_path(name)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
    return jsonify({'success': True})


@app.delete('/api/ide/file')
def api_ide_file_delete():
    name = request.args.get('name')
    if not _is_valid_script_name(name or ''):
        abort(400, description='Invalid filename')
    path = _script_path(name)
    if os.path.isfile(path):
        os.remove(path)
        return jsonify({'success': True})
    abort(404, description='File not found')


@app.post('/api/ide/rename')
def api_ide_rename():
    data = request.get_json(silent=True) or {}
    old_name = data.get('old_name')
    new_name = data.get('new_name')
    if not (_is_valid_script_name(old_name or '') and _is_valid_script_name(new_name or '')):
        abort(400, description='Invalid filename')
    old_path = _script_path(old_name)
    new_path = _script_path(new_name)
    if not os.path.isfile(old_path):
        abort(404, description='Source file not found')
    if os.path.exists(new_path):
        abort(409, description='Target already exists')
    os.rename(old_path, new_path)
    return jsonify({'success': True})


# ----------------------------------
# Routes: Examples browser for IDE
# ----------------------------------
EXAMPLES_DIR = os.path.join(PROJECT_ROOT, 'examples')
SAFE_MD_NAME = re.compile(r'^[A-Za-z0-9_\-.]+\.md$')


def _extract_first_bayan_block(text: str) -> str | None:
    start = text.find("```bayan")
    if start == -1:
        return None
    nl = text.find("\n", start)
    if nl == -1:
        return None
    start = nl + 1
    end = text.find("```", start)
    if end == -1:
        return None
    return text[start:end].strip()


@app.get('/api/ide/examples')
def api_ide_examples():
    items = []
    try:
        if os.path.isdir(EXAMPLES_DIR):
            for name in sorted(os.listdir(EXAMPLES_DIR)):
                if not name.endswith('.md'):
                    continue
                path = os.path.join(EXAMPLES_DIR, name)
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        txt = f.read()
                    has_bayan = ("```bayan" in txt)
                    if has_bayan:
                        items.append({'name': name})
                except Exception:
                    continue
    except Exception:
        pass
    return jsonify(items)


@app.get('/api/ide/example')
def api_ide_example_get():
    name = request.args.get('name') or ''
    if not SAFE_MD_NAME.fullmatch(name):
        abort(400, description='Invalid example name')
    path = os.path.join(EXAMPLES_DIR, name)
    if not os.path.isfile(path):
        abort(404, description='Example not found')
    with open(path, 'r', encoding='utf-8') as f:
        txt = f.read()
    code = _extract_first_bayan_block(txt)
    if not code:
        abort(404, description='No Bayan code block in example')
    return jsonify({'name': name, 'code': code})

# ----------------------------------
# Routes: AI functions listing for IDE autocomplete
# ----------------------------------
AI_FILES = [
    ('ai.ml', os.path.join(PROJECT_ROOT, 'ai', 'ml.bayan')),
    ('ai.nlp', os.path.join(PROJECT_ROOT, 'ai', 'nlp.bayan')),
    ('ai.data', os.path.join(PROJECT_ROOT, 'ai', 'data.bayan')),
]


def _collect_ai_functions():
    items = []
    for meta, fpath in AI_FILES:
        try:
            with open(fpath, 'r', encoding='utf-8') as f:
                lines = f.read().splitlines()
        except Exception:
            continue
        docbuf = []
        for ln in lines:
            s = ln.strip()
            if s.startswith('#'):
                # accumulate contiguous comment lines (without leading '#')
                docbuf.append(s[1:].strip())
                # keep only last few lines to limit size
                if len(docbuf) > 4:
                    docbuf = docbuf[-4:]
                continue
            if s.startswith('def ') and '(' in s:
                name = s[4:s.find('(')].strip()
                if not name:
                    docbuf = []
                    continue
                is_ar = any(ord(c) > 127 for c in name)
                # build short doc from last comment lines
                doc = ''
                if docbuf:
                    short = [d for d in docbuf if d]
                    doc = ' '.join(short[-2:])
                    if len(doc) > 200:
                        doc = doc[:200]
                items.append({'name': name, 'meta': meta, 'ar': is_ar, 'doc': doc})
                docbuf = []
            else:
                # reset when encountering non-comment/non-def
                docbuf = []
    # de-duplicate by name
    dedup = {}
    for it in items:
        if it['name'] not in dedup:
            dedup[it['name']] = it
    return list(dedup.values())


@app.get('/api/ide/ai_functions')
def api_ai_functions():
    try:
        return jsonify(_collect_ai_functions())
    except Exception:
        return jsonify([])



# -----------------------------
# Route: Run Bayan code
# -----------------------------
@app.post('/api/ide/run')
def api_ide_run():
    payload = request.get_json(silent=True) or {}
    code = payload.get('code', '')
    filename = payload.get('filename') or '<editor>'

    # Optional include-expansion for convenience
    expanded = _expand_includes(code)

    # Prepare Bayan interpreter
    try:
        lexer = HybridLexer(expanded)
        tokens = lexer.tokenize()
        parser = HybridParser(tokens, filename=filename)
        ast = parser.parse()

        intr = HybridInterpreter()
        # Better error messages
        intr.traditional.set_source(expanded, filename=filename)
        intr.traditional.set_error_formatting(colors=False, context_lines=1, tabstop=4)
        # Add user_scripts and common folders to Bayan module search path
        bayan_module_paths = getattr(intr, '_bayan_module_paths', [])
        for extra in {
            SCRIPTS_DIR,
            os.path.join(PROJECT_ROOT, 'examples'),
            os.path.join(PROJECT_ROOT, 'bayan_solutions'),
            os.path.join(PROJECT_ROOT, 'ai'),
        }:
            if os.path.isdir(extra) and extra not in bayan_module_paths:
                bayan_module_paths.insert(0, extra)

        # Execute while capturing stdout (for print calls)
        buf = io.StringIO()
        with redirect_stdout(buf):
            result = intr.interpret(ast)
        stdout_text = buf.getvalue()

        # Result may not be JSON-serializable; return a repr
        try:
            json.dumps(result)
            result_json = result
            result_repr = None
        except Exception:
            result_json = None
            result_repr = repr(result)

        return jsonify({
            'success': True,
            'stdout': stdout_text,
            'result': result_json,
            'result_repr': result_repr,
        })
    except Exception as e:
        tb = traceback.format_exc(limit=5)
        return jsonify({
            'success': False,
            'error_type': e.__class__.__name__,
            'error': str(e),
            'traceback': tb,
        }), 400


if __name__ == '__main__':
    # Use port 5001 to avoid collisions
    app.run(host='127.0.0.1', port=5001, debug=True)

