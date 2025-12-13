import sys
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

def verify_neural_integration():
    print("🧠 Verifying Neural Integration...")
    
    try:
        from bayan.bayan.istinbat_engine import IstinbatEngine
        from bayan.bayan.logical_engine import Fact, Predicate, Term
        
        # 1. Initialize Engine (this loads the neural model)
        print("   Loading Unified Brain (Logic + Neural)...")
        engine = IstinbatEngine(enable_dialect_support=False)
        
        if not engine.neural_engine.initialized and engine.neural_engine.model is None:
            print("   ⚠️  Neural Engine running in fallback mode (Torch not found). Skipping deep tests.")
            return

        print("   ✅ Neural Engine loaded successfully!")
        
        # 2. Populate Knowledge Base with diverse facts
        print("\n📚 Populating Knowledge Base...")
        engine.logical_engine.add_fact(Fact(Predicate("is_hot", [Term("Sun")])))
        engine.logical_engine.add_fact(Fact(Predicate("is_cold", [Term("Ice")])))
        engine.logical_engine.add_fact(Fact(Predicate("loves", [Term("Ali"), Term("Reading")])))
        
        # 3. Neural Search Test 1: Exact Match (Semantic)
        print("\n🔍 Test 1: Semantic Search 'Something burning'")
        # "Burning" is semantically close to "Hot/Sun"
        results = engine.neural_search("Something burning", top_k=1)
        if results:
            fact, score, text = results[0]
            print(f"   Result: {text} (Score: {score:.4f})")
            if "Sun" in text:
                print("   ✅ semantic match confirmed")
            else:
                print(f"   ⚠️  Unexpected match: {text}")
        else:
            print("   ❌ No results found")

        # 4. Neural Search Test 2: Concept Matching
        print("\n🔍 Test 2: Semantic Search 'Frozen water'")
        results = engine.neural_search("Frozen water", top_k=1)
        if results:
            fact, score, text = results[0]
            print(f"   Result: {text} (Score: {score:.4f})")
            if "Ice" in text:
                print("   ✅ semantic match confirmed")
            else:
                print(f"   ⚠️  Unexpected match: {text}")

        # 5. Direct Embedding Check
        print("\n🧮 Test 3: Direct Embedding")
        vec = engine.neural_engine.embed("Peace")
        print(f"   Embedding vector shape: {vec.shape}")
        if vec.shape[0] > 0:
            print("   ✅ Vector generation works")

    except ImportError as e:
        print(f"❌ Import Failed: {e}")
    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    verify_neural_integration()
