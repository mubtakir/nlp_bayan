"""
Smart Lexicon System
====================
Integrates the Word Energy Matrix (WEM) with the Bayan Lexicon.
Allows for energy-based semantic search and deep word understanding.
"""

import re
import ast
from typing import Dict, List, Any, Optional
from bayan.bayan.word_energy_matrix import WordEnergyMatrix

class SmartLexicon:
    def __init__(self, lexicon_path: str = "ai/lexicon.bayan"):
        self.wem = WordEnergyMatrix()
        self.lexicon_data = self._load_lexicon_file(lexicon_path)
        
    def _load_lexicon_file(self, path: str) -> Dict:
        """
        Parses the ai/lexicon.bayan file to extract the dictionary.
        Since it's a Bayan file returning a dict, we'll parse the python-like dict structure.
        """
        try:
            with open(path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            # Simple state machine to extract the dict content
            dict_lines = []
            in_dict = False
            brace_count = 0
            
            for line in lines:
                stripped = line.strip()
                
                # Check for start of dict
                if not in_dict and 'return {' in line:
                    in_dict = True
                    brace_count = 1
                    dict_lines.append('{') # Start the dict
                    continue
                
                if in_dict:
                    # Remove comments
                    if '#' in line:
                        line = line.split('#')[0]
                    
                    # Count braces to find the end
                    brace_count += line.count('{')
                    brace_count -= line.count('}')
                    
                    dict_lines.append(line)
                    
                    if brace_count == 0:
                        break
            
            if not dict_lines:
                print(f"Warning: Could not find dictionary block in {path}")
                return {}

            dict_str = "".join(dict_lines)
            # Use ast.literal_eval for safe parsing
            return ast.literal_eval(dict_str)
            
        except Exception as e:
            print(f"Error loading lexicon: {e}")
            return {}

    def enrich_entry(self, concept_key: str, lang: str) -> Optional[Dict]:
        """
        Returns the lexicon entry enriched with WEM analysis.
        """
        if concept_key not in self.lexicon_data:
            return None
            
        entry = self.lexicon_data[concept_key]
        if lang not in entry:
            return None
            
        word_data = entry[lang]
        lemma = word_data.get('lemma')
        
        if not lemma:
            return None
            
        # Run WEM Analysis
        # Handle multi-word lemmas (take the first word or main word?)
        # For now, we analyze the whole string, WEM handles it letter by letter.
        # Ideally we might want to analyze the root, but let's analyze the lemma as is.
        energy_analysis = self.wem.analyze_word(lemma, lang)
        
        return {
            "concept": concept_key,
            "lang": lang,
            "basic_info": word_data,
            "energy_analysis": energy_analysis
        }

    def search_by_energy(self, energy_keyword: str, lang: str = 'en') -> List[Dict]:
        """
        Searches the lexicon for words that contain a specific energy keyword 
        in their analysis narrative or structure.
        """
        results = []
        
        for concept_key, entry in self.lexicon_data.items():
            if lang in entry:
                enriched = self.enrich_entry(concept_key, lang)
                if enriched:
                    analysis = enriched['energy_analysis']
                    # Search in narrative and structural components
                    search_text = (
                        analysis['narrative'] + " " + 
                        analysis['structure']['start'] + " " + 
                        analysis['structure']['core'] + " " + 
                        analysis['structure']['end']
                    ).lower()
                    
                    if energy_keyword.lower() in search_text:
                        results.append(enriched)
                        
        return results

    def get_all_concepts(self) -> List[str]:
        return list(self.lexicon_data.keys())
