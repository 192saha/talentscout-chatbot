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

