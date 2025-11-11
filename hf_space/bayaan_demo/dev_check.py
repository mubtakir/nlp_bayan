import sys, os, re
# allow running locally
THIS_DIR = os.path.dirname(__file__)
VENDORED_DIR = os.path.join(THIS_DIR, 'bayan', 'bayan')
if VENDORED_DIR not in sys.path:
    sys.path.insert(0, VENDORED_DIR)

from bayan import HybridLexer, HybridParser

_SEMI = re.compile(r";+")
_PLUS_EQ = re.compile(r"(?P<lhs>[\w\u0600-\u06FF\.]+)\s*\+=\s*(?P<rhs>[^;\n]+)")
_MINUS_EQ = re.compile(r"(?P<lhs>[\w\u0600-\u06FF\.]+)\s*-\=\s*(?P<rhs>[^;\n]+)")

def normalize(code: str) -> str:
    text = _SEMI.sub("\n", code or "")
    text = _PLUS_EQ.sub(lambda m: f"{m.group('lhs')} = {m.group('lhs')} + {m.group('rhs')}", text)
    text = _MINUS_EQ.sub(lambda m: f"{m.group('lhs')} = {m.group('lhs')} - {m.group('rhs')}", text)
    return text

code = 'محمد.تقديم_وجبة(أحمد);\nأحمد.امتنان += 0.3'
text = normalize(code)
lex = HybridLexer(text)
print('[dev_check] tokenizing...')
tokens = lex.tokenize()
print('[dev_check] tokens:', len(tokens))
print('[dev_check] parsing...')
parser = HybridParser(tokens)
parser.parse()
print('[dev_check] OK')

