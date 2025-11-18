# Probabilistic Facts (fact[0.8] p(args).)

```bayan
hybrid {
  fact[0.9] parent("john", "mary").
  fact[0.6] parent("john", "alex").
}
```

Notes:
- Probability is stored with the fact in the logical engine for downstream use.
- Default probability is 1.0 when `fact[...]` is not used.

