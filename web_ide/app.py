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
NAME_PATTERN = re.compile(r'^[A-Za-z0-9_\-.]+\.(?:bayan|by)$')

def _is_valid_script_name(name: str) -> bool:
    if not isinstance(name, str):
        return False
    if len(name) == 0 or len(name) > 100:
        return False
    if '/' in name or '\\' in name or name.startswith('.'):
        return False
    if not (name.endswith('.bayan') or name.endswith('.by')):
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
       include foo.bayan | include foo.by  | إدراج foo.bayan | إدراج foo.by | استيراد foo.bayan | استيراد foo.by
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

@app.route('/wem')
def wem_ui():
    return render_template('wem.html')

@app.route('/api/wem/analyze', methods=['POST'])
def wem_analyze():
    data = request.json
    word = data.get('word')
    lang = data.get('lang', 'en')
    
    if not word:
        return jsonify({'error': 'Word is required'}), 400
        
    result = wem.analyze_word(word, lang)
    return jsonify(result)

@app.route('/ide_graph')
def ide_graph():
    return render_template('ide_graph.html')


@app.route('/healthz')
def healthz():
    return jsonify({'ok': True})

@app.route('/test')
def test_editor():
    return render_template('test_simple.html')


@app.route('/ai_playground')
def ai_playground():
    return render_template('ai_playground.html')

@app.route('/logic_graph')
def logic_graph():
    return render_template('logic_graph.html')

@app.route('/unified_graph')
def unified_graph():
    return render_template('unified_graph.html')

@app.route('/api/ide/run_logic', methods=['POST'])
def api_run_logic():
    data = request.json
    code = data.get('code', '')
    
    # Use HybridInterpreter to run the code
    from bayan.hybrid_interpreter import HybridInterpreter
    from bayan.visualization import ExistentialVisualizer
    import io
    import sys
    
    interpreter = HybridInterpreter()
    
    # Capture stdout
    old_stdout = sys.stdout
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    try:
        # Parse and interpret
        from bayan.lexer import HybridLexer
        from bayan.parser import HybridParser
        
        lexer = HybridLexer(code)
        tokens = lexer.tokenize()
        parser = HybridParser(tokens)
        ast = parser.parse()
        interpreter.interpret(ast)
        
        output = captured_output.getvalue()
        
        # Get Graph Data
        visualizer = ExistentialVisualizer(interpreter)
        graph_data = visualizer.export_d3_graph()
        
        # Get Trace and Contradictions
        trace = interpreter.logical.trace
        contradictions = interpreter.logical.check_contradictions()
        
        return jsonify({
            'output': output,
            'graph': graph_data,
            'trace': trace,
            'contradictions': contradictions
        })
        
    except Exception as e:
        return jsonify({
            'output': f"Error: {str(e)}",
            'graph': {'nodes': [], 'links': []},
            'trace': [f"Error: {str(e)}"],
            'contradictions': []
        }), 500
    finally:
        sys.stdout = old_stdout

@app.route('/api/ide/run_unified', methods=['POST'])
def api_run_unified():
    data = request.json
    code = data.get('code', '')
    mode = data.get('mode', 'unified')  # logic, procedural, oop, entity, unified
    
    # Use HybridInterpreter to run the code
    from bayan.hybrid_interpreter import HybridInterpreter
    from bayan.visualization import ExistentialVisualizer
    import io
    import sys
    
    interpreter = HybridInterpreter()
    
    # Capture stdout
    old_stdout = sys.stdout
    captured_output = io.StringIO()
    sys.stdout = captured_output
    
    try:
        # Parse and interpret
        from bayan.lexer import HybridLexer
        from bayan.parser import HybridParser
        
        lexer = HybridLexer(code)
        tokens = lexer.tokenize()
        parser = HybridParser(tokens)
        ast = parser.parse()
        interpreter.interpret(ast)
        
        output = captured_output.getvalue()
        
        # Get Graph Data based on mode
        visualizer = ExistentialVisualizer(interpreter)
        
        if mode == 'logic':
            graph_data = visualizer.export_d3_graph()
        elif mode == 'procedural':
            graph_data = visualizer.export_procedural_graph()
        elif mode == 'oop':
            graph_data = visualizer.export_oop_graph()
        elif mode == 'entity':
            graph_data = visualizer.export_entity_graph()
        else:  # unified
            graph_data = visualizer.export_unified_graph()
        
        # Get Trace and Contradictions
        trace = interpreter.logical.trace
        contradictions = interpreter.logical.check_contradictions()
        
        return jsonify({
            'output': output,
            'graph': graph_data,
            'trace': trace,
            'contradictions': contradictions
        })
        
    except Exception as e:
        import traceback
        error_trace = traceback.format_exc()
        return jsonify({
            'output': f"Error: {str(e)}",
            'graph': {'nodes': [], 'links': [], 'stats': {'total_nodes': 0, 'total_links': 0, 'logic_nodes': 0, 'procedural_nodes': 0, 'oop_nodes': 0, 'entity_nodes': 0}},
            'trace': [f"Error: {str(e)}", error_trace],
            'contradictions': []
        }), 500
    finally:
        sys.stdout = old_stdout


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


