
import sys
sys.path.insert(0, 'bayan')
from tests.test_generators_execution import test_simple_generator_to_list, test_generator_in_for_loop_sum, test_fibonacci_generator_prefix

if __name__ == "__main__":
    print("Testing Generators Execution")
    print("=" * 50)
    try:
        test_simple_generator_to_list()
        print("✅ test_simple_generator_to_list passed")
    except Exception as e:
        print(f"❌ test_simple_generator_to_list failed: {e}")
        import traceback
        traceback.print_exc()

    try:
        test_generator_in_for_loop_sum()
        print("✅ test_generator_in_for_loop_sum passed")
    except Exception as e:
        print(f"❌ test_generator_in_for_loop_sum failed: {e}")
        import traceback
        traceback.print_exc()

    try:
        test_fibonacci_generator_prefix()
        print("✅ test_fibonacci_generator_prefix passed")
    except Exception as e:
        print(f"❌ test_fibonacci_generator_prefix failed: {e}")
        import traceback
        traceback.print_exc()
        
    print("=" * 50)
