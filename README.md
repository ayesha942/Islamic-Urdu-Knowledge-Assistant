# 🕌 Islamic Urdu AI Assistant

This is a GenAI-based Urdu chatbot built using **Streamlit** and **Gemini 1.5 Flash**. It is designed to answer Islamic questions in natural Urdu, provide duas in JSON format, analyze halal/haram topics through step-by-step reasoning, define Islamic terms, and even critique answers using prompt engineering.

---

## 🌟 Features

- 🤖 Gemini 1.5 Flash as the AI backend
- ✍️ Ask anything in Urdu (Fatwa-style)
- 🤲 Generate JSON-formatted Duas
- ⚖️ Halal vs Haram explanations with chain-of-thought logic
- 📘 Dictionary mode for Islamic terms
- 🧠 Critic mode to review or critique answers

---

## 🛠️ Technologies Used

- **Python 3.10+**
- **Streamlit** for frontend UI
- **Google Generative AI** (`gemini-1.5-flash`)
- **python-dotenv** to manage API keys
- **Prompt Engineering** (Custom `.txt` templates)

---

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/islamic-urdu-ai.git
cd islamic-urdu-ai
```

### 2. Install Requirements

```bash
pip install streamlit python-dotenv google-generativeai
```

### 3. Setup API Key

Create a `.env` file in the root folder and add your Gemini API key:

```
GEMINI_API_KEY=your_google_genai_api_key
```

### 4. Run the App

```bash
streamlit run app.py
```

---

## 🔍 Prompt Modes (Templates)

| Mode                | Prompt File      | What It Does                            |
|---------------------|------------------|------------------------------------------|
| Islamic Answer       | `mufti.txt`       | Gives fatwa-like Urdu answers             |
| Dua JSON Generator   | `dua_json.txt`    | Outputs duas in structured JSON format    |
| Halal or Haram       | `cot.txt`         | Uses reasoning steps (chain-of-thought)   |
| Islamic Dictionary   | `faq.txt`         | Explains terms like zakat, sawm, etc.     |

---

## 💬 Example Inputs

- `کیا کرپٹو کرنسی حلال ہے؟` *(Is crypto halal? — Mufti mode)*
- `Give me 3 duas for health in JSON format` *(Dua JSON mode)*
- `فوٹو لینا حلال ہے یا حرام؟ وجہ کے ساتھ بتائیں` *(Halal/Haram CoT mode)*
- `روزہ کیا ہے؟` *(FAQ mode — dictionary style)*


---

## 📌 Notes

- This is an experimental learning project for **Prompt Engineering + GenAI tools in Urdu**.
- It is **not intended for issuing real fatwas** — always consult real scholars for religious decisions.

