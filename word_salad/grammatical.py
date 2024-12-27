import json
import ollama
from config import MODEL

def make_grammatical_prompt():
    system_prompt = (
        "You are an AI assistant tasked with generating examples of grammatical word salad. "
        "Grammatical word salad involves text that uses correct grammar but is semantically nonsensical. "
        "Guidelines:\n"
        "1. Create examples of grammatically correct sentences that make no logical or meaningful sense.\n"
        "2. Use a variety of sentence structures while ensuring the content remains nonsensical.\n"
        "3. Avoid forming coherent ideas; focus on logical absurdities.\n\n"
        "Example:\n"
        '{"context": "A chatbot trying to answer a philosophical question", "text": "The yellow dreams of laughter beneath the silent clock."}'
    )
    user_prompt = (
        "Generate a single JSON object with:\n"
        "1. 'context': A brief scenario where grammatical word salad occurs.\n"
        "2. 'text': An example of grammatical word salad reflecting the scenario.\n"
        "3. 'label': The parent label is 'word salad', and the sub-label is 'grammatical'."
    )

    return f"<|begin_of_text|>{system_prompt}<|eot_id|>{user_prompt}<|eot_id|>"

def generate():
    prompt = make_grammatical_prompt()
    result = ollama.generate(model=MODEL, prompt=prompt)
    response_str = result.get('response', '').strip()
    try:
        data = json.loads(response_str)
        data["label"] = {"parent": "word salad", "sub_label": "grammatical"}
        return data
    except json.JSONDecodeError:
        return {}
