# Gerekli kütüphaneleri içe aktar
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
import pandas as pd

# 1. Yapay veri oluştur (2 özellik, 2 sınıf)
X, y = make_classification(n_samples=100, n_features=2, n_classes=2, n_redundant=0, random_state=42)

# 2. Veriyi eğitim ve test olarak ayır
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# 3. Model oluştur ve eğit
model = DecisionTreeClassifier()
model.fit(X_train, y_train)

# 4. Test verisiyle tahmin yap
y_pred = model.predict(X_test)

# 5. Başarı oranını yazdır
print("Doğruluk oranı:", accuracy_score(y_test, y_pred))

# 6. Veriyi görselleştir
plt.scatter(X_test[:, 0], X_test[:, 1], c=y_pred, cmap='coolwarm', marker='o')
plt.title("Tahmin Sonuçları")
plt.xlabel("Özellik 1")
plt.ylabel("Özellik 2")
plt.show()
