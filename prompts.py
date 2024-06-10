# prompts.py

system_prompt = """
Beschreibe ein zufälliges Encounter in einem Fantasy-Rollenspiel.

Der Encounter soll herausfordernd, aber schaffbar sein. Daher berücksichtige die Informationen über den Spieler, über sein aktuelles Level, seine Fähigkeiten, Stärken und Schwächen und Ausrüstung. Berücksichtige die 3 Standard-Reaktionsmöglichkeiten. Der Encounter muss immer so geschaffen sein, dass alle drei Optionen zumindest möglich sein können. Es ist aber okay, dass für einen Encounter Kampf die leichtere Option wäre, während eine friedliche Alternative für einen anderen Encounter besser funktionieren würde.

Baue den Encounter folgendermaßen auf:

Kurze Beschreibung der Situation. Was ist passiert, was sieht, hört, riecht oder spürt der Spieler.

Was ist zu tun?

Gib 3 Optionen, um die Situation zu lösen.

Kampf (durch Stärke, Geschick, Schlauheit), 
Hilfe leisten (durch Intelligenz, Talent, Willenskraft, Kreativität) 
Verhandeln (durch Reden, Überzeugen, Ausweichen, Handeln, Geschenke, Lügen, Schmeicheleien)

Füge keine Charakter-Werte oder Ausrüstung hinzu, sofern es nicht als Prompt dir gesagt wird.
"""

def get_encounter_prompt(level):
    return f"Ein Level {level} Held beginnt sein Abenteuer."
