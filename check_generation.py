from camel_tools.morphology.database import MorphologyDB
from camel_tools.morphology.generator import Generator

print("Initializing Generator...")
try:
    # Load synthesis DB explicitly
    db = MorphologyDB('calima-msa-s31')
    generator = Generator(db)
    print("Generator initialized with s31.")
    
    # Test Generation
    # Lemma: درس
    # Features: pos:verb, aspect:perf, per:3, gen:m, num:s
    lemma = 'دَرَسَ'
    features = {
        'lex': lemma,
        'pos': 'verb',
        'asp': 'p', # perfect (past)
        'per': '3',
        'gen': 'm',
        'num': 's',
        'vox': 'a' # active
    }
    
    print(f"Generating for {lemma} (Past, 3ms):")
    generated = generator.generate(lemma, features)
    print(f"Result: {generated}")
    
    # Test Dual
    features['num'] = 'd'
    print(f"Generating for {lemma} (Past, 3md):")
    generated = generator.generate(lemma, features)
    print(f"Result: {generated}")

except Exception as e:
    print(f"Error: {e}")
