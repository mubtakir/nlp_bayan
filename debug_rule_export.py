from bayan.bayan.hybrid_interpreter import HybridInterpreter
from bayan.bayan.lexer import HybridLexer
from bayan.bayan.parser import HybridParser
import json

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

# Check knowledge base
print("Knowledge base:")
for pred_name, items in interp.logical.knowledge_base.items():
    print(f"  {pred_name}:")
    for item in items:
        print(f"    {item}")
        if hasattr(item, 'head') and hasattr(item, 'body'):
            print(f"      head: {item.head}")
            print(f"      body: {item.body}")
            print(f"      body length: {len(item.body)}")

# Export
data = interp.logical.to_json()
print("\nExported JSON:")
print(json.dumps(data, indent=2, ensure_ascii=False))