def _extract_first_heading(text: str) -> str | None:
    try:
        for line in text.splitlines():
            s = line.lstrip()
            if s.startswith('#'):
                # strip leading hashes and spaces
                s2 = s.lstrip('#').strip()
                if s2:
                    return s2
        return None
    except Exception:
        return None



def _infer_example_domain(text: str) -> str:
    try:
        code = _extract_first_bayan_block(text) or ''
        domains = set()
        if 'include "ai/ml.bayan"' in code or "include 'ai/ml.bayan'" in code:
            domains.add('ai.ml')
        if 'include "ai/nlp.bayan"' in code or "include 'ai/nlp.bayan'" in code:
            domains.add('ai.nlp')
        if 'include "ai/data.bayan"' in code or "include 'ai/data.bayan'" in code:
            domains.add('ai.data')
        # Graphics domain detection (any include from gfx/*)
        if 'include "gfx/' in code or "include 'gfx/" in code:
            domains.add('gfx')
        if len(domains) == 1:
            return next(iter(domains))
        if len(domains) > 1:
            return 'mixed'
        # Heuristics: logic examples without ai.* includes
        cl = code.lower()
        if ((":-" in code)
                or ("query " in cl)
                or ("استعلام" in code)
                or ("هجين" in code)
                or ("حقيقة" in code)
                or ("قاعدة" in code)
                or re.search(r'\bfact\b', cl)
                or re.search(r'\brule\b', cl)):
            return 'logic'
        return 'unknown'
    except Exception:
        return 'unknown'



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
                        desc = _extract_first_heading(txt) or ''
                        domain = _infer_example_domain(txt)
                        items.append({'name': name, 'desc': desc, 'domain': domain})
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
    include_graph = payload.get('include_graph', False)
    graph_type = payload.get('graph_type', 'unified')  # logic, procedural, oop, entity, unified

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
            os.path.join(PROJECT_ROOT, 'gfx'),
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

        # Generate graph data if requested
        graph_data = None
        trace = []
        contradictions = []
        
        if include_graph:
            try:
                from bayan.visualization import ExistentialVisualizer
                visualizer = ExistentialVisualizer(intr)
                
                if graph_type == 'logic':
                    graph_data = visualizer.export_d3_graph()
                elif graph_type == 'procedural':
                    graph_data = visualizer.export_procedural_graph()
                elif graph_type == 'oop':
                    graph_data = visualizer.export_oop_graph()
                elif graph_type == 'entity':
                    graph_data = visualizer.export_entity_graph()
                else:  # unified
                    graph_data = visualizer.export_unified_graph()
                
                # Get trace and contradictions from logical engine
                if hasattr(intr, 'logical') and intr.logical:
                    trace = getattr(intr.logical, 'trace', [])
                    contradictions = intr.logical.check_contradictions()
                    
            except Exception as graph_error:
                # If graph generation fails, continue without it
                graph_data = {'nodes': [], 'links': [], 'error': str(graph_error)}

        response_data = {
            'success': True,
            'stdout': stdout_text,
            'result': result_json,
            'result_repr': result_repr,
        }
        
        if include_graph:
            response_data['graph'] = graph_data
            response_data['trace'] = trace
            response_data['contradictions'] = contradictions
        
        return jsonify(response_data)
        
    except Exception as e:
        tb = traceback.format_exc(limit=5)
        return jsonify({
            'success': False,
            'error_type': e.__class__.__name__,
            'error': str(e),
            'traceback': tb,
        }), 400


