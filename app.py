# app.py
import os
import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv

# Load API Key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("models/gemini-1.5-flash")

# Streamlit UI config
st.set_page_config(page_title="🕌 Islamic Urdu AI Assistant")
st.title("🕌 Islamic Urdu Knowledge Assistant")
st.markdown("Ask anything about Islam, duas, rulings — in **Urdu** ✨")

# Select prompt type
prompt_type = st.selectbox("Select prompt type", [
    "Islamic Answer (Mufti)",
    "Dua List (JSON Format)",
    "Halal or Haram (Chain of Thought)",
    "Islamic Term Dictionary(FAQ)",
])

# Map prompt type to file
prompt_map = {
    "Islamic Answer (Mufti)": "prompts/mufti.txt",
    "Dua List (JSON Format)": "prompts/dua_json.txt",
    "Halal or Haram (Chain of Thought)": "prompts/cot.txt",
    "Islamic Term Dictionary": "prompts/faq.txt",
    "Self-Review (Critic Mode)": "prompts/faq.txt"  # can use same or different
}

# Load user input
user_input = st.text_area("✍️ Ask your question or give instruction in Urdu")
submit = st.button("💬 Get Answer")

# Function to load and inject prompt
def load_prompt(template_file, user_input=""):
    with open(template_file, "r", encoding="utf-8") as f:
        prompt = f.read()
    return prompt.replace("{{user_input}}", user_input)

# Show result
if submit and user_input:
    st.info("⏳ Generating answer from Gemini...")
    full_prompt = load_prompt(prompt_map[prompt_type], user_input)
    try:
        response = model.generate_content(full_prompt)
        st.success("✅ Response from AI")
        st.markdown(response.text)
    except Exception as e:
        st.error(f"❌ Error: {e}")
