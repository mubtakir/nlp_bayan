import asyncio
from bayan.bayan.istinbat_engine import IstinbatEngine
from bayan.bayan.logical_engine import Fact, Predicate, Term, TemporalOperator

def verify_worlds():
    print("\n🚀 Verifying Parallel Worlds")
    engine = IstinbatEngine(enable_dialect_support=False)
    
    # 1. Setup Reality
    print("--- Setting up Reality ---")
    # Add fact manually for test since we aren't parsing full text yet
    engine.logical_engine.add_fact(Fact(Predicate("exists", [Term("Oil")])))
    engine.logical_engine.add_fact(Fact(Predicate("price", [Term("High")])))
    print("Reality: exists(Oil), price(High)")

    # 2. Clone World
    print("\n--- Cloning World to 'NoOilWorld' ---")
    engine.create_world("NoOilWorld")
    engine.switch_world("NoOilWorld")

    # Modify new world
    # Retract not fully implemented in high level API, manually removing
    engine.logical_engine.retract(Predicate("exists", [Term("Oil")]))
    engine.logical_engine.add_fact(Fact(Predicate("energy", [Term("Solar")])))
    print("NoOilWorld: Retracted Oil, Added Solar")

    # 3. Verify Isolation
    print("\n--- Verifying Isolation ---")
    
    # Check Reality
    engine.switch_world("Reality")
    reality_has_oil = any(f.predicate.args[0].value == "Oil" for f in engine.logical_engine.knowledge_base.get("exists", []))
    print(f"Reality has Oil? {'✅ Yes' if reality_has_oil else '❌ No'}")
    
    if not reality_has_oil:
        print("FAILURE: Reality was modified by clone!")
        return False

    # Check NoOilWorld
    engine.switch_world("NoOilWorld")
    clone_has_oil = any(f.predicate.args[0].value == "Oil" for f in engine.logical_engine.knowledge_base.get("exists", []))
    print(f"NoOilWorld has Oil? {'✅ No' if not clone_has_oil else '❌ Yes'}")

    if clone_has_oil:
        print("FAILURE: Clone was not modified correctly!")
        return False

    # 4. Compare Worlds
    print("\n--- Comparing Worlds ---")
    diffs = engine.compare_worlds("Reality", "NoOilWorld")
    for d in diffs:
        print(d)

    valid_diff = any("[- REMOVED] exists(Oil)" in d for d in diffs) and \
                 any("[+ ADDED] energy(Solar)" in d for d in diffs)
    
    print(f"Diff detection correct? {'✅ Yes' if valid_diff else '❌ No'}")
    return valid_diff

def verify_balagha():
    print("\n📜 Verifying Balagha (Eloquence)")
    engine = IstinbatEngine(enable_dialect_support=False)
    engine.set_context(["sports", "game", "ball", "hit", "player"])

    # 1. Verbose
    verbose_text = "The player named John proceeded to forcefully hit the ball with great strength during the sports game event"
    print(f"\nEvaluating Verbose: '{verbose_text}'")
    score1 = engine.balagha_engine.evaluate(verbose_text, engine.active_context)
    print(f"Score: Conciseness={score1.conciseness:.2f}, Relevance={score1.relevance:.2f}, Total={score1.total:.2f}")

    # 2. Concise
    concise_text = "John hit the ball"
    print(f"\nEvaluating Concise: '{concise_text}'")
    score2 = engine.balagha_engine.evaluate(concise_text, engine.active_context)
    print(f"Score: Conciseness={score2.conciseness:.2f}, Relevance={score2.relevance:.2f}, Total={score2.total:.2f}")

    if score2.conciseness > score1.conciseness:
        print("✅ Conciseness check passed")
    else:
        print("❌ Conciseness check passed")
        return False
        
    return True

def verify_hierarchy():
    print("\n🌳 Verifying Hierarchy & Cycles")
    engine = IstinbatEngine(enable_dialect_support=False)
    
    # Define Cycle
    water_cycle = ["Evaporation", "Condensation", "Precipitation", "Collection"]
    print(f"Defining Cycle: {water_cycle}")
    engine.hierarchy_engine.define_cycle("WaterCycle", water_cycle)
    
    # Verify Facts
    facts = engine.logical_engine.knowledge_base
    
    # Check "next" relations
    print("Checking 'next' relations...")
    next_rels = [f.predicate for f in facts.get("next", [])]
    has_loop = False
    for p in next_rels:
        print(f"  {p}")
        if p.args[1].value == "Collection" and p.args[2].value == "Evaporation":
            has_loop = True
            
    print(f"Cycle Loop Detected? {'✅ Yes' if has_loop else '❌ No'}")
    
    # Check "cause" relations (Temporal Logic)
    print("Checking 'cause' relations...")
    cause_rels = []
    for f in facts.get("cause", []):
        if f.temporal_op == TemporalOperator.NEXT:
            cause_rels.append(f)
            
    if len(cause_rels) == 4:
         print(f"✅ Found 4 causal links with NEXT operator.")
    else:
         print(f"❌ Found {len(cause_rels)} causal links (expected 4).")
         return False

    return has_loop

if __name__ == "__main__":
    r1 = verify_worlds()
    r2 = verify_balagha()
    r3 = verify_hierarchy()
    
    if r1 and r2 and r3:
        print("\n✨ ALL TESTS PASSED: Advanced Features Ported Successfully! ✨")
    else:
        print("\n⚠️ SOME TESTS FAILED")
