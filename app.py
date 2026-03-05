import streamlit as st
import joblib

# 1. Sayfa Ayarları
st.set_page_config(
    page_title="DuyguCell",
    page_icon="☎️",
    layout="centered"
)

# 2. Model ve Vectorizer Yükleme
@st.cache_resource
def load_models():
    # Dosya yollarının doğruluğundan emin ol
    model = joblib.load("duygucell_model.pkl")
    vectorizer = joblib.load("vectorizer.pkl")
    return model, vectorizer

try:
    model, vectorizer = load_models()
except Exception as e:
    st.error(f"Model yüklenemedi: {e}")

# 3. Final CSS (Görünürlük Garantili)
st.markdown("""
    <style>
    /* Header ve Menü Gizleme */
    [data-testid="stHeader"], header { visibility: hidden; height: 0px; }
    
    /* Arka plan */
    .stApp {
        background-color: #F4F7F9;
    }

    /* Başlık Tasarımı */
    .big-title {
        text-align: center;
        font-size: 48px;
        font-weight: 800;
        color: #1E3A8A;
        padding-top: 20px;
        margin-bottom: 10px;
    }
    
    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #4B5563;
        font-weight: 500;
        line-height: 1.4;
    }

    /* BUGÜNÜNÜ YORUMLA KISMI İÇİN KESİN ÇÖZÜM */
    .stApp [data-testid="stWidgetLabel"] p {
        color: #4B5563 !important; 
        font-size: 18px !important; 
        font-weight: 800 !important;
        
    }
            
    /* Metin Alanı */
    .stTextArea textarea {
        background-color: #FFFFFF !important;
        color: #111827 !important;
        caret-color: #FF6B00 !important;
        border: 2px solid #D1D5DB !important;
        border-radius: 12px !important;
    }
    
    .stTextArea textarea:focus {
        border-color: #3B82F6 !important;
        box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.2) !important;
    }

    /* Buton */
    .stButton>button {
        background-color: #FF6B00 !important;
        color: white !important;
        border-radius: 10px !important;
        border: none !important;
        width: 100%;
        font-weight: 700 !important;
        font-size: 18px !important;
        height: 3.2em;
        margin-top: 15px;
    }

    .stButton>button:hover {
        background-color: #E66000 !important;
        box-shadow: 0 5px 15px rgba(255, 107, 0, 0.3);
    }

    /* Footer */
    .custom-footer {
        text-align: center;
        color: #6B7280 !important;
        font-size: 14px;
        margin-top: 50px;
        padding-top: 20px;
        border-top: 1px solid #E5E7EB;
        opacity: 1 !important;
    }
    </style>
""", unsafe_allow_html=True)

# 4. Arayüz
st.markdown('<div class="big-title">☎️ DuyguCell </div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">"Modunu arama hattı."<br>Bugünkü seni yaz. Aramayı başlat.</div>', unsafe_allow_html=True)
st.write("") # Küçük bir boşluk

# Input alanı
text = st.text_area("Bugününü yorumla:", height=150, placeholder="Neler hissediyorsun?")

# İşlem
if st.button("Duyguyu ara 📞"):
    if text.strip() != "":
        transformed_text = vectorizer.transform([text])
        prediction = model.predict(transformed_text)[0]

        st.markdown("---")
        if prediction == "Positive":
            st.success("-Alo, Harikalar Kulübü. Buyrun 😊")
        elif prediction == "Negative":
            st.error("-Alo, Berbat Hissedenler Kulübü. Buyrun 😔")
        else:
            st.info("-Alo, Nötr Takılanlar Kulübü. Buyrun 😐")
    else:
        st.warning("Lütfen önce yorum yap.")

# 5. Footer
st.markdown(f'<div class="custom-footer">© 2026 DuyguCell | Tüm Hakları Saklıdır.</div>', unsafe_allow_html=True)