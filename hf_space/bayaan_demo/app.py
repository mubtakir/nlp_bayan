import gradio as gr
import requests, json
import re, os, sys

# Ensure vendored bayan package is importable when running in HF Space
THIS_DIR = os.path.dirname(__file__)
# Add the inner vendored package (…/bayan/bayan) to sys.path so `import bayan` works
VENDORED_DIR = os.path.join(THIS_DIR, "bayan", "bayan")
if VENDORED_DIR not in sys.path:
    sys.path.insert(0, VENDORED_DIR)

try:
    from bayan import HybridLexer, HybridParser
    HAS_FULL_PARSER = True
except Exception:
    HAS_FULL_PARSER = False

DATASET_ID = "Mubtakir/bayaan-alignment-sample"
METRICS_URL = "https://raw.githubusercontent.com/mubtakir/nlp_bayan/main/eval_framework/results/metrics_v1.2_detailed.json"

_cached = {}

def get_dataset():
    if "ds" not in _cached:
        # Lazy import to avoid heavy deps at startup; use streaming to avoid requiring pyarrow
        from datasets import load_dataset
        _cached["ds"] = load_dataset(DATASET_ID, streaming=True)
    return _cached["ds"]

AR_QS = (
    "\u0627\u062c\u0644\u0628 \u0627\u0644\u0628\u064a\u0627\u0646\u0627\u062a\u060c \u0648\u062e\u0630 \u0646\u0645\u0627\u0630\u062c\u064b\u0627 \u0645\u0646 \u0627\u0644\u0648\u062c\u0647\u0627\u062a \u0627\u0644\u0645\u062a\u0648\u0641\u0631\u0629 (train/val/test) \u0648\u0627\u0644\u0644\u063a\u0627\u062a (ar/en)."  # noqa
)

EN_QS = (
    "Load the dataset and sample from the available splits (train/val/test) and languages (ar/en)."
)

QUICKSTART = f"""
Python Quickstart
-----------------

from datasets import load_dataset

# Load the Bayaan alignment dataset
# Load the Bayaan alignment dataset (Arabic+English, 9 domains, v1.2 ~1000 rows)
ds = load_dataset("{DATASET_ID}")
print(ds)
print(ds["train"][0])

# Filter by language
ar_train = [x for x in ds["train"] if x.get("lang") == "ar"]
print("Arabic train examples:", len(ar_train))
"""

def load_metrics():
    try:
        r = requests.get(METRICS_URL, timeout=10)
        r.raise_for_status()
        return json.dumps(r.json(), ensure_ascii=False, indent=2)
    except Exception as e:
        return f"Failed to load metrics: {e}\nURL: {METRICS_URL}"


def browse_examples(split, lang, limit):
    """Prefer datasets streaming if available; fallback to HF datasets-server API."""
    length = int(limit) if limit else 10
    # Try using the `datasets` library with streaming (no pyarrow required)
    try:
        ds = get_dataset()
        it = ds[split]
        rows = []
        for ex in it:
            if lang and ex.get("lang") != lang:
                continue
            rows.append([
                ex.get("id"), ex.get("lang"), ex.get("split"),
                (ex.get("natural_text", "") or "")[:160],
                (ex.get("bayan_code", "") or "")[:160],
                ", ".join((ex.get("actions") or [])[:3]),
                ", ".join((ex.get("states") or [])[:3]),
            ])
            if len(rows) >= length:
                break
        if rows:
            return rows
    except Exception:
        pass
    # Fallback to lightweight API (no local deps)
    try:
        cfg = _cached.get("cfg")
        if not cfg:
            info_url = f"https://datasets-server.huggingface.co/info?dataset={DATASET_ID}"
            r_info = requests.get(info_url, timeout=10)
            r_info.raise_for_status()
            js = r_info.json()
            configs = js.get("configs") or []
            cfg = (configs[0].get("config") if configs else "default")
            _cached["cfg"] = cfg
        url = (
            "https://datasets-server.huggingface.co/rows"
            f"?dataset={DATASET_ID}&config={cfg}&split={split}&offset=0&length={length}"
        )
        r = requests.get(url, timeout=20)
        r.raise_for_status()
        j = r.json()
        rows = []
        for rr in j.get("rows", []):
            ex = rr.get("row", {})
            if lang and ex.get("lang") != lang:
                continue
            rows.append([
                ex.get("id"), ex.get("lang"), ex.get("split"),
                (ex.get("natural_text", "") or "")[:160],
                (ex.get("bayan_code", "") or "")[:160],
                ", ".join((ex.get("actions") or [])[:3]),
                ", ".join((ex.get("states") or [])[:3]),
            ])
        return rows or [["No rows", "", "", "", "", "", ""]]
    except Exception as e:
        return [[f"Failed to fetch rows: {e}", "", "", "", "", "", ""]]
