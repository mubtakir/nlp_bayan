# Logic in Bayan Language (9): Synonyms, Proximity, and Similarity

> In previous parts we saw facts, rules, probabilities, entities, causal networks, and semantic networks.
> In this part we add an important new layer:
>
> **Synonyms and Proximity (Similarity)** as a core feature in Bayan,
> so we can say: `lion` is close to `leo` with degree 0.8 for example,
> and use that in logic, in generation, and in everything before the language model.

---

## 1. The Idea: «Proximity Set» Instead of Just One Word

We want to represent a **concept** (word, entity, or interaction...) with elements close to it with degrees [0..1].

### 1.1 Simple Linguistic Example (Higher-Level DSL)

The initial syntax proposed in the RFC:

```bayan
lion(leo:0.8, panthera:0.5)  # Default value when omitted: 0.7
```

You can read it like this:

- "lion" is the **concept head**.
- "leo" is close to it with degree 0.8 (strong synonym).
- "panthera" is close with degree 0.5 (slightly weaker).

The idea is more general than natural language; the same form can be used in other domains:

```bayan
chemical_product(reactionA:0.9, reactionB:0.6)
sound(buzz:0.8, hum:0.5)
```

---

## 2. General Similarity Module: `bayan.core.similarity`

This module provides a general logic layer (not limited to NLP), with facts and rules like:

- `similar(X, Y, Score, Kind, Domain)`
- `sim_threshold(Kind, Tau)`
- `close(X, Y, Tau, Kind)` and `close(X, Y, Kind)`
- `synonym(X, Y, S)` as sugar for linguistic synonyms.

### 2.1 Default Examples Inside the Module

Some built-in examples (you can consider them a small knowledge base):

```bayan
hybrid {
    similar("lion", "leo", 0.8, "syn", "lexicon").
    similar("lion", "panthera", 0.5, "syn", "lexicon").

    sim_threshold("syn", 0.7).
    sim_threshold("alias", 0.7).
}
```

- `"syn"` is a proximity type for linguistic synonyms.
- `"alias"` for proximity of «different names for the same thing».

---

## 3. English Interface for Querying Synonyms and Proximity

Let's define an English interface around these facts and rules:

```bayan
hybrid {
    import bayan.core.similarity as sim
    sim.load_selective(logical, ["similarity"])

    is_synonym(?original, ?word, ?degree) :- synonym(?original, ?word, ?degree).
    is_close(?original, ?word) :- close(?original, ?word, "syn").
    is_close_with_threshold(?original, ?word, ?threshold) :- close(?original, ?word, ?threshold, "syn").
}

query is_synonym("lion", ?word, ?degree)?
query is_close("lion", "leo")?
query is_close_with_threshold("lion", "panthera", 0.4)?
```

- `is_synonym/3` returns all synonymous words with their degrees.
- `is_close/2` uses the default threshold for type `"syn"` (e.g., 0.7).
- `is_close_with_threshold/3` allows you to set a custom threshold (`?threshold`).

You can now use these relations inside other rules, just like any logic relation.

---

## 4. Proximity Types and Domains (Kinds & Domains)

From the synonyms RFC:

- `Domain`:
  - `"lexicon"` (word dictionary).
  - `"chem"` (chemistry), `"physics"`, `"behavior"`, ...
- `Kind` (proximity type):
  - `"syn"` (linguistic synonyms).
  - `"alias"` (different names for the same thing).
  - `"approx_eq"` (numerical/unit proximity).
  - `"pattern"` (pattern similarity), etc.

The idea:

> **The same structure** `similar/5` and `close/3` can be used in
> linguistic lexicon, chemistry, measurement units, medicine, behavior...

### 4.1 Small Example on alias (Alternative Name)

```bayan
hybrid {
    import bayan.core.similarity as sim
    sim.load_selective(logical, ["similarity"])

    # Assume the knowledge base contains:
    # similar("car", "automobile", 0.9, "alias", "lexicon").

    alternative_name(?original, ?name) :- close(?original, ?name, "alias").
}

query alternative_name("car", ?other_name)?
```

---

## 5. Linking with Semantic Programming and Language Model

This layer works **before the language model** and serves it:

- In semantic programming:
  - `similar/5` can be used to expand search in meaning networks `meaning`.
  - Or to discover close information in `information` and `evolving_knowledge`.
- In text generation (with `ai/nlp` and `nlp_bayan`):
  - Similarity can be used to suggest alternative linguistic candidates (close words).
  - Or to raise/lower the probability of a word in the language model based on its proximity to a certain meaning.

This makes **synonym/proximity** a first-class entity in Bayan,
not just as a word list in NLP, but as part of the logical and cognitive structure
that can be queried and relied upon in all higher layers.

## 6. Practical Example: Expanding English Query with Synonyms

```bayan
hybrid {
    # Assume is_synonym/3 is available as in previous example
    loves("Ahmad", "lion").
    loves("Sarah", "leo").

    loves_animal_expanded(?person, ?close_name) :-
        loves(?person, ?original_name),
        is_synonym(?original_name, ?close_name, ?degree),
        ?degree >= 0.6.
}

query loves_animal_expanded(?person, ?name)?
```

- `loves/2` defines original facts with certain names (like `"lion"`).
- `loves_animal_expanded/2` uses `is_synonym/3` to return **all close names** with sufficient degree,
  so `"leo"` or `"panthera"` can appear even if you didn't write them in facts directly.

