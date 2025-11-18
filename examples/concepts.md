# Concepts and Membership (concept / \u0645\u0641\u0647\u0648\u0645)

```bayan
hybrid {
  concept Animal = {"\u0623\u0633\u062f","\u0646\u0645\u0631","\u0641\u0647\u062f"}
  ok1 = "\u0623\u0633\u062f" in Animal
  ok2 = "\u0642\u0637" \u2208 Animal
  # Logical facts asserted: in_concept("Animal", X)
  query in_concept("Animal", ?X).
}
```

