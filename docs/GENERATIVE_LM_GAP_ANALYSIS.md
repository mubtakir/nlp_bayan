# Gap Analysis: From Conceptual LM to Generative LM

To build a full Generative Language Model (GLM) based on the existing Conceptual LM stack, we need to bridge the gap between **Abstract Meaning** (Traces/Blueprints) and **Surface Text** (Arabic/English strings).

## Current Status
- **Conceptual Layer**: ✅ Complete (Traces, Blueprints, Circuits, Programs).
- **Bridge Layer**: ⚠️ Partial (Maps to sentence patterns, but not to words).
- **Surface Layer**: ❌ Stub (Realizer just counts entities or uses hardcoded labels).
- **NLP Layer**: ⚠️ Basic (Analysis tools only: TF-IDF, Naive Bayes. No generation/morphology).

## Missing Components (The "Generative" Pipeline)

### 1. Lexical Mapper (The Dictionary)
**Role:** Maps abstract concepts to language-specific lemmas.
- **Input:** `Concept(Action="study", Domain="education")`
- **Output:** `Lemma("درس", POS="verb")` (Arabic), `Lemma("study", POS="verb")` (English).
- **Needs:** A bilingual dictionary database (JSON/Bayan) mapping concepts to lemmas with synonyms.

### 2. Morphological Generator (The Grammar Engine)
**Role:** Converts lemmas + grammatical features into surface word forms.
- **Input:** `Lemma("درس")` + `Features(Tense="past", Actor="3rd_male_singular")`
- **Output:** "دَرَسَ"
- **Needs:** A rule-based morphology system (especially for Arabic verb conjugations and noun declensions).

### 3. Surface Linearizer (The Assembler)
**Role:** Traverses the `SentenceTree` and assembles words, handling agreement.
- **Input:** Tree with lemmas and features.
- **Output:** List of words in order (e.g., VSO for Arabic: "درس الطالب...").
- **Needs:** Agreement logic (Subject-Verb agreement, Noun-Adjective agreement).

### 4. Probabilistic Refinement (The "LM" Polish)
**Role:** Selects the best synonym or word order based on n-gram statistics.
- **Input:** Candidate sentences.
- **Output:** Most natural sentence.
- **Needs:** Integration with `ai/nlp.bayan` n-grams to score candidates.

## Proposed Roadmap

1.  **Phase 1: Lexicon**: Build `ai/lexicon.bayan` with basic concept-to-lemma mappings.
2.  **Phase 2: Morphology**: Build `ai/morphology.bayan` for basic Arabic/English inflection.
3.  **Phase 3: Realizer**: Upgrade `ai/conceptual_surface_realizer.bayan` to use Lexicon + Morphology.
4.  **Phase 4: Generation**: Connect `conceptual_programs` -> `Realizer` -> `Text`.
