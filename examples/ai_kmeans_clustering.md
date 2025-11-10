# K-Means Clustering (k=2)

Run k-means++ on two clusters in 2D.

```bayan
include "ai/ml.bayan"

data = [ [0,0],[0,1],[1,0],[1,1], [8,8],[9,8],[8,9],[9,9] ]
model = k_means_pp(data, 2, max_iters=10)

centers = model[0]
labels = model[1]

print("centers:")
print(centers)
print("labels:")
print(labels)
```

