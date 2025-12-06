# Implementation Plan - Proposal 2: Advanced Parser

The goal is to upgrade the `IstinbatEngine` to support complex sentence structures beyond the simple Subject-Verb-Object (SVO) pattern. This includes handling prepositions, adverbs, adjectives, and conditional statements.

## User Review Required

> [!IMPORTANT]
> This change introduces `AdvancedArabicParser` which uses Regex patterns to identify sentence structures. It will replace the simple split-based parsing in `LinguisticEquationParser`.

## Proposed Changes

### Core Logic

#### [NEW] [advanced_arabic_parser.py](file:///home/al-mubtakir/Documents/bayan_python_ide1/bayan/bayan/advanced_arabic_parser.py)
- Create `AdvancedArabicParser` class.
- **Regex Patterns**:
    - **Prepositional**: `Subject + Verb + Preposition + Object` (e.g., "محمد ذهب إلى المدرسة").
    - **Adverbial**: `Subject + Verb + Object + Time/Place` (e.g., "أحمد أكل التفاحة صباحاً").
    - **Descriptive**: `Subject + Verb + Object + Adjective` (e.g., "الرجل ضرب الكرة الكبيرة").
    - **Conditional**: `If + Condition + Then + Result` (e.g., "إذا درس الطالب فإن الطالب ينجح").

#### [MODIFY] [istinbat_engine.py](file:///home/al-mubtakir/Documents/bayan_python_ide1/bayan/bayan/istinbat_engine.py)
- Import `AdvancedArabicParser`.
- Replace `LinguisticEquationParser` with `AdvancedArabicParser` in `__init__`.

#### [MODIFY] [linguistic_equation.py](file:///home/al-mubtakir/Documents/bayan_python_ide1/bayan/bayan/linguistic_equation.py)
- Update `LinguisticEquation` class to support new fields: `preposition`, `adverb`, `adjective`, `condition`.

## Verification Plan

### Automated Tests
- Create `tests/test_advanced_parser.py`:
    - **Preposition**: Test "ذهب إلى المدرسة" -> Verify `preposition="إلى"`, `object="المدرسة"`.
    - **Adverb**: Test "أكل صباحاً" -> Verify `time="صباحاً"`.
    - **Adjective**: Test "الكرة الكبيرة" -> Verify `adjective="الكبيرة"`.
    - **Conditional**: Test "إذا درس نجح" -> Verify causal link.

### Manual Verification
- Run `tests/test_advanced_parser.py` and verify output.

