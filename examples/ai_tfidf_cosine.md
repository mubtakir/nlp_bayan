# TF-IDF Cosine Similarity

Compare two texts using TF-IDF (log + L2 norm) and cosine similarity.

```bayan
include "ai/nlp.bayan"

text1 = "machine learning with simple examples"
text2 = "simple examples for learning machines"

sim = tfidf_cosine_similarity(text1, text2)
print(sim)
```

