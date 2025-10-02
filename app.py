import streamlit as st
from transformers import pipeline
import re

# Function to clean the article text
def clean_text(text):
    text = re.sub(r'\n+', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'(Recommended For You.*|Show Quick Read.*|©.*)', '', text, flags=re.IGNORECASE)
    return text.strip()

# Load the summarization model
@st.cache_resource
def load_model():
    return pipeline("summarization", model="facebook/bart-large-cnn")

summarizer = load_model()

# Streamlit UI
st.title("AI Text Summarizer")
st.write("Paste your article text below and get a concise summary:")

user_input = st.text_area("Enter text here", height=300)

if st.button("Summarize"):
    if user_input.strip() == "":
        st.warning("Please enter some text first!")
    else:
        cleaned_text = clean_text(user_input)
        summary = summarizer(cleaned_text, max_length=100, min_length=30, do_sample=False)
        st.subheader("Summary")
        st.write(summary[0]['summary_text'])

