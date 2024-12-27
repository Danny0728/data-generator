import json
import ollama
from config import MODEL

def make_word_salad_prompt():
    system_prompt = (
        "You are an AI assistant tasked with generating examples of word salad. "
        "Word salad involves a random, meaningless arrangement of words that do not form coherent sentences. "
        "Guidelines:\n"
        "1. Create examples where random words are strung together without any logical or grammatical connection.\n"
        "2. Avoid forming meaningful phrases or sentences; the text should appear incoherent and nonsensical.\n"
        "3. Include a variety of random words from different categories (e.g., nouns, verbs, adjectives).\n\n"
        "Example:\n"
        '{"context": "An overheard conversation in a chaotic market", "text": "Apple run quickly table blue sky jumping backwards."}'
    )
    user_prompt = (
        "Generate a single JSON object with:\n"
        "1. 'context': A brief scenario where word salad occurs.\n"
        "2. 'text': An example of word salad reflecting the scenario.\n"
        "3. 'label': The parent label is 'word salad', and the sub-label is 'word salad'."
    )

    return f"<|begin_of_text|>{system_prompt}<|eot_id|>{user_prompt}<|eot_id|>"

def generate():
    prompt = make_word_salad_prompt()
    result = ollama.generate(model=MODEL, prompt=prompt)
    response_str = result.get('response', '').strip()
    try:
        data = json.loads(response_str)
        data["label"] = {"parent": "word salad", "sub_label": "word salad"}
        return data
    except json.JSONDecodeError:
        return {}
