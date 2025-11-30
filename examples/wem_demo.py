from bayan.bayan.word_energy_matrix import WordEnergyMatrix
import sys

def print_analysis(result):
    print(f"\n{'='*40}")
    print(f"Word: {result['word'].upper()}")
    print(f"{'='*40}")
    
    print("\n1. Letter Analysis:")
    for item in result['letters']:
        char = item['char']
        data = item['data']
        if data:
            print(f"  [{char.upper()}] {data.category}: {data.meaning}")
        else:
            print(f"  [{char}] (No data)")
            
    print("\n2. Structural Flow:")
    print(f"  Start : {result['structure']['start']}")
    print(f"  Core  : {result['structure']['core']}")
    print(f"  End   : {result['structure']['end']}")
    
    print("\n3. Narrative:")
    print(f"  {result['narrative']}")

def main():
    wem = WordEnergyMatrix()
    
    # English Examples from the research file
    english_words = [
        "LIFE", "LOVE", "LIGHT", "TIME", "FORM", "POWER", "MIND"
    ]
    
    print("\nAnalyzing English Words from Research...")
    for word in english_words:
        analysis = wem.analyze_word(word, 'en')
        print_analysis(analysis)

    # Arabic Examples
    arabic_words = [
        "علم", "كتب", "بحر"
    ]
    
    print("\n\nAnalyzing Arabic Words...")
    for word in arabic_words:
        analysis = wem.analyze_word(word, 'ar')
        print_analysis(analysis)

if __name__ == "__main__":
    main()
