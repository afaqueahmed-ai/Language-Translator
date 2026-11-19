import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(page_title="Language Translator", page_icon="🌐", layout="centered")

st.title("🌐 Instant Language Translator")
st.caption("Google Colab + GitHub + Streamlit Cloud se deploy kiya gaya app")

LANGUAGES = {
    "Auto Detect": "auto",
    "Urdu": "ur",
    "English": "en",
    "Hindi": "hi",
    "Arabic": "ar",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Turkish": "tr",
    "Chinese (Simplified)": "zh-CN",
}

col1, col2 = st.columns(2)

with col1:
    source_name = st.selectbox("Source Language", list(LANGUAGES.keys()), index=0)

with col2:
    target_options = [lang for lang in LANGUAGES.keys() if lang != "Auto Detect"]
    default_idx = target_options.index("Urdu") if "Urdu" in target_options else 0
    target_name = st.selectbox("Target Language", target_options, index=default_idx)

text_to_translate = st.text_area(
    "Yahan text likhein:",
    height=150,
    placeholder="Maslan: Hello, how are you doing today?",
)

if st.button("Translate Karein", type="primary", use_container_width=True):
    cleaned_text = text_to_translate.strip()
    if not cleaned_text:
        st.warning("Pehle kuch text likhein.")
    else:
        try:
            with st.spinner("Translate ho raha hai..."):
                translated_text = GoogleTranslator(
                    source=LANGUAGES[source_name],
                    target=LANGUAGES[target_name],
                ).translate(cleaned_text)

            st.subheader("Translated Output:")
            st.success(translated_text)
            st.code(translated_text, language=None)
        except Exception as e:
            st.error(f"Translation mein masla aaya: {e}")