# --- Lightweight normalization and structural validator (beta) ---
_SEMI = re.compile(r";+")
_PLUS_EQ = re.compile(r"(?P<lhs>[\w\u0600-\u06FF\.]+)\s*\+=\s*(?P<rhs>[^;\n]+)")
_MINUS_EQ = re.compile(r"(?P<lhs>[\w\u0600-\u06FF\.]+)\s*-\=\s*(?P<rhs>[^;\n]+)")
CALL_PAT = re.compile(r"^[\w\u0600-\u06FF]+(?:\.[\w\u0600-\u06FF]+)*\s*\(([^()]*)\)\s*$")
ASSIGN_PAT = re.compile(r"^[\w\u0600-\u06FF]+(?:\.[\w\u0600-\u06FF]+)*\s*=\s*.+$")

def normalize_bayan(code: str) -> str:
    text = _SEMI.sub("\n", code or "")
    text = _PLUS_EQ.sub(lambda m: f"{m.group('lhs')} = {m.group('lhs')} + {m.group('rhs')}", text)
    text = _MINUS_EQ.sub(lambda m: f"{m.group('lhs')} = {m.group('lhs')} - {m.group('rhs')}", text)
    return text

def _balanced_parens(s: str) -> bool:
    c = 0
    for ch in s:
        if ch == '(': c += 1
        elif ch == ')':
            c -= 1
            if c < 0: return False
    return c == 0

def validate_bayan(code: str):
    norm = normalize_bayan(code or "")
    errors = []
    if not _balanced_parens(norm):
        errors.append("Unbalanced parentheses")
    for i, line in enumerate(norm.splitlines(), 1):
        s = line.strip()
        if not s:
            continue
        if CALL_PAT.match(s) or ASSIGN_PAT.match(s):
            continue
        errors.append(f"Line {i}: Unrecognized statement: {s[:60]}")
    ok = len(errors) == 0
    return {"ok": ok, "errors": errors}, norm


def validate_bayan_full(code: str):
    """Full syntax validation using HybridLexer/HybridParser if available; falls back to structural checks."""
    norm = normalize_bayan(code or "")
    if not HAS_FULL_PARSER:
        # Fallback to lightweight structural validator
        return validate_bayan(norm)
    try:
        lexer = HybridLexer(norm)
        tokens = lexer.tokenize()
        parser = HybridParser(tokens)
        parser.parse()
        return {"ok": True, "errors": []}, norm
    except Exception as e:
        return {"ok": False, "errors": [str(e)]}, norm



def make_app():
    with gr.Blocks(title="Bayaan Demo") as demo:
        gr.Markdown("""
        # Bayaan — Bilingual Hybrid Language
        - Explore the dataset and view evaluation metrics.
        - This lightweight demo does not run the full interpreter.
        - For full usage: see GitHub repo and eval framework.
        """)

        with gr.Tab("Dataset Browser"):
            gr.Markdown("""
            اختر التقسيم واللغة لاستعراض عينات. | Pick split and language to preview examples.
            """)
            with gr.Row():
                split = gr.Dropdown(choices=["train", "validation", "test"], value="train", label="Split")
                lang = gr.Dropdown(choices=["", "ar", "en"], value="", label="Language (optional)")
                limit = gr.Slider(1, 50, value=10, step=1, label="How many rows?")
            out = gr.Dataframe(headers=["id","lang","split","natural_text","bayan_code","actions","states"], type="array", wrap=True, label="Examples")
            btn = gr.Button("Load")
            btn.click(browse_examples, inputs=[split, lang, limit], outputs=[out])

        with gr.Tab("Metrics v1.2"):
            gr.Markdown("""
            Precomputed dataset-quality metrics (syntax/logic; per-language and per-split).
            Source: eval_framework/results/metrics_v1.2_detailed.json
            """)
            metrics_text = gr.Code(language="json", label="metrics.json")
            load_btn = gr.Button("Fetch Metrics")
            load_btn.click(fn=lambda: load_metrics(), inputs=None, outputs=[metrics_text])

        with gr.Tab("Code Validator"):
            gr.Markdown("""
            Full syntax validation via Bayan HybridParser (vendored). Falls back to structural checks if parser unavailable.
            """)
            code_in = gr.Textbox(lines=8, label="Bayan code", placeholder="محمد.تقديم_وجبة(أحمد);\nأحمد.امتنان += 0.3")
            run_btn = gr.Button("Validate")
            res = gr.JSON(label="Result")
            norm = gr.Code(language="python", label="Normalized code")
            run_btn.click(fn=validate_bayan_full, inputs=[code_in], outputs=[res, norm])


        with gr.Tab("Quickstart"):
            gr.Markdown("""
            Use these snippets locally to load the dataset and start experimenting.
            """)
            gr.Code(QUICKSTART, language="python")

    return demo

if __name__ == "__main__":
    make_app().launch()

