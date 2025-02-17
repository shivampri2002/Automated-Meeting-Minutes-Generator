import streamlit as st
import requests
import io
from PIL import Image
# import json


st.set_page_config(page_title="Audio & Text Summarizer", layout="wide")

# Custom CSS to improve the UI
st.markdown("""
<style>
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    .main-header {
        font-size: 2.5rem;
        color: #4A4A4A;
        margin-bottom: 1rem;
    }
    .sub-header {
        font-size: 1.8rem;
        color: #6C6C6C;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .st-emotion-cache-1v0mbdj > img {
        margin-bottom: 1rem;
    }
    .stButton>button {
        width: 100%;
    }
    .output-area {
        background-color: #f0f2f6;
        border-radius: 5px;
        padding: 1rem;
        margin-top: 1rem;
    }
</style>
""", unsafe_allow_html=True)

API_URL = "http://localhost:8000"  # Update with actual FastAPI server URL

def transcribe_audio(file):
    files = {"file": (file.name, file.getvalue(), file.type)}
    response = requests.post(f"{API_URL}/transcribe/", files=files)
    return response.json()

def summarize_text(text):
    headers = {'Content-type': 'application/json'}
    response = requests.post(f"{API_URL}/summarize/", json={"text": text}, headers=headers)
    return response.json()

def transcribe_and_summarize(file):
    files = {"file": (file.name, file.getvalue(), file.type)}
    response = requests.post(f"{API_URL}/transcribe_and_summarize/", files=files)
    return response.json()


# Header
st.markdown("<h1 class='main-header'>🎙️ Audio & Text Summarizer</h1>", unsafe_allow_html=True)
st.write("Upload an audio file or enter text to get a transcript and summary.")

# Tabs for different functionalities
tab1, tab2, tab3 = st.tabs(["Audio Transcription", "Text Summarization", "Transcribe & Summarize"])

with tab1:
    st.markdown("<h2 class='sub-header'>Upload Audio for Transcription</h2>", unsafe_allow_html=True)
    audio_file = st.file_uploader("Choose an audio file", type=["mp3", "wav"])
    
    col1, col2 = st.columns(2)
    with col1:
        if audio_file:
            st.audio(audio_file)
    with col2:
        if audio_file and st.button("Transcribe Audio", key="transcribe_btn"):
            with st.spinner("Transcribing..."):
                result = transcribe_audio(audio_file)
                st.markdown("<div class='output-area'>", unsafe_allow_html=True)
                st.subheader("Transcript:")
                st.write(result.get("transcript", "Error in transcription"))
                st.markdown("</div>", unsafe_allow_html=True)

with tab2:
    st.markdown("<h2 class='sub-header'>Enter Text for Summarization</h2>", unsafe_allow_html=True)
    text_input = st.text_area("Paste your text here", height=200)
    if text_input and st.button("Summarize Text", key="summarize_btn"):
        with st.spinner("Summarizing..."):
            result = summarize_text(text_input)
            st.markdown("<div class='output-area'>", unsafe_allow_html=True)
            st.subheader("Summary:")
            st.write(result.get("summary", "Error in summarization"))
            st.markdown("</div>", unsafe_allow_html=True)

with tab3:
    st.markdown("<h2 class='sub-header'>Transcribe and Summarize Audio</h2>", unsafe_allow_html=True)
    audio_file = st.file_uploader("Choose an audio file", type=["mp3", "wav"], key="audio_file_2")
    
    col1, col2 = st.columns(2)
    with col1:
        if audio_file:
            st.audio(audio_file)
    with col2:
        if audio_file and st.button("Transcribe & Summarize Audio", key="transcribe_summarize_btn"):
            with st.spinner("Processing..."):
                result = transcribe_and_summarize(audio_file)
                st.markdown("<div class='output-area'>", unsafe_allow_html=True)
                st.subheader("Transcript:")
                st.write(result.get("transcript", "Error in transcription"))
                st.subheader("Summary:")
                st.write(result.get("summary", "Error in summarization"))
                st.markdown("</div>", unsafe_allow_html=True)

# Additional Features
st.markdown("<h2 class='sub-header'>Additional Features</h2>", unsafe_allow_html=True)
feature_col1, feature_col2, feature_col3 = st.columns(3)
with feature_col1:
    st.markdown("### 🎵 Supported Formats")
    st.write("✔️ MP3")
    st.write("✔️ WAV")
with feature_col2:
    st.markdown("### ⚡ Performance")
    st.write("✔️ Fast transcription")
    st.write("✔️ Efficient summarization")
with feature_col3:
    st.markdown("### 🌐 Accessibility")
    st.write("✔️ User-friendly interface")
    st.write("✔️ Real-time feedback")

# Feedback Section
st.markdown("<h2 class='sub-header'>Feedback & Improvements</h2>", unsafe_allow_html=True)
feedback = st.text_area("Have suggestions? Let us know!", height=100)
if st.button("Submit Feedback", key="feedback_btn"):
    st.success("Thank you for your feedback! We appreciate your input.")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ by Shivam")

