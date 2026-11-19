import streamlit as st
from deep_translator import GoogleTranslator

st.set_page_config(page_title="Language Translator", page_icon="🌐", layout="centered")

st.title("🌐 Instant Language Translator")
st.write("Kisi bhi language ka text aasani se translate karen.")

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
}

col1, col2 = st.columns(2)

with col1:
    source_lang = st.selectbox("Source Language", list(LANGUAGES.keys()), index=0)

with col2:
    target_choices = [lang for lang in LANGUAGES.keys() if lang != "Auto Detect"]
    default_index = target_choices.index("Urdu") if "Urdu" in target_choices else 0
    target_lang = st.selectbox("Target Language", target_choices, index=default_index)

user_text = st.text_area("Yahan text likhein:", height=140, placeholder="Maslan: Hello, how are you?")

if st.button("Translate", type="primary", use_container_width=True):
    text = user_text.strip()
    if not text:
        st.warning("Pehle kuch text likhein.")
    else:
        try:
            with st.spinner("Translate ho raha hai..."):
                result = GoogleTranslator(
                    source=LANGUAGES[source_lang],
                    target=LANGUAGES[target_lang],
                ).translate(text)
            st.subheader("Translated Text:")
            st.success(result)
        except Exception as err:
            st.error(f"Error aaya: {err}")
