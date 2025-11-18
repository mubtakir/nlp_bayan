# Approximate Equality Examples (~= / ≈)

```bayan
hybrid {
  x = 3.14
  y = 22 / 7
  ok_num = x ~= y
  ok_char = 3.0 ≈ 3.0000001

  import bayan.core.similarity as sim
  sim.load_selective(logical, ["similarity"])  # loads close/3 (Kind="syn")
  ok_syn = "أسد" ~= "غضنفر"
  bad_syn = "أسد" ~= "هيضم"
}
```

