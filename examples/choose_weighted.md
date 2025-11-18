# Weighted Choice — الاختيار الموزون

Domain: logic

```bayan
hybrid {
  # Always choose the highest weight if others are 0
  best = choose { "A":0.0, "B":1.0, "C":0.0 }
  print(best)
}
```

