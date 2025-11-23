from bayan.bayan.hybrid_interpreter import HybridInterpreter
from bayan.bayan.lexer import HybridLexer
from bayan.bayan.parser import HybridParser

interp = HybridInterpreter()

# Test parsing the exact import code
code = "grandparent(X, Z) :- parent(X, Y), parent(Y, Z)."
print(f"Parsing: {code}")

lexer = HybridLexer(code)
tokens = lexer.tokenize()
print(f"Tokens: {tokens[:20]}")  # First 20 tokens

parser = HybridParser(tokens)
ast = parser.parse()
print(f"AST: {ast}")
print(f"AST statements: {ast.statements}")

if ast.statements:
    stmt = ast.statements[0]
    print(f"Statement type: {type(stmt)}")
    if hasattr(stmt, 'head'):
        print(f"Head: {stmt.head}")
    if hasattr(stmt, 'body'):
        print(f"Body: {stmt.body}")
        print(f"Body length: {len(stmt.body)}")
        for i, goal in enumerate(stmt.body):
            print(f"  Body[{i}]: {goal}, type={type(goal)}")

# Now interpret it
interp.interpret(ast)

print("\nKnowledge base after interpret:")
for k, v in interp.logical.knowledge_base.items():
    print(f"  {k}: {v}")
    for item in v:
        if hasattr(item, 'body'):
            print(f"    Body: {item.body}, length={len(item.body)}")
