def get_initial_prompt():
    return "Hello! I'm your AI Hiring Assistant 🤖. I’ll help with your initial screening. Let's start. Please provide your full name."

def get_question_prompt(tech_list):
    tech_string = ", ".join(tech_list)
    return (
        f"You are a technical interviewer. A candidate listed the following tech stack: {tech_string}.\n"
        f"Generate 3-5 relevant technical questions to assess their skill level in these technologies."
    )

def get_fallback_prompt():
    return "Sorry, I didn’t understand that. Could you please clarify or continue with the requested information?"

# === FILE: utils.py ===
def extract_tech_stack(text):
    # Simple split, could be enhanced with NER or LLM call
    return [tech.strip() for tech in text.split(",")]

def contains_exit_keywords(text):
    keywords = ["exit", "quit", "bye", "goodbye"]
    return any(word in text.lower() for word in keywords)