@app.post('/api/ide/export_graph')
def api_ide_export_graph():
    """
    Export graph visualization data
    Accepts: code, graph_type, export_format
    Returns: graph data in requested format
    """
    payload = request.get_json(silent=True) or {}
    code = payload.get('code', '')
    graph_type = payload.get('graph_type', 'unified')
    export_format = payload.get('export_format', 'json')  # json, svg_data
    
    try:
        # Parse and interpret code
        expanded = _expand_includes(code)
        lexer = HybridLexer(expanded)
        tokens = lexer.tokenize()
        parser = HybridParser(tokens)
        ast = parser.parse()
        
        intr = HybridInterpreter()
        buf = io.StringIO()
        with redirect_stdout(buf):
            intr.interpret(ast)
        
        # Generate graph
        from bayan.visualization import ExistentialVisualizer
        visualizer = ExistentialVisualizer(intr)
        
        if graph_type == 'logic':
            graph_data = visualizer.export_d3_graph()
        elif graph_type == 'procedural':
            graph_data = visualizer.export_procedural_graph()
        elif graph_type == 'oop':
            graph_data = visualizer.export_oop_graph()
        elif graph_type == 'entity':
            graph_data = visualizer.export_entity_graph()
        else:  # unified
            graph_data = visualizer.export_unified_graph()
        
        if export_format == 'json':
            return jsonify({
                'success': True,
                'data': graph_data,
                'format': 'json'
            })
        elif export_format == 'svg_data':
            # Return metadata for SVG generation on client side
            return jsonify({
                'success': True,
                'data': graph_data,
                'format': 'svg_data',
                'metadata': {
                    'node_count': len(graph_data.get('nodes', [])),
                    'link_count': len(graph_data.get('links', [])),
                    'graph_type': graph_type
                }
            })
        else:
            return jsonify({
                'success': False,
                'error': f'Unsupported export format: {export_format}'
            }), 400
            
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'traceback': traceback.format_exc(limit=5)
        }), 500


# Debugger State
debug_session = {
    'vm': None,
    'code_object': None,
    'source_code': None
}

@app.route('/api/debug/start', methods=['POST'])
def api_debug_start():
    """Start debugging session"""
    data = request.json
    code = data.get('code', '')
    
    try:
        # 1. Parse AST
        from bayan.lexer import HybridLexer
        from bayan.parser import HybridParser
        lexer = HybridLexer(code)
        tokens = lexer.tokenize()
        parser = HybridParser(tokens)
        ast = parser.parse()
        
        # 2. Compile to Bytecode
        from bayan.bytecode.codegen import compile_to_bytecode
        code_obj = compile_to_bytecode(ast)
        
        # 3. Initialize VM in debug mode
        from bayan.bytecode.vm import BytecodeVM
        vm = BytecodeVM(debug_mode=True)
        
        # Store session
        debug_session['vm'] = vm
        debug_session['code_object'] = code_obj
        debug_session['source_code'] = code
        
        # Start execution (will pause at first instruction if we set a breakpoint or just init)
        # Actually, we want to start paused.
        # Let's just set up the VM and not call execute yet, or call execute and expect it to pause?
        # The VM.execute runs until end or breakpoint.
        # We want to "load" the code.
        vm.current_code = code_obj
        vm.running = True
        vm.paused = True # Start paused
        vm.ip = 0
        
        return jsonify({
            'success': True,
            'state': vm.get_state()
        })
        
    except Exception as e:
        import traceback
        traceback.print_exc()
        return jsonify({'success': False, 'error': str(e)})

@app.route('/api/debug/step', methods=['POST'])
def api_debug_step():
    """Step execution"""
    vm = debug_session.get('vm')
    if not vm:
        return jsonify({'success': False, 'error': 'No active debug session'})
        
    status = vm.step()
    return jsonify({
        'success': True,
        'status': status,
        'state': vm.get_state()
    })

@app.route('/api/debug/resume', methods=['POST'])
def api_debug_resume():
    """Resume execution"""
    vm = debug_session.get('vm')
    if not vm:
        return jsonify({'success': False, 'error': 'No active debug session'})
        
    result = vm.resume()
    return jsonify({
        'success': True,
        'result': str(result) if result != "PAUSED" else None,
        'status': "PAUSED" if result == "PAUSED" else "FINISHED",
        'state': vm.get_state()
    })

@app.route('/api/debug/stop', methods=['POST'])
def api_debug_stop():
    """Stop debugging"""
    debug_session['vm'] = None
    debug_session['code_object'] = None
    return jsonify({'success': True})

@app.route('/api/debug/breakpoint', methods=['POST'])
def api_debug_breakpoint():
    """Toggle breakpoint"""
    vm = debug_session.get('vm')
    if not vm:
        return jsonify({'success': False, 'error': 'No active debug session'})
        
    data = request.json
    line = data.get('line')
    enable = data.get('enable', True)
    
    if enable:
        vm.set_breakpoint(line)
    else:
        vm.clear_breakpoint(line)
        
    return jsonify({'success': True, 'breakpoints': list(vm.breakpoints)})

