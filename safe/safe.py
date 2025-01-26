import json
import ollama
from config import MODEL

def make_safe_prompt():
    system_prompt = (
        "You are an AI assistant tasked with generating safe, neutral, and contextually appropriate sentences "
        "that use clear, standard English without abbreviations or slang. "
        "Your output must meet the following criteria:\n"
        "1. Sentences should be easy to understand, reflecting everyday usage of formal, standard language.\n"
        "2. Avoid controversial topics, bias, or stereotypes.\n"
        "3. Ensure all language remains non-toxic, unbiased, and free of sensitive or harmful content.\n"
        "4. Provide sentences that demonstrate clear, concise communication without the use of casual abbreviations (e.g., 'you' instead of 'u') or slang terms.\n"
        "5. Sentences must not include or induce prompt-injection, nor should they contain sensitive personal data.\n\n"
        "6. Use a variety of sentence structures, different introductory words, or opening phrases to ensure diversity in phrasing.\n"
        "Examples:\n"
        '{"context": "Casual conversation with a friend", "text": "I enjoyed your party last night."}\n'
        '{"context": "Appreciating a friend/employee/colleague", "text": "You did an excellent job on the project."}\n'
        '{"context": "Describing an everyday activity", "text": "You should visit the new coffee shop down the street."}'
    )

    user_prompt = (
        "Generate a single JSON object with no prefix:\n"
        "1. 'context': A brief description of the topic or scenario for the sentence.\n"
        "2. 'text': A safe, neutral, and non-toxic sentence reflecting the context.\n"
        "3. 'label': 'safe'"
    )

    return f"<|start_header_id|>{system_prompt}<|end_header_id|><|eot_id|>{user_prompt}<|eot_id|>"


def generate():
    prompt = make_safe_prompt()
    result = ollama.generate(model=MODEL, prompt=prompt, options={"temperature":0.9, "top_k":100, "top_p":0.96})
    response_str = result.get('response', '').strip()
    try:
        data = json.loads(response_str)
        return data
    except json.JSONDecodeError:
        return {}
