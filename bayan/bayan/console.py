#!/usr/bin/env python3
"""
Bayan Interactive Console (REPL)
قشرة بيان التفاعلية
"""

import sys
import os
import readline
import atexit

# Ensure we can import bayan packages
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from bayan.bayan.istinbat_engine import IstinbatEngine, Fact, Predicate, Term, Concept, Relation
from bayan.bayan.logical_engine import ModalOperator, TemporalOperator

class BayanConsole:
    def __init__(self):
        print("🔄 Initializing Bayan Engine... / جاري تهيئة محرك بيان...")
        self.engine = IstinbatEngine(enable_dialect_support=True)
        self.history_file = os.path.expanduser("~/.bayan_history")
        self.init_history()
        
    def init_history(self):
        try:
            readline.read_history_file(self.history_file)
            readline.set_history_length(1000)
        except FileNotFoundError:
            pass
        atexit.register(readline.write_history_file, self.history_file)

    def print_banner(self):
        banner = """
        ╔══════════════════════════════════════════════╗
        ║       Bayan Python Interactive Console       ║
        ║           قشرة بيان التفاعلية (v2.0)           ║
        ╚══════════════════════════════════════════════╝
        Type 'exit' or 'خروج' to quit.
        Type 'help' or 'مساعدة' for commands.
        """
        print(banner)

    def print_help(self):
        help_text = """
        Commands / الأوامر:
        -------------------
        fact <predicate>(<arg1>, <arg2>)  : Add a fact / إضافة حقيقة
        حقيقة <محمول>(<معامل1>, <معامل2>)
        
        query <predicate>(<arg1>, <arg2>) : Query facts / استعلام
        استعلم <محمول>(<معامل1>, <معامل2>)
        
        search <text>                     : Semantic search / بحث دلالي
        ابحث <نص>
        
        world <name>                      : Switch world / تبديل العالم
        عالم <اسم>
        
        create_world <name>               : Create new world / إنشاء عالم
        انشئ_عالم <اسم>
        
        load_arramooz                     : Load dictionary / تحميل القاموس
        حمل_القاموس
        """
        print(help_text)

    def process_command(self, line):
        line = line.strip()
        if not line:
            return

        parts = line.split(maxsplit=1)
        cmd = parts[0].lower()
        args = parts[1] if len(parts) > 1 else ""

        if cmd in ['exit', 'quit', 'خروج']:
            print("Goodbye! / مع السلامة!")
            sys.exit(0)
            
        elif cmd in ['help', '?', 'مساعدة']:
            self.print_help()
            
        elif cmd in ['load_arramooz', 'حمل_القاموس']:
            self.engine.initialize_knowledge()
            print("✅ Arramooz loaded / تم تحميل القاموس")
            
        elif cmd in ['search', 'ابحث']:
            if not args:
                print("⚠️  Provide text to search / أدخل نصاً للبحث")
                return
            print(f"🔍 Searching for: {args}...")
            results = self.engine.neural_search(args)
            if results:
                for fact, score, text in results:
                    print(f"   ★ {text} (Score: {score:.3f})")
            else:
                print("   No results found / لا توجد نتائج")

        elif cmd in ['fact', 'حقيقة']:
            # Simple parsing: fact loves(Ali, Reading)
            try:
                # Extract content between parens
                if '(' not in args or ')' not in args:
                    print("❌ Format: fact pred(arg1, arg2)")
                    return
                
                pred_name = args.split('(')[0].strip()
                args_str = args[args.find('(')+1 : args.rfind(')')]
                arg_list = [Term(a.strip()) for a in args_str.split(',')]
                
                self.engine.logical_engine.add_fact(Fact(Predicate(pred_name, arg_list)))
                print(f"✅ Fact added: {pred_name}({', '.join(str(a) for a in arg_list)})")
                
            except Exception as e:
                print(f"❌ Error: {e}")

        elif cmd in ['query', 'استعلم', 'q']:
            try:
                if '(' not in args or ')' not in args:
                    print("❌ Format: query pred(arg1, arg2)")
                    return
                
                pred_name = args.split('(')[0].strip()
                args_str = args[args.find('(')+1 : args.rfind(')')]
                # Handle variables (uppercase start)
                arg_list = []
                for a in args_str.split(','):
                    a = a.strip()
                    if a and a[0].isupper(): # Convention: Uppercase = specific term
                        arg_list.append(Term(a))
                    else:
                        arg_list.append(a) # Variable string
                
                results = self.engine.logical_engine.query(Predicate(pred_name, arg_list))
                if results:
                    print(f"✅ Found {len(results)} matches:")
                    for res in results:
                        print(f"   {res}")
                else:
                    print("❌ No match found (False)")
                    
            except Exception as e:
                print(f"❌ Error: {e}")

        elif cmd in ['world', 'عالم']:
            if self.engine.switch_world(args):
                print(f"🌍 Switched to world: {args}")
            else:
                print(f"❌ World '{args}' does not exist.")

        elif cmd in ['create_world', 'انشئ_عالم']:
            self.engine.create_world(args)
            print(f"🌍 Created world: {args}")

        else:
            # Try to eval as python code inside engine context?
            # or just complain
            print(f"❓ Unknown command: {cmd}")

    def run(self):
        self.print_banner()
        while True:
            try:
                # Dynamic prompt based on active world
                world = getattr(self.engine, 'active_world_name', 'Reality')
                prompt = f"Bayan({world})> "
                line = input(prompt)
                self.process_command(line)
            except KeyboardInterrupt:
                print("\nType 'exit' to quit.")
            except EOFError:
                print("\nGoodbye!")
                break
            except Exception as e:
                print(f"❌ System Error: {e}")

if __name__ == "__main__":
    console = BayanConsole()
    console.run()
