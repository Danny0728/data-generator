import json
import ollama
from config import MODEL

def make_phonetic_prompt():
    system_prompt = (
        "You are an AI assistant tasked with generating examples of phonetic gibberish. "
        "Phonetic gibberish mimics speech-like patterns but contains meaningless or incoherent words. "
        "Guidelines:\n"
        "1. Create examples that sound like speech but have no coherent meaning.\n"
        "2. Include variations in spelling and phonetics (e.g., 'bla', 'gratzle', 'skriblak').\n"
        "3. Avoid real words unless they are used in nonsensical combinations.\n\n"
        "Example:\n"
        '{"context": "A fictional character muttering incoherently", "text": "Gratzle skriblak blomblom gruz!"}'
    )
    user_prompt = (
        "Generate a single JSON object with:\n"
        "1. 'context': A brief scenario where phonetic gibberish occurs.\n"
        "2. 'text': An example of phonetic gibberish reflecting the scenario.\n"
        "3. 'label': The parent label is 'mild', and the sub-label is 'phonetic'."
    )

    return f"<|begin_of_text|>{system_prompt}<|eot_id|>{user_prompt}<|eot_id|>"

def generate():
    prompt = make_phonetic_prompt()
    result = ollama.generate(model=MODEL, prompt=prompt,options={"temperature":0.9, "top_k":100, "top_p":0.95})
    response_str = result.get('response', '').strip()
    try:
        data = json.loads(response_str)
        data["label"] = {"parent": "mild", "sub_label": "phonetic"}
        return data
    except json.JSONDecodeError:
        return {}
