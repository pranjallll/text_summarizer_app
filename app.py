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

import streamlit as st
from transformers import pipeline
import re

# App title and description
st.set_page_config(page_title="AI Text Summarizer", page_icon="✍️", layout="centered")

st.title("✍️ AI Text Summarizer")
st.markdown(
    """
    Welcome to **AI Text Summarizer**!  
    Paste any long article or text, and this app will generate a **clear and concise summary** 📚✨  
    """
)

# Load model
@st.cache_resource
def load_summarizer():
    return pipeline("summarization", model="facebook/bart-large-cnn")

summarizer = load_summarizer()

# User input
article = st.text_area("📝 Paste your article here:", height=200, placeholder="Copy and paste your text...")

# Action button
if st.button("✨ Summarize"):
    if article.strip():
        with st.spinner("Generating summary... 🔄"):
            clean_text = re.sub(r'\s+', ' ', article.strip())
            summary = summarizer(clean_text, max_length=120, min_length=40, do_sample=False)
        st.success("✅ Summary ready!")
        st.markdown("### 📌 Summary")
        st.write(summary[0]['summary_text'])
    else:
        st.warning("⚠️ Please paste some text first!")

# Footer
st.markdown("---")
st.markdown(
    "Built with ❤️ using [Streamlit](https://streamlit.io/) & [Transformers](https://huggingface.co/transformers/)."
)


