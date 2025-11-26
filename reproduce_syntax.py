
from bayan.bayan import HybridLexer, HybridParser

code = """
def foo(): {
}
{
    x = 1
}
"""

print("Tokenizing...")
lexer = HybridLexer(code)
tokens = list(lexer.tokenize())
# for t in tokens: print(t)

print("Parsing...")
parser = HybridParser(tokens)
try:
    ast = parser.parse()
    print("Parsed successfully")
except Exception as e:
    print(f"Error: {e}")
