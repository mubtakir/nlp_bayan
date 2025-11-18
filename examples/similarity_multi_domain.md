# Similarity (Multi-Domain) — التشابه عبر مجالات متعددة

This example demonstrates using different Kinds/Domains (alias, approx_eq, etc.) with the similarity core and querying them.

```bayan
hybrid {
  import bayan.core.similarity as sim
  sim.load_selective(logical, ["similarity"])  # loads similar/5, close/3, close/4

  # Alias in chemistry domain
  sim.assert_similar("H2O", "Water", 1.0, kind="alias", domain="chem")
  query close("H2O", "Water", "alias").      # (true)

  # Approximate equality for measurement units (physics/units)
  sim.assert_similar("m", "cm", 0.9, kind="approx_eq", domain="units")
  sim.assert_similar("kg", "g", 0.9, kind="approx_eq", domain="units")
  query close("m", "cm", "approx_eq").        # (true)
  query close("kg", "g", 0.95, "approx_eq").  # (no solutions) because 0.9 < 0.95

  # You can mix in lexicon synonyms too
  أسد(غضنفر:0.8, هيضم:0.5)
  query close("أسد", "غضنفر", "syn").         # (true)
}
```
