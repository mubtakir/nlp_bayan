from bayan.bayan.hybrid_interpreter import HybridInterpreter
from bayan.bayan.lexer import HybridLexer
from bayan.bayan.parser import HybridParser

interp = HybridInterpreter()

# Add facts and rule
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

print("Knowledge base:")
for pred_name, items in interp.logical.knowledge_base.items():
    print(f"  {pred_name}: {items}")

# Test query first
print("\nTesting query grandparent(ali, ?Z):")
lexer2 = HybridLexer("query grandparent(ali, ?Z).\n")
tokens2 = lexer2.tokenize()
parser2 = HybridParser(tokens2)
ast2 = parser2.parse()
result = interp.interpret(ast2)
print(f"Query result: {result}")

# Test explain
print("\nTesting explain:")
lexer3 = HybridLexer('explain("grandparent(ali, sara)")\n')
tokens3 = lexer3.tokenize()
parser3 = HybridParser(tokens3)
ast3 = parser3.parse()
explanation = interp.interpret(ast3)
print(f"Explanation: {explanation}")
