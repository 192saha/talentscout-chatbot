from openai import OpenAI
from prompts import get_initial_prompt, get_question_prompt, get_fallback_prompt
from utils import extract_tech_stack, contains_exit_keywords
import streamlit as st

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

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
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
