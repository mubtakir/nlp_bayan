import os
import json
from bayan.bayan.hybrid_interpreter import HybridInterpreter
from bayan.bayan.lexer import HybridLexer
from bayan.bayan.parser import HybridParser

# First interpreter - create and export
interp1 = HybridInterpreter()
code = """
parent(ali, ahmed).
parent(ahmed, sara).
grandparent(X, Z) :- parent(X, Y), parent(Y, Z).
"""
lexer = HybridLexer(code + "\n")
tokens = lexer.tokenize()
parser = HybridParser(tokens)
ast = parser.parse()
interp1.interpret(ast)

print("Interpreter 1 KB:")
for k, v in interp1.logical.knowledge_base.items():
    print(f"  {k}: {v}")

# Export
lexer2 = HybridLexer('export_knowledge("test_kb.json")\n')
tokens2 = lexer2.tokenize()
parser2 = HybridParser(tokens2)
ast2 = parser2.parse()
interp1.interpret(ast2)

# Check exported JSON
with open("test_kb.json", "r") as f:
    data = json.load(f)
print("\nExported JSON:")
print(json.dumps(data, indent=2))

# Second interpreter - import
interp2 = HybridInterpreter()
# Initialize logical engine with a dummy fact
lexer3 = HybridLexer("dummy(1).\n")
parser3 = HybridParser(lexer3.tokenize())
interp2.interpret(parser3.parse())

print("\nInterpreter 2 KB before import:")
for k, v in interp2.logical.knowledge_base.items():
    print(f"  {k}: {v}")

# Import
lexer4 = HybridLexer('import_knowledge("test_kb.json")\n')
parser4 = HybridParser(lexer4.tokenize())
interp2.interpret(parser4.parse())

print("\nInterpreter 2 KB after import:")
for k, v in interp2.logical.knowledge_base.items():
    print(f"  {k}: {v}")

# Query
lexer5 = HybridLexer("query grandparent(ali, ?X).\n")
parser5 = HybridParser(lexer5.tokenize())
results = interp2.interpret(parser5.parse())
print(f"\nQuery results: {results}")

# Cleanup
if os.path.exists("test_kb.json"):
    os.remove("test_kb.json")
