import sys
import os

# Add project root to path
sys.path.append('/home/al-mubtakir/Documents/bayan_python_ide14')

try:
    from bayan.hybrid_interpreter import HybridInterpreter
    from bayan.visualization import ExistentialVisualizer
    from bayan.lexer import HybridLexer
    from bayan.parser import HybridParser

    print("Imports successful")

    code = """
# منطقي
مبرمج(أحمد).
يكتب_كود(X) :- مبرمج(X).

# إجرائي
def greet(name): {
    return "مرحباً " + name
}

# كائني
class Person: {
    def __init__(self, name): {
        self.name = name
    }
}
    """

    print("Initializing Interpreter...")
    interpreter = HybridInterpreter()

    print("Parsing Code...")
    lexer = HybridLexer(code)
    tokens = lexer.tokenize()
    parser = HybridParser(tokens)
    ast = parser.parse()

    print("Interpreting...")
    interpreter.interpret(ast)

    print("Initializing Visualizer...")
    visualizer = ExistentialVisualizer(interpreter)

    print("Exporting Unified Graph...")
    graph = visualizer.export_unified_graph()
    
    print("Success!")
    print(f"Nodes: {len(graph['nodes'])}")
    print(f"Links: {len(graph['links'])}")

except Exception as e:
    import traceback
    print("\nERROR OCCURRED:")
    traceback.print_exc()
