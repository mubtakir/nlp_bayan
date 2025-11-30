#!/usr/bin/env python3
"""Test different ways to load Camel Tools Generator"""

from camel_tools.morphology.database import MorphologyDB
from camel_tools.morphology.generator import Generator

print("Testing Generator loading methods...")
print("=" * 60)

# Method 1: Try builtin_db with different parameters
print("\n1. Testing builtin_db():")
try:
    db = MorphologyDB.builtin_db()
    print(f"   Default DB loaded: {db}")
    print(f"   Supports generation: {db.flags}")
except Exception as e:
    print(f"   Error: {e}")

# Method 2: List available databases
print("\n2. Listing available databases:")
try:
    from camel_tools.data import CATALOGUE
    print("   Available databases:")
    for name, info in CATALOGUE.items():
        if 'morphology' in name:
            print(f"     - {name}: {info.get('description', 'N/A')}")
except Exception as e:
    print(f"   Error: {e}")

# Method 3: Try to create Generator with default DB
print("\n3. Testing Generator with default DB:")
try:
    db = MorphologyDB.builtin_db()
    gen = Generator(db)
    print(f"   Generator created successfully!")
    
    # Test generation
    result = gen.generate('كتب', {'pos': 'verb', 'asp': 'p', 'per': '3', 'gen': 'm', 'num': 's', 'vox': 'a'})
    print(f"   Test generation result: {result[:2] if result else 'None'}")
except Exception as e:
    print(f"   Error: {e}")

print("\n" + "=" * 60)
