import streamlit as st
from chatbot import HiringAssistant

st.set_page_config(page_title="TalentScout Hiring Assistant", page_icon="🧠")
st.title("🧠 TalentScout Hiring Assistant Chatbot")

if 'assistant' not in st.session_state:
    st.session_state.assistant = HiringAssistant()

if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []

user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.chat_history.append(("You", user_input))
    response = st.session_state.assistant.handle_message(user_input)
    st.session_state.chat_history.append(("Bot", response))

for sender, msg in st.session_state.chat_history:
    with st.chat_message(sender):
        st.markdown(msg)

# === FILE: chatbot.py ===
import openai
from prompts import get_initial_prompt, get_question_prompt, get_fallback_prompt
from utils import extract_tech_stack, contains_exit_keywords

openai.api_key = "YOUR_OPENAI_API_KEY"  # Replace this or use secrets

class HiringAssistant:
    def __init__(self):
        self.stage = "greeting"
        self.collected_data = {}

    def handle_message(self, user_input):
        if contains_exit_keywords(user_input):
            self.stage = "ended"
            return "Thank you for your time! We’ll be in touch shortly."

        if self.stage == "greeting":
            self.stage = "collecting"
            return get_initial_prompt()

        elif self.stage == "collecting":
            return self.collect_candidate_data(user_input)

        elif self.stage == "questioning":
            return self.ask_technical_questions()

        else:
            return get_fallback_prompt()

    def collect_candidate_data(self, text):
        keys = ["name", "email", "phone", "location", "position", "experience", "tech_stack"]
        for key in keys:
            if key not in self.collected_data:
                self.collected_data[key] = text
                if key != "tech_stack":
                    return f"Please provide your {keys[keys.index(key)+1].replace('_', ' ')}"
                else:
                    self.stage = "questioning"
                    return self.ask_technical_questions()

    def ask_technical_questions(self):
        tech_list = extract_tech_stack(self.collected_data["tech_stack"])
        prompt = get_question_prompt(tech_list)
        completion = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        return completion.choices[0].message.content
