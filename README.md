# 📚 Text to Math Problem Solver & Wiki Assistant

This Streamlit web app uses **LangChain + Groq + Wikipedia** to solve logical and mathematical questions from natural language input and provide real-time information using Wikipedia.

---

## 🚀 Features

- ✍️ **Natural Language Math Solver** — Converts text-based math problems into solutions with reasoning.
- 📖 **Wikipedia Search Integration** — Pulls summarized info from Wikipedia using LangChain.
- 🤖 **Powered by Google Gemma via Groq** — Fast, low-latency LLM experience.

---

## 🧠 How It Works

1. Accepts a question from the user in plain English.
2. Uses LangChain tools:
   - `LLMMathChain` for math computation
   - `WikipediaAPIWrapper` for fetching data
3. Uses Groq’s **Gemma-2-9B-IT** model to respond intelligently.
4. Displays the step-by-step solution or wiki summary.

---

## 🔧 How to Run This App Locally

### 1. Clone this Repository
```bash
git clone https://github.com/juhi-shahi/streamlit-wiki-app.git
cd streamlit-wiki-app



