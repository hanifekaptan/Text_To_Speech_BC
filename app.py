from gtts import gTTS
from gtts import lang
import streamlit as st
import pandas as pd

# Load language data from CSV file
data = lang.tts_langs()

st.title("Text to Speech")
text = st.text_area("Enter your text", placeholder="Enter your text here")

# Create a dropdown menu for language selection
language = st.selectbox("Select Language", data.values())

# Create a dropdown menu for speed selection
speed = st.selectbox("Select Language", ["Fast", "Slow"])

if st.button("Convert"):
    try:
        # Determine if the speech should be slow
        is_slow = False if speed == "Fast" else True

        # Get the selected language code
        lang = [key for key, value in data.items() if value == language][0]

        # Create a gTTS object with the provided text and language
        tts = gTTS(text = text, lang = lang, slow = is_slow)
    
    except Exception as e:
        st.error("Could not be converted" + str(e))

    try:
        tts.save("output.mp3")
        # Provide a download button for the user to download the MP3 file
        with open("output.mp3", "rb") as f:
            download = st.download_button("Download", data=f, file_name="output.mp3", mime="audio/mpeg")
    
    except Exception as e:
        st.error("Download could not be completed"+ str(e))
