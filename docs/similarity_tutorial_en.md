# Extended Tutorial: Synonyms/Similarity in Bayan

This tutorial shows how to declare synonym/similarity relations using native syntax and how to query them inside hybrid logic using the official module `bayan.core.similarity`.

- Native declarations (sugar): `Head(term:score, term:score, ...)`
  - Example: `Asad("غضنفر":0.8, "هيضم":0.5)` — but in Arabic you typically write the head in Arabic, e.g. `أسد(غضنفر:0.8, هيضم:0.5)`
- Semantics: for each pair, two facts are generated automatically (symmetry):
  - `similar(Head, Term, Score, "syn", "lexicon")`
  - `similar(Term, Head, Score, "syn", "lexicon")`
- Queries provided by the module:
  - `close(X, Y, Kind)` uses the default threshold for that Kind (e.g. syn → 0.7)
  - `close(X, Y, Tau, Kind)` uses a custom threshold Tau

Note: Inside `hybrid { ... }`, logical statements like facts/rules/queries are usually ended with a trailing dot `.`.

## 1) Quick start: declare and query

At top-level, declare synonyms with the native sugar:

```bayan
أسد(غضنفر:0.8, هيضم:0.5)
روح(نفس:0.9, ذات:0.5)
ذهب(راح:0.8, انطلق:0.6, سار:0.7)
```

Then in a hybrid block, load the module rules and query:

```bayan
hybrid {
  import bayan.core.similarity as sim
  sim.load_selective(logical, ["similarity"])  # similar/5, sim_threshold/2, close/3, close/4, synonym/3

  # Numeric score (prints ?S=0.8)
  query similar("أسد", "غضنفر", ?S, "syn", "lexicon").

  # Default-threshold (syn → 0.7)
  query close("أسد", "غضنفر", "syn").      # (true)
  query close("أسد", "هيضم", "syn").        # (no solutions) because 0.5 < 0.7

  # Custom threshold
  query close("أسد", "هيضم", 0.5, "syn").   # (true)
  query close("أسد", "هيضم", 0.6, "syn").   # (no solutions)

  # Enumerate all close synonyms above the default tau
  query close("أسد", ?Word, "syn").         # e.g., ?Word=غضنفر
}
```

The hybrid interpreter will print variable bindings like `?S=0.8` or `(true)/(no solutions)` for ground queries.

## 2) Building synsets programmatically

Sometimes you want to build a synset from a dictionary, a comma string, or a list. Use:

```
sim.synset(head, items, default=0.7, kind="syn", domain="lexicon")
```

- `items` can be:
  - Dict: `{"term":score, ...}`
  - String: `"term1:0.8, term2:0.6, term3"` (missing score → uses default)
  - List: `[("term", 0.8), ("other", 0.6), "third"]`

Example:

```bayan
hybrid {
  import bayan.core.similarity as sim
  sim.load_selective(logical, ["similarity"])

  sim.synset("طالب", "تلميذ:0.8, دارس:0.6, متعلم")
  query close("طالب", ?Y, "syn").         # e.g., ?Y=تلميذ, ?Y=متعلم
}
```

## 3) Cross-domain examples (beyond lexicon)

You can store different kinds and domains, e.g. aliases or approximate equality for units.

```bayan
hybrid {
  import bayan.core.similarity as sim
  sim.load_selective(logical, ["similarity"])  # loads thresholds too

  sim.assert_similar("H2O", "Water", 1.0, kind="alias", domain="chem")
  query close("H2O", "Water", "alias").     # (true)
}
```

The current `close/3` rule filters by Kind only and ignores Domain on purpose. If you need domain-specific filtering, add a custom rule that constrains on Domain, or use `similar/5` directly in your queries.

## 4) Printing booleans directly (optional)

Besides `query ... .`, you can also use `print(close(...))` to print `True/False` inside hybrid, because function calls with logical variables (or calls to `close/3,4`) are recognized as logical queries:

```bayan
hybrid {
  import bayan.core.similarity as sim
  sim.load_selective(logical, ["similarity"])

  print(close("أسد", "غضنفر", "syn"))    # True
  print(close("أسد", "هيضم", "syn"))      # False
  print(close("أسد", "هيضم", 0.4, "syn")) # True (0.5 ≥ 0.4)
}
```

## 5) Common pitfalls

- Forgetting to load the module rules into your logical engine: call `sim.load_selective(logical, ["similarity"])` before using `close`.
- Non-numeric score in `Head(term:score)`: the score must be numeric; otherwise you will get a runtime error.
- Expecting Domain filtering in `close/3`: it currently filters by Kind only. Add a domain-specific rule if needed, or use `close/4` with custom logic.
- Inside hybrid, remember to end logical statements with a dot `.`.

## 6) Where to go next

- Reference grammar and details: see docs/reference.md, section “Similarity Declarations”.
- Cookbook examples: docs/cookbook.md (soon to include similarity snippets).
- Full Arabic tutorial: docs/similarity_tutorial_ar.md.

