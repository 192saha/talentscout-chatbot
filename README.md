# TalentScout Hiring Assistant 🤖

## Overview
A smart AI-powered chatbot for screening tech candidates based on their tech stack and experience.

## Features
- Collects essential candidate info
- Generates technical questions based on tech stack
- Uses GPT-4 for dynamic prompt handling
- Built with Streamlit and OpenAI

## Setup
```bash
git clone https://github.com/yourname/talentscout-chatbot.git
cd talentscout-chatbot
pip install -r requirements.txt
streamlit run app.py
```

## Deployment (Streamlit Cloud)
1. Push this project to a public GitHub repo
2. Go to https://streamlit.io/cloud and click **"New app"**
3. Connect your GitHub and select this repo
4. Set `app.py` as the main file
5. In *Secrets*, add:
```
OPENAI_API_KEY="your-openai-key"
```
6. Deploy 🚀
