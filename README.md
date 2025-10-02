# AI Text Summarizer App

## Overview
This project is a **tiny AI-powered text summarizer app** that summarizes long articles or text into **concise 2–3 sentence summaries**. It demonstrates motivation, problem-solving skills, and creativity by combining Python programming, AI models, and a simple interactive UI.

You can use it in two ways:
1. **Terminal-based script** (`summarizer.py`) – paste text in terminal and get a summary.
2. **Interactive Streamlit web app** (`app.py`) – paste text in a clean UI and generate summaries with a single click.

---

## Features

### Terminal Version (`summarizer.py`)
- Summarizes pasted text in the terminal.
- Cleans up unwanted headers, ads, and repeated lines automatically.
- Uses **Hugging Face transformers** with the **BART summarization model**.

### Streamlit Web App (`app.py`)
- Interactive web interface for a better user experience.
- Input text area with **character & word count**.
- **Sidebar sliders** to adjust summary max/min length.
- “Summarize” and “Clear” buttons for easy usage.
- Styled summary output using Streamlit’s `st.success()` box.
- Page title and emojis (Unicode) for visual appeal.

---

## Installation & Setup

### 1. Clone the repository
```bash
git clone https://github.com/pranjallll/text_summarizer_app.git
cd text_summarizer_app
```

### 2. Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```
### 3. Install dependencies
```bash
pip install --upgrade pip
pip install transformers torch streamlit
```
### 4. Run the app
## Terminal version
```bash
python3 summarizer.py
Paste your article text → press Enter twice → get a concise summary.
```
## Streamlit version
```bash
streamlit run app.py
```
Your browser opens a web app. Paste text → click Summarize → view output.

### Project Journey & Learning
- Documentation: Every step was documented, including troubleshooting Git, virtual environments, and terminal issues.
- Research & Problem-Solving: Googled solutions for pip/python path issues on Mac, model download warnings, and Streamlit UI enhancements.
- Extra Touches: Added:
Character & word count display
Sidebar sliders for summary length customization
Clear button to reset input
Automatic text cleaning to handle noisy article content
- Version Control: Used Git and GitHub, including .gitignore to exclude venv/.
- Resourcefulness: Leveraged Hugging Face models for summarization without pretraining, Streamlit for interactive UI, and caching for performance improvement.

### Challenges & Solutions
1. File & Git issues: Initially, project files like README.md and summarizer.py were misplaced, causing Git errors.
Solution: Learned to locate, move files correctly, initialize Git, and push to the repository.
2. Python & pip setup on Mac: Encountered python/pip not found errors and virtual environment issues.
Solution: Googled solutions and used python3 -m venv to create a working virtual environment.
3. Terminal hangs & script freezing: Running the summarizer script sometimes caused the terminal to lag.
Solution: Shifted to Streamlit UI, which allowed safe input handling and improved user experience.
4. Streamlit rendering issues: Emojis didn’t display properly in the web app.
Solution: Used Unicode emojis to ensure compatibility across Mac and browser setups.
💡 Support tools: For each problem, I used Google searches to find solutions, and ChatGPT to troubleshoot Python, Git, Streamlit, and model-related issues efficiently.

 

