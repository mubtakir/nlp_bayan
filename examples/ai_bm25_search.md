# BM25 Search (Top-k)

Build a tiny BM25 index and query it.

```bayan
include "ai/nlp.bayan"

docs = [
  "the cat sat on the mat",
  "the dog sat on the log",
  "cats and dogs are friends"
]

model = bm25_build(docs, k1=1.5, b=0.75)
results = bm25_top_k(model, "cat on mat", k=3)

print("[index, score] top-3:")
print(results)
```

