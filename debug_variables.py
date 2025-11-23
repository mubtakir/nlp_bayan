from bayan.bayan.hybrid_interpreter import HybridInterpreter
from bayan.bayan.lexer import HybridLexer
from bayan.bayan.parser import HybridParser

interp = HybridInterpreter()

# Add facts and rule
code = """
parent(ali, ahmed).
grandparent(X, Z) :- parent(X, Y), parent(Y, Z).
"""
lexer = HybridLexer(code + "\n")
tokens = lexer.tokenize()
parser = HybridParser(tokens)
ast = parser.parse()
interp.interpret(ast)

print("Knowledge base details:")
for pred_name, items in interp.logical.knowledge_base.items():
    print(f"\n{pred_name}:")
    for item in items:
        print(f"  Item: {item}")
        if hasattr(item, 'predicate'):
            print(f"    Predicate: {item.predicate}")
            print(f"    Predicate.args: {item.predicate.args}")
            for i, arg in enumerate(item.predicate.args):
                print(f"      arg[{i}]: {arg}, is_variable={arg.is_variable}")
        if hasattr(item, 'head'):
            print(f"    Head: {item.head}")
            print(f"    Head.args: {item.head.args}")
            for i, arg in enumerate(item.head.args):
                print(f"      arg[{i}]: {arg}, is_variable={arg.is_variable}")
            print(f"    Body: {item.body}")
            for i, pred in enumerate(item.body):
                print(f"      body[{i}]: {pred}")
                for j, arg in enumerate(pred.args):
                    print(f"        arg[{j}]: {arg}, is_variable={arg.is_variable}")
