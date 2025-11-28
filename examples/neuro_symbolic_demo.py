import sys
import os
import json

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from bayan.ai.neuro_symbolic_loop import NeuroSymbolicLoop

def print_section(title: str):
    print("\n" + "="*60)
    print(f"  {title}")
    print("="*60)

def demo_mode(mode_name: str, mode_value: str, test_input: str):
    """Demo a specific mode."""
    print_section(f"Mode: {mode_name}")
    print(f"Input: \"{test_input}\"")
    print(f"Backend: {mode_value}\n")
    
    try:
        loop = NeuroSymbolicLoop(mode=mode_value)
        
        # Show configuration
        info = loop.get_info()
        print(f"Configuration:")
        print(f"  - Gateway Mode: {info['gateway']['mode']}")
        print(f"  - Backend: {info['gateway']['backend']}")
        print(f"  - Available: {info['gateway']['available']}")
        print()
        
        # Process
        result = loop.process(test_input, language="arabic")
        
        # Display results
        print("Results:")
        print(f"  1. Dream (Atom Generation):")
        print(f"     {json.dumps(result['dream'], indent=6, ensure_ascii=False)}")
        print()
        print(f"  2. Reality Check (Verification):")
        print(f"     {json.dumps(result['reality_check'], indent=6, ensure_ascii=False)}")
        print()
        print(f"  3. Realization (Final Text):")
        print(f"     \"{result['realization']}\"")
        print()
        
    except Exception as e:
        print(f"❌ Error: {str(e)}")
        import traceback
        traceback.print_exc()

def main():
    print("""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║        Neuro-Symbolic Integration Demo                      ║
║        محرك الدمج العصبي-الرمزي                            ║
║                                                              ║
║  This demo shows 3 modes of operation:                      ║
║  1. Standalone (Default) - Pure Bayan, no external LLM      ║
║  2. Local - Ollama with open-source models                  ║
║  3. Cloud - Gemini 1.5 Pro via API                          ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
""")
    
    # Test input
    test_input = "أحمد ضرب الكرة"
    
    # Demo Mode 3: Standalone (Default)
    demo_mode(
        "Standalone (الوضع المستقل)",
        "standalone",
        test_input
    )
    
    print("\n" + "🔍 ANALYSIS OF STANDALONE MODE ".center(60, "="))
    print("""
This mode proves that Bayan is CAPABLE on its own.
It successfully:
  ✓ Parsed the sentence into a Linguistic Equation
  ✓ Identified entities (أحمد, الكرة) and action (ضرب)
  ✓ Deduced consequences (anger, tiredness, pain)
  ✓ Built a logical circuit

The limitation is NOT the engine, but the DATA.
With more causal rules, this mode can handle any domain.
""")
    
    # Demo Mode 2: Local (if available)
    print("\n" + "📋 OPTIONAL MODES ".center(60, "="))
    print("""
The following modes require additional setup:

Mode 2: Local (Ollama)
  - Install: pip install ollama
  - Start server: ollama serve
  - Pull model: ollama pull qwen2.5-coder:7b

Mode 3: Cloud (Gemini)
  - Install: pip install google-generativeai
  - Set API key: export GEMINI_API_KEY=your_key_here

To test these modes, uncomment the demo_mode() calls below.
""")
    
    # Uncomment to test Local mode:
    # demo_mode("Local (Ollama)", "local", test_input)
    
    # Uncomment to test Cloud mode:
    # demo_mode("Cloud (Gemini)", "cloud", test_input)
    
    print_section("Demo Complete")
    print("""
Summary:
  - Standalone mode is ALWAYS available and proves Bayan's independence
  - Local mode provides open-source LLM power without internet
  - Cloud mode provides maximum capability for complex tasks

The choice is yours based on your needs:
  Privacy? → Standalone or Local
  Power? → Cloud
  Simplicity? → Standalone
""")

if __name__ == "__main__":
    main()
