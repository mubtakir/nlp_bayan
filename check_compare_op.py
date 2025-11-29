import dis
import sys

print(f"Python Version: {sys.version}")

ops = ['<', '<=', '==', '!=', '>', '>=']
for op in ops:
    print(f"\n--- Native Bytecode for '1 {op} 2' ---")
    code_str = f"1 {op} 2"
    code = compile(code_str, "<string>", "eval")
    dis.dis(code)


