# تصنيف متعدد الفئات بـ Softmax (عربي)

```bayan
include "ai/ml.bayan"

# بيانات لعب بسيطة: 3 فئات
X = [ [1,0], [0,1], [1,1], [2,0], [0,2], [2,1] ]
y = [0, 1, 2, 0, 1, 2]

نموذج = تدريب_Softmax(X, y, lr=0.2, epochs=200)

pred = توقع_Softmax(X, نموذج)
print("pred:")
print(pred)
```
