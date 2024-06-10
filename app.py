import google.generativeai as genai
import streamlit as st
import json
from config import generation_config

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

    # Beispiel-Encounter
    st.subheader("Begegnung")
    encounter_description = "Du stehst vor einem alten, verwitterten Tempel. Die Luft ist kühl und eine mystische Aura umgibt den Ort."
    st.write(encounter_description)

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

        try:
            response = gemini.generate_content(prompt_parts)
            st.subheader("Ergebnis:")
            if response.text:
                st.write(response.text)
            else:
                st.write("No output from Gemini.")
        except Exception as e:
            st.write(f"An error occurred: {str(e)}")

main()
