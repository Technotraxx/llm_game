# mechanics.py

import random

def calculate_random_events():
    events = {
        "Fehlschlag": random.random() < 0.05,
        "Glück": random.random() < 0.10,
        "Überraschung": random.random() < 0.10,
        "Erfahrung": random.random() < 0.25,
    }
    return events
