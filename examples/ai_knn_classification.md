# KNN Classification (k=3)

Simple KNN example on tiny dataset.

```bayan
include "ai/ml.bayan"

train_X = [ [0,0], [0,1], [1,0], [1,1] ]
train_y = [0, 0, 0, 1]

test_X = [ [1,1], [0,0], [0,1] ]
pred = k_nearest_neighbors_predict(train_X, train_y, test_X, k=3)

print("pred:")
print(pred)
```

