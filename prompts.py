# prompts.py

system_prompt_encounter = """
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

system_prompt_action = """
Reagiere auf die Aktion des Spielers und beschreibe die Konsequenzen der Wahl. 
"""

random_events_prompt = """
Die Aktion des Helden hat die folgenden zufälligen Ereignisse ausgelöst. Beziehe sie in deine Antwort ein.

Wenn Fehlschlag: Ja --> mache die Situation dramatischer. Es wird für den Helden nun schwieriger die Situation zu lösen. Die Logik dafür übernimmt aber das Spiel. Du musst nur das Szenario beschreiben.
Wenn Überraschung: Ja --> mache die Situation interessanter und ungewöhnlicher. Es sollte eine interessante Wendung sein. Nichts allzu schlimmes. Die Logik dafür übernimmt aber das Spiel. Du musst nur das Szenario beschreiben.
Wenn Glück: Ja --> mache die Situation deutlich leichter und angenehmer für den Helden. Die Logik dafür übernimmt aber das Spiel. Du musst nur das Szenario beschreiben.
Wenn Erfahrung: Ja gib keine Werteveränderung in deiner Antwort an. Baue es nur in den Text ein, dass der Held durch seine Aktion einen Erfahrungs-Bonus erhalten hat. Es soll sich natürlich lesen. Die Logik dafür übernimmt aber das Spiel. Du musst nur das Szenario beschreiben.
"""

def get_encounter_prompt(level):
    return f"Ein Level Held mit dem Level {level} beginnt sein Abenteuer."
