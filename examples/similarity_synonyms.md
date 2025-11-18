# Synonyms/Similarity — المترادفات/التشابه

This example shows how to declare similarity with native sugar and how to query it inside a hybrid block.

```bayan
# Declarations (auto-generate similar/5 facts with symmetry)
أسد(غضنفر:0.8, هيضم:0.5)
روح(نفس:0.9, ذات:0.5)
ذهب(راح:0.8, انطلق:0.6, سار:0.7)

hybrid {
  import bayan.core.similarity as sim
  # Load rules and thresholds for similar/5, close/3, close/4, synonym/3
  sim.load_selective(logical, ["similarity"]) 

  # Numeric score lookup (prints ?S=0.8)
  query similar("أسد", "غضنفر", ?S, "syn", "lexicon").

  # Default threshold (Kind="syn" ⇒ τ=0.7)
  query close("أسد", "غضنفر", "syn").      # (true)
  query close("أسد", "هيضم", "syn").        # (no solutions) because 0.5 < 0.7

  # Custom threshold
  query close("أسد", "هيضم", 0.5, "syn").   # (true)

  # Enumerate all synonyms above default τ
  query close("أسد", ?كلمة, "syn").          # e.g., ?كلمة=غضنفر

  # Cross-domain example (alias in chemistry)
  sim.assert_similar("H2O", "Water", 1.0, kind="alias", domain="chem")
  query close("H2O", "Water", "alias").     # (true)
}
```
