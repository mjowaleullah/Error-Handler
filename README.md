# 🐛 Error Debugger — AI-Powered Bug Explainer

An intelligent error debugging assistant built with **Streamlit** and **Google Gemini**. Upload a screenshot of your error, choose how you want help, and get an instant AI-generated explanation and solution.

---

## Overview

Error Debugger uses Google Gemini's vision capabilities to analyze error screenshots and provide either helpful hints or complete code-based solutions — making debugging faster and more intuitive.

---

## Features

- 📸 **Screenshot-based error analysis** — Upload any error screenshot (JPEG, JPG, PNG)
- 🔍 **Two solution modes:**
  - **Hints** — Guided clues to help you solve it yourself
  - **Solution with Code** — Complete fix with working code
- ⚡ **Powered by Google Gemini** — Fast, accurate vision-language understanding
- 🖥️ **Clean Streamlit UI** — Simple sidebar controls with instant results

---

## Tech Stack

| Tool | Purpose |
|------|---------|
| [Streamlit](https://streamlit.io) | Web UI |
| [Google Gemini](https://ai.google.dev) | Vision + Language Model |
| [Pillow (PIL)](https://pillow.readthedocs.io) | Image processing |
| Python 3.10+ | Core language |

---

## Project Structure

```
.
├── app.py               # Main Streamlit UI
├── api_calling.py       # Gemini API logic (bug_explatation, debug)
├── .env                 # API keys (never commit this)
├── .env.example         # Template for environment variables
├── requirements.txt     # Python dependencies
└── README.md
```

---

## Setup & Installation

**1. Clone the repository**
```bash
git clone https://github.com/your-username/error-debugger.git
cd error-debugger
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Set up environment variables**

Create a `.env` file based on `.env.example`:
```env
GOOGLE_API_KEY=your_google_gemini_api_key
OPENAI_MODEL_NAME=gemini-2.0-flash-preview
```

**4. Run the app**
```bash
streamlit run app.py
```

---

## Usage

1. Open the app in your browser
2. Upload an error screenshot from the **sidebar**
3. Select your preferred solution type — **Hints** or **Solution with Code**
4. Click **Submit and initiate with AI**
5. View the issue explanation and solution

---

## Environment Variables

| Variable | Description |
|----------|-------------|
| `GOOGLE_API_KEY` | Your Google Gemini API key |
| `OPENAI_MODEL_NAME` | Gemini model name (e.g. `gemini-2.0-flash-preview`) |

> ⚠️ Never commit your `.env` file. It is listed in `.gitignore`.

---

## Requirements

```
streamlit
google-generativeai
pillow
python-dotenv
```

---

## License

MIT License — feel free to use, modify, and distribute.
