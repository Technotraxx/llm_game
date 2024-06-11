# mechanics.py

import random

def calculate_random_events(action):
    if action == "Kampf":
        events = {
            "Fehlschlag": random.random() < 0.05,
            "Glück": random.random() < 0.10,
            "Überraschung": random.random() < 0.10,
            "Erfahrung": random.random() < 0.25,
        }
    elif action == "Hilfe leisten":
        events = {
            "Fehlschlag": random.random() < 0.10,
            "Glück": random.random() < 0.20,
            "Überraschung": random.random() < 0.15,
            "Erfahrung": random.random() < 0.15,
        }
    elif action == "Verhandeln":
        events = {
            "Fehlschlag": random.random() < 0.20,
            "Glück": random.random() < 0.05,
            "Überraschung": random.random() < 0.25,
            "Erfahrung": random.random() < 0.10,
        }
    return events
