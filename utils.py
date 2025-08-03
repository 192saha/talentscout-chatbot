def extract_tech_stack(text):
    # Simple split, could be enhanced with NER or LLM call
    return [tech.strip() for tech in text.split(",")]

def contains_exit_keywords(text):
    keywords = ["exit", "quit", "bye", "goodbye"]
    return any(word in text.lower() for word in keywords)
