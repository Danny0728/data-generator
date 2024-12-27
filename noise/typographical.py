import json
import ollama
from config import MODEL

def make_typographical_prompt():
    system_prompt = (
        "You are an AI assistant tasked with generating examples of typographical noise. "
        "Typographical noise involves text errors caused by human or system mistakes, including typos, misspellings, "
        "and unintended input sequences.\n"
        "Guidelines:\n"
        "1. Create examples of text with intentional misspellings, typos, or repeated characters (e.g., 'heloo', 'innput').\n"
        "2. Avoid forming meaningful sentences; the text should appear noisy and incorrect.\n\n"
        "Example:\n"
        '{"context": "A rushed email draft", "text": "Plase snd the documnt as sooon as psbl!!"}'
    )
    user_prompt = (
        "Generate a single JSON object with:\n"
        "1. 'context': A brief scenario where typographical noise occurs.\n"
        "2. 'text': An example of typographical noise reflecting the scenario.\n"
        "3. 'label': The parent label is 'noise', and the sub-label is 'typographical'."
    )

    return f"<|begin_of_text|>{system_prompt}<|eot_id|>{user_prompt}<|eot_id|>"

def generate():
    prompt = make_typographical_prompt()
    result = ollama.generate(model=MODEL, prompt=prompt)
    response_str = result.get('response', '').strip()
    try:
        data = json.loads(response_str)
        data["label"] = {"parent": "noise", "sub_label": "typographical"}
        return data
    except json.JSONDecodeError:
        return {}
