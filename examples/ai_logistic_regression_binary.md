# Logistic Regression (Binary) — AND gate

This example trains a simple binary logistic regression on the AND dataset.

```bayan
include "ai/ml.bayan"

X = [ [0.0,0.0], [1.0,0.0], [0.0,1.0], [1.0,1.0] ]
y = [0, 0, 0, 1]

wb = logistic_regression_train(X, y, lr=0.5, epochs=400, l2=0.0)
#w = wb[0]; b = wb[1]
pred = logistic_regression_predict(X, wb[0], wb[1], threshold=0.5)

print("pred:")
print(pred)
print("acc:")
print(accuracy_score(y, pred))
```

