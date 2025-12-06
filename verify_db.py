import sqlite3
import sys

db_path = '/home/al-mubtakir/Documents/bayan_python_ide1/bayan/bayan/arramooz_dictionary.db'

try:
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    print(f"Checking database: {db_path}")
    
    # Get tables
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    print(f"Tables found: {[t[0] for t in tables]}")
    
    required_tables = ['nouns', 'verbs']
    missing_tables = [t for t in required_tables if t not in [x[0] for x in tables]]
    
    if missing_tables:
        print(f"❌ Missing tables: {missing_tables}")
        sys.exit(1)
        
    # Check columns for nouns
    print("\nChecking 'nouns' table columns:")
    cursor.execute("PRAGMA table_info(nouns)")
    columns = [row[1] for row in cursor.fetchall()]
    print(columns)
    
    # Check columns for verbs
    print("\nChecking 'verbs' table columns:")
    cursor.execute("PRAGMA table_info(verbs)")
    columns = [row[1] for row in cursor.fetchall()]
    print(columns)
    
    # Check row counts
    cursor.execute("SELECT count(*) FROM nouns")
    nouns_count = cursor.fetchone()[0]
    cursor.execute("SELECT count(*) FROM verbs")
    verbs_count = cursor.fetchone()[0]
    
    print(f"\nStats:")
    print(f"Nouns: {nouns_count}")
    print(f"Verbs: {verbs_count}")
    print(f"Total: {nouns_count + verbs_count}")
    
    conn.close()
    print("\n✅ Database structure looks correct.")

except Exception as e:
    print(f"❌ Error: {e}")
    sys.exit(1)
