import os
import sys

# Add project root to path properly
# We need the parent of 'bayan' folder to be in sys.path to import 'bayan.bayan...'
project_root = os.path.abspath(os.path.dirname(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

def verify_stdlib():
    print("📚 Verifying Bayan Standard Library Expansion...")
    
    # 1. Random Library
    try:
        from bayan.bayan.stdlib.random_lib import randint, choice, shuffle
        print("\n🎲 Testing Random Library:")
        
        r_int = randint(1, 100)
        print(f"   randint(1, 100) = {r_int} {'✅' if 1 <= r_int <= 100 else '❌'}")
        
        items = ['Apple', 'Banana', 'Cherry']
        chosen = choice(items)
        print(f"   choice({items}) = {chosen} {'✅' if chosen in items else '❌'}")
        
        original_list = [1, 2, 3, 4, 5]
        shuffled = list(original_list)
        shuffle(shuffled)
        print(f"   shuffle({original_list}) = {shuffled} {'✅' if set(original_list) == set(shuffled) else '❌'}")
        
    except ImportError as e:
        print(f"❌ Random Library Import Error: {e}")

    # 2. System Library
    try:
        from bayan.bayan.stdlib.system_lib import execute, get_env
        print("\n🖥️  Testing System Library:")
        
        res = execute('echo "Bayan System Test"')
        print(f"   execute('echo ...'): Success={res['success']}, Output='{res['stdout'].strip()}' {'✅' if 'Bayan' in res['stdout'] else '❌'}")
        
        user = get_env('USER', 'unknown')
        print(f"   get_env('USER') = {user} {'✅' if user else '⚠️'}")
        
    except ImportError as e:
        print(f"❌ System Library Import Error: {e}")

    # 3. CSV Library
    try:
        from bayan.bayan.stdlib.csv_lib import write_csv, read_csv
        print("\n📊 Testing CSV Library:")
        
        test_file = 'test_bayan.csv'
        data = [
            {'name': 'Ali', 'age': 25},
            {'name': 'Sara', 'age': 22}
        ]
        
        # Write
        write_success = write_csv(test_file, data)
        print(f"   write_csv: {write_success} {'✅' if write_success else '❌'}")
        
        # Read
        read_data = read_csv(test_file)
        print(f"   read_csv: {read_data}")
        is_match = len(read_data) == 2 and read_data[0]['name'] == 'Ali'
        print(f"   Data Integrity: {'✅' if is_match else '❌'}")
        
        # Clean up
        if os.path.exists(test_file):
            os.remove(test_file)
            
    except ImportError as e:
        print(f"❌ CSV Library Import Error: {e}")

if __name__ == "__main__":
    verify_stdlib()
