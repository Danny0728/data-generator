import json
import ollama
from config import MODEL

def make_repetitive_prompt():
    system_prompt = (
        "You are an AI assistant tasked with generating examples of repetitive noise. "
        "Repetitive noise involves text with repeated patterns, words, or characters that create incoherent or redundant sequences. "
        "Guidelines:\n"
        "1. Generate text that contains repeated words, phrases, or characters (e.g., 'yes yes yes', 'blah blah blah','La-la-la').\n"
        "2. Ensure the repetition appears excessive and disrupts natural readability.\n"
        "3. Avoid meaningful sentences; the text should appear noisy and redundant.\n\n"
        "Example:\n"
        '{"context": "A malfunctioning chatbot response", "text": "I I I I don\'t don\'t don\'t know know know know."}'
    )
    user_prompt = (
        "Generate a single JSON object with:\n"
        "1. 'context': A brief scenario where repetitive noise occurs.\n"
        "2. 'text': An example of repetitive noise reflecting the scenario.\n"
        "3. 'label': The parent label is 'noise', and the sub-label is 'repetitive'."
    )

    return f"<|begin_of_text|>{system_prompt}<|eot_id|>{user_prompt}<|eot_id|>"

def generate():
    prompt = make_repetitive_prompt()
    result = ollama.generate(model=MODEL, prompt=prompt)
    response_str = result.get('response', '').strip()
    try:
        data = json.loads(response_str)
        data["label"] = {"parent": "noise", "sub_label": "repetitive"}
        return data
    except json.JSONDecodeError:
        return {}
