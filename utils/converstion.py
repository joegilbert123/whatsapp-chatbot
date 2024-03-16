from fuzzywuzzy import fuzz
import random
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


def load_intents(file_path):
    with open(file_path) as file:
        return json.load(file)


def chat(query, intents=None):
    best_match = None
    highest_score = 0
    intents = intents or load_intents(BASE_DIR / "intents.json")

    for intent in intents:
        for question in intent["questions"]:
            similarity_score = fuzz.ratio(query.lower(), question.lower())
            if similarity_score == 100:
                return random.choice(intent["responses"])
            elif similarity_score > highest_score:
                best_match = intent
                highest_score = similarity_score

    if best_match:
        return random.choice(best_match["responses"])
    else:
        return "I'm sorry, I couldn't unserstand what you are trying to ask"
