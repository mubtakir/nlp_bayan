from bayan.bayan.hybrid_interpreter import HybridInterpreter
from bayan.bayan.lexer import HybridLexer
from bayan.bayan.parser import HybridParser

interp = HybridInterpreter()

# Add knowledge
code = """
parent(ali, ahmed).
parent(ahmed, sara).
grandparent(X, Z) :- parent(X, Y), parent(Y, Z).
"""
lexer = HybridLexer(code + "\n")
tokens = lexer.tokenize()
parser = HybridParser(tokens)
ast = parser.parse()
interp.interpret(ast)

# Query
print("Query: grandparent(ali, ?X)")
lexer2 = HybridLexer("query grandparent(ali, ?X).\n")
tokens2 = lexer2.tokenize()
parser2 = HybridParser(tokens2)
ast2 = parser2.parse()
results = interp.interpret(ast2)

print(f"Results: {results}")
for r in results:
    print(f"  {r}")
