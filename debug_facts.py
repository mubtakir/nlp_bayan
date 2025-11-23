import unittest
from bayan.bayan.hybrid_interpreter import HybridInterpreter
from bayan.bayan.lexer import HybridLexer
from bayan.bayan.parser import HybridParser

# Simple debug test
interp = HybridInterpreter()

# Add a fact
code = "parent(ali, ahmed)."
lexer = HybridLexer(code + "\n")
tokens = lexer.tokenize()
parser = HybridParser(tokens)
ast = parser.parse()
print(f"AST: {ast}")
print(f"AST statements: {ast.statements}")
result = interp.interpret(ast)
print(f"Result: {result}")

# Check knowledge base
print(f"\nKnowledge base: {interp.logical.knowledge_base}")

# Try a query
code2 = "query parent(?X, ?Y)."
lexer2 = HybridLexer(code2 + "\n")
tokens2 = lexer2.tokenize()
parser2 = HybridParser(tokens2)
ast2 = parser2.parse()
print(f"\nQuery AST: {ast2}")
result2 = interp.interpret(ast2)
print(f"Query result: {result2}")
if result2:
    for r in result2:
        print(f"  Solution: {r}")
