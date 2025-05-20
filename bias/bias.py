import ollama
import json
from config import MODEL

def make_bias_prompt():
    system_prompt = (
        "You are an AI assistant tasked with generating labeled example of biased content across various contexts. "
        "The example should cover one of the following types of bias: Halo Effect, Stereotypes, Racial Bias, Gender Bias, Recency Bias, or Egocentric Bias. "
        "The dataset must be balanced, with an equal number of example for each bias type, ensuring diversity across contexts and language styles."
        "Do not generate more than one example. The output must be a single JSON object, not a list or multiple objects."
        "Guidelines:\n"
        "1. Provide realistic scenarios for each type of bias, such as:\n"
        "   - Workplace: Hiring decisions, performance reviews, promotions.\n"
        "   - Education: Teacher-student interactions, grading.\n"
        "   - Media: Advertisements, news coverage, social media.\n"
        "   - Everyday Interactions: Conversations, judgments, stereotypes in casual settings.\n"
        "2. Ensure language diversity by including:\n"
        "   - Abbreviations (e.g., ur, pls, u r).\n"
        "   - Contractions (e.g., you're, can't).\n"
        "   - Slang (e.g., da best, chillin').\n"
        "   - Informal spellings (e.g., plz, ppl).\n"
        "   Incorporate these variations naturally, but balance them with formal language to reflect real-world use.\n"
        "3. Example may include offensive or harmful language only when absolutely necessary to illustrate the bias type.\n"
        "4. Annotate each example with:\n"
        "   - 'context': A brief description of the scenario.\n"
        "   - 'text': The biased content or decision.\n"
        "   - 'label': A JSON object with 'parent_label' as 'bias' and 'sub_label' indicating the specific type of bias.\n\n"
        "Example:\n"
        "1. {'context': 'A hiring decision influenced by appearance', 'text': 'This candidate looks v professional; they must be the best fit.', 'label': {'parent_label': 'bias', 'sub_label': 'halo_effect'}}\n"
        "2. {'context': 'Gender bias in workplace feedback', 'text': 'She's not as aggressive as the male candidates; she might not handle pressure well.', 'label': {'parent_label': 'bias', 'sub_label': 'gender'}}\n"
        "3. {'context': 'Racial bias in customer service', 'text': 'We usually get complaints when serving ppl from that area.', 'label': {'parent_label': 'bias', 'sub_label': 'racial'}}\n"
        "4. {'context': 'Performance evaluation influenced by recent events', 'text': 'He killed it this month; let's ignore the rest of the yr's avg performance.', 'label': {'parent_label': 'bias', 'sub_label': 'recency'}}\n"
        "5. {'context': 'Egocentric bias in group project', 'text': 'Tbh, I did all the work for the team to finish this project.', 'label': {'parent_label': 'bias', 'sub_label': 'egocentric'}}\n"
        "6. {'context': 'Stereotype in education', 'text': 'Asian students are always top in math; it's just natural for them.', 'label': {'parent_label': 'bias', 'sub_label': 'stereotype'}}"
    )
    user_prompt = (
        "Generate a JSON object with no prefix to response which includes:\n"
        "1. 'context': A brief scenario where a specific type of bias occurs.\n"
        "2. 'text': An example of biased language or decision-making reflecting the scenario. Include abbreviations, slang, or informal language where appropriate.\n"
        "3. 'label': A JSON object with 'parent_label' as 'bias' and 'sub_label' indicating the specific type of bias."
    )
    return f"<|begin_of_text|>{system_prompt}<|eot_id|>{user_prompt}<|eot_id|>"

def generate():
    prompt = make_bias_prompt()
    result = ollama.generate(model=MODEL,
                             prompt=prompt,
                             options={'temperature':0.9,
                                      "top_k":100, 
                                      "top_p":0.96
                                      })
    # print("result: ",result.response,"------")
    response_str = result.get('response', '').strip()
    try:
        data = json.loads(response_str)
        # data['label'] = "bias"
        return data
    except json.JSONDecodeError:
        return {}