import joblib

# Model ve vectorizer'ı yükle
model = joblib.load("duygucell_model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

print("DuyguCell Başlatıldı 😎")
print("Çıkmak için q yaz.\n")

while True:
    text = input("Bir cümle yaz: ")

    if text.lower() == "q":
        print("DuyguCell kapanıyor...")
        break

    text_vec = vectorizer.transform([text])
    prediction = model.predict(text_vec)

    print("Tahmin edilen duygu:", prediction[0])
    print("-" * 40)