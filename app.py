import streamlit as st
from deep_translator import GoogleTranslator, MyMemoryTranslator

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

def translate_with_fallback(text, src, tgt):
    try:
        return GoogleTranslator(source=src, target=tgt).translate(text), "Google Translate"
    except Exception:
        mm_src = "en-US" if src in ("auto", "en") else src
        mm_tgt = tgt
        translated = MyMemoryTranslator(source=mm_src, target=mm_tgt).translate(text)
        return translated, "MyMemory (Backup)"

if st.button("Translate", type="primary", use_container_width=True):
    text = user_text.strip()
    if not text:
        st.warning("Pehle kuch text likhein.")
    else:
        try:
            with st.spinner("Translate ho raha hai..."):
                result, engine = translate_with_fallback(
                    text,
                    LANGUAGES[source_lang],
                    LANGUAGES[target_lang],
                )
            st.subheader("Translated Text:")
            st.success(result)
            st.caption(f"Engine used: {engine}")
        except Exception as err:
            st.error(f"Abhi server busy hai, thori der baad try karen: {err}")
