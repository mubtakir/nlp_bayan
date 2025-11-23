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
result = interp.interpret(ast)

# Check knowledge base
print(f"Knowledge base: {interp.logical.knowledge_base}")
for pred_name, items in interp.logical.knowledge_base.items():
    print(f"  {pred_name}:")
    for item in items:
        print(f"    Type: {type(item)}, Value: {item}")
        if hasattr(item, 'predicate'):
            print(f"      predicate type: {type(item.predicate)}, value: {item.predicate}")
