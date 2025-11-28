import sys
import os
import json

# Add the project root to the path so we can import bayan modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from bayan.bayan.reverse_glm import ReverseGLM

def main():
    print("=== Reverse GLM Demo: Arabic NL -> Conceptual Circuits ===\n")
    
    # Example text containing multiple discourse markers, including the complex one reported by the user
    text = """
    إنّ الذكاء الاصطناعي يتطور بسرعة هائلة.
    هذا يدل على أنّ المستقبل سيشهد تغييرات جذرية في سوق العمل.
    بينما الطرق التقليدية في التعليم قد تصبح أقل فعالية.
    فكلما كان الاعتماد على الأتمتة أكبر، زادت الحاجة إلى مهارات بشرية فريدة.
    اذا اردت معرفة تأثير ذلك فعليك دراسة التاريخ الاقتصادي.
    """
    
    print(f"Input Text:\n{text}\n")
    print("-" * 50)
    
    # Initialize Reverse GLM
    reverse_glm = ReverseGLM()
    
    # 1. Segmentation
    print("\n1. Segmentation Phase:")
    segments = reverse_glm.segment_text(text)
    for i, (marker, content) in enumerate(segments):
        print(f"  Segment {i+1}:")
        print(f"    Marker : {marker}")
        print(f"    Content: {content[:50]}..." if len(content) > 50 else f"    Content: {content}")

    print("-" * 50)

    # 2. Mapping to Circuits
    print("\n2. Circuit Mapping Phase (Conceptualization):")
    circuits = reverse_glm.process_text(text)
    
    for i, circuit in enumerate(circuits):
        print(f"\n  Circuit {i+1} Generated:")
        print(f"    Source Segment: {circuit.get('source_text_segment')}")
        
        # Check for trace/roles to identify it as a valid circuit
        if "trace" in circuit:
            trace_meta = circuit["trace"].get("meta", {})
            source_type = trace_meta.get("source", "Unknown Circuit")
            print(f"    Circuit Type  : {source_type}")
            
            # Print some roles to show understanding
            if "roles" in circuit:
                print("    Extracted Roles:")
                for role_group, roles in circuit["roles"].items():
                    print(f"      - {role_group}: {roles}")
        else:
            print("    [Generic/Fallback Segment]")

    print("\n" + "-" * 50)
    print("Reverse GLM Processing Complete.")

if __name__ == "__main__":
    main()
