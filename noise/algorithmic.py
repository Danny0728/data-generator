import json
import ollama
from config import MODEL

def make_algorithmic_prompt():
    system_prompt = (
        "You are an AI assistant tasked with generating examples of algorithmic noise. "
        "Algorithmic noise involves text generated by algorithms that creates random, meaningless, or machine-like patterns. "
        "Guidelines:\n"
        "1. Create examples that include random symbols, numbers, or characters that mimic machine output (e.g., 'xz@#$12AB', '00110011').\n"
        "2. Ensure the text appears artificially generated rather than human-like.\n"
        "3. Avoid forming meaningful sequences; the text should appear completely random and nonsensical.\n\n"
        "Example:\n"
        '{"context": "Corrupted data output from a system log", "text": "xz1@#$12AB000101010!!"}'
    )
    user_prompt = (
        "Generate a single JSON object with:\n"
        "1. 'context': A brief scenario where algorithmic noise occurs.\n"
        "2. 'text': An example of algorithmic noise reflecting the scenario.\n"
        "3. 'label': The parent label is 'noise', and the sub-label is 'algorithmic'."
    )

    return f"<|begin_of_text|>{system_prompt}<|eot_id|>{user_prompt}<|eot_id|>"

def generate():
    prompt = make_algorithmic_prompt()
    result = ollama.generate(model=MODEL, prompt=prompt)
    response_str = result.get('response', '').strip()
    try:
        data = json.loads(response_str)
        data["label"] = {"parent": "noise", "sub_label": "algorithmic"}
        return data
    except json.JSONDecodeError:
        return {}
