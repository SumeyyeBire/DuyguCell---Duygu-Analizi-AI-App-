\# DuyguCell – Türkçe Duygu Analizi AI Uygulaması



DuyguCell, kullanıcıların yazdığı metinleri analiz ederek metnin duygu durumunu tahmin eden bir yapay zeka uygulamasıdır.



Uygulama metinleri \*\*Pozitif, Negatif veya Nötr\*\* olarak sınıflandırır. Ancak bu sınıflandırmayı, "Duygularınızı arayın. Ait olduğunuz topluluktan size dönüş yapılsın." Mantığında yaparak UX iyileştirmesi sağlanarak daha eğlenceli hale getirildi. 



\## Canlı Uygulama



Uygulamayı buradan deneyebilirsiniz:



https://duygucell.streamlit.app/



\## Özellikler



\- Türkçe metinler için duygu analizi

\- Pozitif / Negatif / Nötr sınıflandırma

\- Makine öğrenmesi modeli

\- Streamlit ile oluşturulmuş web arayüzü

\- Gerçek zamanlı tahmin



\## Kullanılan Teknolojiler



\- Python

\- Scikit-learn

\- Pandas

\- Streamlit

\- TF-IDF Vectorizer

\- Joblib



\## Nasıl Çalışır



1\. Kullanıcı bir metin girer

2\. Metin TF-IDF yöntemi ile sayısal formata çevrilir

3\. Eğitilmiş makine öğrenmesi modeli tahmin yapar

4\. Sonuç kullanıcıya gösterilir



\## Proje Yapısı



DuyguCell

│

├── streamlit\_app.py

├── train\_model.py

├── duygucell\_model.pkl

├── vectorizer.pkl

├── requirements.txt

└── README.md





\## Örnek Kullanım



Örnek metinler:



\- "Bugün çok mutluyum"

\- "Bugün moralim çok bozuk"

\- "Bugün normal bir gündü"



\## Geliştirici



Sümeyye Bire  

Bilgisayar Mühendisliği Öğrencisi



Bu proje makine öğrenmesi ve doğal dil işleme alanında pratik yapmak amacıyla geliştirilmiştir.

