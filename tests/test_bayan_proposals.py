import unittest
import os
import json
from bayan.bayan.hybrid_interpreter import HybridInterpreter
from bayan.bayan.lexer import HybridLexer
from bayan.bayan.parser import HybridParser

class TestBayanProposals(unittest.TestCase):
    def setUp(self):
        self.interpreter = HybridInterpreter()
        self.test_json = "test_kb.json"

    def tearDown(self):
        if os.path.exists(self.test_json):
            os.remove(self.test_json)

    def parse_and_run(self, code):
        lexer = HybridLexer(code + "\n") # Ensure newline
        tokens = lexer.tokenize()
        # print(f"Tokens for '{code}': {tokens}")
        parser = HybridParser(tokens)
        ast = parser.parse()
        return self.interpreter.interpret(ast)

    def test_export_import_knowledge(self):
        # 1. Define knowledge
        code = """
        parent(ali, ahmed).
        parent(ahmed, sara).
        grandparent(X, Z) :- parent(X, Y), parent(Y, Z).
        """
        self.parse_and_run(code)
        
        # 2. Export
        self.parse_and_run(f'export_knowledge("{self.test_json}")')
        
        # Verify file exists
        self.assertTrue(os.path.exists(self.test_json))
        
        # 3. Create new interpreter and import
        new_interpreter = HybridInterpreter()
        # Initialize logical engine
        lexer = HybridLexer("dummy(1).\n")
        parser = HybridParser(lexer.tokenize())
        new_interpreter.interpret(parser.parse())
        
        lexer = HybridLexer(f'import_knowledge("{self.test_json}")\n')
        parser = HybridParser(lexer.tokenize())
        new_interpreter.interpret(parser.parse())
        
        # 4. Verify knowledge
        lexer = HybridLexer("query grandparent(ali, ?X).\n")
        parser = HybridParser(lexer.tokenize())
        results = new_interpreter.interpret(parser.parse())
        
        # Let's check if we get 'sara' - it should be in the second argument position
        found = False
        if results:
            for res in results:
                # Check all values in the result dictionary
                for key, value in res.items():
                    if value == 'sara' or 'sara' in str(value):
                        found = True
                        break
                if found:
                    break
        self.assertTrue(found, "Could not find grandparent relation after import")

    def test_explain(self):
        code = """
        parent(ali, ahmed).
        parent(ahmed, sara).
        grandparent(X, Z) :- parent(X, Y), parent(Y, Z).
        """
        self.parse_and_run(code)
        
        # Call explain
        explanation = self.parse_and_run('explain("grandparent(ali, sara)")')
        
        print(f"Explanation:\n{explanation}")
        self.assertIsInstance(explanation, str)
        self.assertIn("Goal: grandparent(ali, sara)", explanation)
        self.assertIn("Derived from rule", explanation)
        self.assertIn("Fact found", explanation)

    def test_what_if(self):
        # Define base knowledge
        self.parse_and_run("val(1).")
        
        # Verify base state
        # Use query keyword for logical query
        res = self.parse_and_run("query val(?X).")
        res_list = list(res)
        self.assertTrue(any("1" in str(r) for r in res_list))
        
        # What if val(2)?
        res_what_if = self.parse_and_run('what_if("val(2)", "val(?X)")')
        
        print(f"What If Result: {res_what_if}")
        self.assertIn("2", res_what_if)
        self.assertIn("1", res_what_if)
        
        # Verify side effect is gone
        res_after = self.parse_and_run("query val(?X).")
        res_after_list = list(res_after)
        self.assertFalse(any("2" in str(r) for r in res_after_list), "Side effect of what_if persisted")
        self.assertTrue(any("1" in str(r) for r in res_after_list))


if __name__ == '__main__':
    unittest.main()
