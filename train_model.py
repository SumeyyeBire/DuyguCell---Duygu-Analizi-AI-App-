import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# Dataseti oku
df = pd.read_csv("train.csv")

X = df["text"]
y = df["label"]

# Veriyi böl
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 🔥 GELİŞTİRİLMİŞ VECTORIZER
vectorizer = TfidfVectorizer(
    max_features=20000,
    ngram_range=(1,2)
)

X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec = vectorizer.transform(X_test)

# Model
model = LogisticRegression(max_iter=1000)
model.fit(X_train_vec, y_train)

accuracy = model.score(X_test_vec, y_test)
print("Yeni Model Doğruluk Oranı:", accuracy)

# Modeli kaydet
joblib.dump(model, "duygucell_model.pkl")
joblib.dump(vectorizer, "vectorizer.pkl")

print("Model güncellendi ve kaydedildi ✅")