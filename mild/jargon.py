import json
import ollama
from config import MODEL 

def make_jargon_prompt():
    system_prompt = (
        "You are an AI assistant tasked with generating examples of jargon gibberish. "
        "Jargon gibberish uses technical or formal-sounding words in nonsensical combinations. "
        "Guidelines:\n"
        "1. Create examples of technical-sounding but incoherent statements.\n"
        "2. Include plausible terminology from science, business, or technology.\n"
        "3. Avoid making sense, but ensure the syntax resembles real-world jargon.\n\n"
        "Example:\n"
        '{"context": "A marketing consultant overcomplicating a simple idea", "text": "The synaptic leverage of our paradigm shift enhances the ROI schema throughput."}'
    )
    user_prompt = (
        "Generate a single JSON object with:\n"
        "1. 'context': A brief scenario where jargon gibberish occurs.\n"
        "2. 'text': An example of jargon gibberish reflecting the scenario.\n"
        "3. 'label': The parent label is 'mild', and the sub-label is 'jargon'."
    )

    return f"<|begin_of_text|>{system_prompt}<|eot_id|>{user_prompt}<|eot_id|>"

def generate():
    prompt = make_jargon_prompt()
    result = ollama.generate(model=MODEL, prompt=prompt)
    response_str = result.get('response', '').strip()
    try:
        data = json.loads(response_str)
        data["label"] = {"parent": "mild", "sub_label": "jargon"}
        return data
    except json.JSONDecodeError:
        return {}
