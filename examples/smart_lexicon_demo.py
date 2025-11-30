from bayan.bayan.smart_lexicon import SmartLexicon
import sys

def print_enriched_entry(entry):
    if not entry:
        print("Entry not found.")
        return
        
    print(f"\nConcept: {entry['concept']}")
    print(f"Word: {entry['basic_info']['lemma']} ({entry['lang']})")
    print("-" * 30)
    print(f"Narrative: {entry['energy_analysis']['narrative']}")
    print("-" * 30)

def main():
    print("Initializing Smart Lexicon...")
    # Point to the correct relative path of the lexicon file
    sl = SmartLexicon("ai/lexicon.bayan")
    
    if not sl.lexicon_data:
        print("Failed to load lexicon data. Exiting.")
        return

    print(f"Loaded {len(sl.get_all_concepts())} concepts.")

    # 1. Enrichment Demo
    print("\n=== 1. Enrichment Demo: 'Study' ===")
    # English
    en_entry = sl.enrich_entry("action_study", "en")
    print_enriched_entry(en_entry)
    
    # Arabic
    ar_entry = sl.enrich_entry("action_study", "ar")
    print_enriched_entry(ar_entry)

    # 2. Energy Search Demo
    print("\n=== 2. Energy Search Demo ===")
    
    # Search for "Flow" in English
    keyword = "Flow"
    print(f"\nSearching for English words with energy: '{keyword}'...")
    results = sl.search_by_energy(keyword, "en")
    for res in results[:5]: # Show top 5
        print(f" - {res['basic_info']['lemma']}: {res['energy_analysis']['narrative']}")
        
    # Search for "Containment" in Arabic
    keyword = "Containment" # The WEM outputs English descriptions for Arabic letters too
    print(f"\nSearching for Arabic words with energy: '{keyword}'...")
    results = sl.search_by_energy(keyword, "ar")
    for res in results[:5]:
        print(f" - {res['basic_info']['lemma']}: {res['energy_analysis']['narrative']}")

if __name__ == "__main__":
    main()
