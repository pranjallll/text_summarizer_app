from transformers import pipeline
import re

def clean_text(text):
    text = re.sub(r'\n+', ' ', text)
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'(Recommended For You.*|Show Quick Read.*|©.*)', '', text, flags=re.IGNORECASE)
    return text.strip()

def summarize_text(text):
    summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
    summary = summarizer(text, max_length=100, min_length=30, do_sample=False)
    return summary[0]['summary_text']

if __name__ == "__main__":
    print("Paste your article text below (press Enter twice when done):")
    user_input = []
    while True:
        line = input()
        if line == "":
            break
        user_input.append(line)
    article = " ".join(user_input)
    article = clean_text(article)
    print("\n--- Summary ---")
    print(summarize_text(article))

