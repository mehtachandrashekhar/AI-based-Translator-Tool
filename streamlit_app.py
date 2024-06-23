import streamlit as st
from app.model import translate

# Streamlit app title
st.title("AI-based English to Hindi Translator")

# Text input
input_text = st.text_area("Enter text in English:", "")

# Button to trigger translation
if st.button("Translate"):
    if input_text:
        # Perform translation
        translated_text = translate(input_text)
        
        # Display the translated text
        st.write("Translated text in Hindi:")
        st.write(translated_text)
    else:
        st.write("Please enter text to translate.")