@app.route('/api/debug/state', methods=['GET'])
def api_debug_state():
    """Get current state"""
    vm = debug_session.get('vm')
    if not vm:
        return jsonify({'success': False, 'error': 'No active debug session'})
        
    return jsonify({
        'success': True,
        'state': vm.get_state()
    })

@app.route('/debugger')
def debugger_page():
    # Assuming render_template is imported from Flask
    from flask import render_template
    return render_template('debugger.html')

# ========================================
# AI Code Assistant API
# ========================================

# إضافة مسار extensions للاستيراد
EXTENSIONS_DIR = os.path.join(PROJECT_ROOT, 'extensions')
if EXTENSIONS_DIR not in sys.path:
    sys.path.insert(0, EXTENSIONS_DIR)

try:
    from ai_code_assistant import AICodeAssistant
    ai_assistant = AICodeAssistant(language="ar")
    HAS_AI_ASSISTANT = True
except ImportError:
    ai_assistant = None
    HAS_AI_ASSISTANT = False

@app.route('/api/ai/status')
def api_ai_status():
    """حالة المساعد الذكي"""
    return jsonify({
        'available': HAS_AI_ASSISTANT,
        'features': ['completion', 'error_explain', 'optimization', 'analysis', 'generation'] if HAS_AI_ASSISTANT else []
    })

@app.route('/api/ai/complete', methods=['POST'])
def api_ai_complete():
    """إكمال الكود"""
    if not HAS_AI_ASSISTANT:
        return jsonify({'error': 'AI Assistant not available'}), 503

    data = request.get_json() or {}
    code = data.get('code', '')

    suggestions = ai_assistant.suggest_completion(code)
    return jsonify({
        'suggestions': [
            {
                'text': s.text,
                'description': s.description_ar,
                'confidence': s.confidence
            } for s in suggestions
        ]
    })

@app.route('/api/ai/explain-error', methods=['POST'])
def api_ai_explain_error():
    """شرح الخطأ"""
    if not HAS_AI_ASSISTANT:
        return jsonify({'error': 'AI Assistant not available'}), 503

    data = request.get_json() or {}
    error = data.get('error', '')
    context = data.get('context', '')

    explanation = ai_assistant.explain_error(error, context)
    return jsonify({
        'error_type': explanation.error_type,
        'explanation': explanation.explanation_ar,
        'fix': explanation.fix_suggestion,
        'example': explanation.example_fix,
        'concepts': explanation.related_concepts
    })

@app.route('/api/ai/optimize', methods=['POST'])
def api_ai_optimize():
    """اقتراح تحسينات"""
    if not HAS_AI_ASSISTANT:
        return jsonify({'error': 'AI Assistant not available'}), 503

    data = request.get_json() or {}
    code = data.get('code', '')

    suggestions = ai_assistant.suggest_optimization(code)
    return jsonify({
        'suggestions': [
            {
                'title': s.text,
                'description': s.description_ar,
                'type': s.suggestion_type.value,
                'priority': s.priority
            } for s in suggestions
        ]
    })

@app.route('/api/ai/analyze', methods=['POST'])
def api_ai_analyze():
    """تحليل الكود"""
    if not HAS_AI_ASSISTANT:
        return jsonify({'error': 'AI Assistant not available'}), 503

    data = request.get_json() or {}
    code = data.get('code', '')

    analysis = ai_assistant.analyze_code(code)
    return jsonify({
        'language': analysis.language.value,
        'lines': analysis.lines_count,
        'functions': analysis.functions_count,
        'classes': analysis.classes_count,
        'imports': analysis.imports_count,
        'complexity': analysis.complexity_score,
        'issues': analysis.issues,
        'suggestions': [
            {
                'title': s.text,
                'description': s.description_ar
            } for s in analysis.suggestions
        ]
    })

@app.route('/api/ai/generate', methods=['POST'])
def api_ai_generate():
    """توليد كود"""
    if not HAS_AI_ASSISTANT:
        return jsonify({'error': 'AI Assistant not available'}), 503

    data = request.get_json() or {}
    description = data.get('description', '')
    template = data.get('template', None)

    code = ai_assistant.generate_code(description, template)
    return jsonify({
        'code': code
    })

@app.route('/api/ai/chat', methods=['POST'])
def api_ai_chat():
    """محادثة مع المساعد"""
    if not HAS_AI_ASSISTANT:
        return jsonify({'error': 'AI Assistant not available'}), 503

    data = request.get_json() or {}
    message = data.get('message', '')

    response = ai_assistant.chat(message)
    return jsonify({
        'response': response
    })

if __name__ == '__main__':
    # Use port 5001 to avoid collisions
    app.run(host='127.0.0.1', port=5000, debug=True)
