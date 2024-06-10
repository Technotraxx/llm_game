import google.generativeai as genai
import streamlit as st
import json
import diskcache as dc
from config import generation_config
from prompts import get_encounter_prompt

# Funktion zur Initialisierung des Session State
def initialize_session_state():
    if 'character' not in st.session_state:
        st.session_state.character = {
            'Name': 'Abenteurer',
            'Level': 1,
            'Gesundheit': 100,
            'Mana': 50,
            'Erfahrung': 0,
            'Gold': 10
        }
    if 'api_key' not in st.session_state:
        st.session_state.api_key = None
    if 'encounter_description' not in st.session_state:
        st.session_state.encounter_description = ""

# Haupt-Streamlit-App
def main():
    st.title("Rundenbasiertes Rollenspiel")

    # Initialisierung des Session State
    initialize_session_state()

    # API-Schlüssel in der Sidebar konfigurieren
    api_key = st.sidebar.text_input("Enter your API key:", value=st.session_state.api_key)

    # Überprüfen, ob der API-Schlüssel angegeben ist
    if not api_key:
        st.sidebar.error("Please enter your API key.")
        st.stop()
    else:
        # API-Schlüssel im Session State speichern
        st.session_state.api_key = api_key

    genai.configure(api_key=api_key)

    safety_settings = "{}"
    safety_settings = json.loads(safety_settings)

    # Charakter in der Sidebar anzeigen
    st.sidebar.title("Charakter")
    st.sidebar.text(f"Name: {st.session_state.character['Name']}")
    st.sidebar.text(f"Level: {st.session_state.character['Level']}")
    st.sidebar.text(f"Gesundheit: {st.session_state.character['Gesundheit']}")
    st.sidebar.text(f"Mana: {st.session_state.character['Mana']}")
    st.sidebar.text(f"Erfahrung: {st.session_state.character['Erfahrung']}")
    st.sidebar.text(f"Gold: {st.session_state.character['Gold']}")

    # Button zum Starten des Spiels
    if st.button("Spiel starten"):
        prompt = get_encounter_prompt()

        gemini = genai.GenerativeModel(model_name="gemini-1.5-flash",
                                       generation_config=generation_config,
                                       safety_settings=safety_settings)

        prompt_parts = [prompt]

        cache = dc.Cache('cache_dir')  # Verwenden des diskcache
        cache_key = "encounter_description"

        if cache_key in cache:
            encounter_description = cache[cache_key]
            st.write("Verwende zwischengespeicherte Antwort")
        else:
            try:
                response = gemini.generate_content(prompt_parts)
                if response.text:
                    encounter_description = response.text
                    cache[cache_key] = encounter_description  # Antwort zwischengespeichern
                else:
                    encounter_description = "No output from Gemini."
            except Exception as e:
                encounter_description = f"An error occurred: {str(e)}"

        st.session_state.encounter_description = encounter_description

    # Beispiel-Encounter
    st.subheader("Begegnung")
    if st.session_state.encounter_description:
        st.write(st.session_state.encounter_description)
    else:
        st.write("Drücke den 'Spiel starten' Button, um ein neues Encounter zu generieren.")

    # Optionen für den Spieler
    option = st.selectbox(
        "Wie möchtest du vorgehen?",
        ["Betrete den Tempel", "Untersuche die Umgebung", "Weitergehen"]
    )

    # Reaktion auf die gewählte Option
    if st.button("Bestätigen"):
        st.write(f"Du hast die Option '{option}' gewählt.")
        prompt = f"Spieler hat die Option '{option}' gewählt. Was passiert als nächstes?"

        gemini = genai.GenerativeModel(model_name="gemini-1.5-flash",
                                       generation_config=generation_config,
                                       safety_settings=safety_settings)

        prompt_parts = [prompt]

        cache_key = f"response_{option}"

        if cache_key in cache:
            response_text = cache[cache_key]
            st.write("Verwende zwischengespeicherte Antwort")
        else:
            try:
                response = gemini.generate_content(prompt_parts)
                if response.text:
                    response_text = response.text
                    cache[cache_key] = response_text  # Antwort zwischengespeichern
                else:
                    response_text = "No output from Gemini."
            except Exception as e:
                response_text = f"An error occurred: {str(e)}"

        st.subheader("Ergebnis:")
        st.write(response_text)

main()
