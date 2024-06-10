import google.generativeai as genai
import streamlit as st
import json
import diskcache as dc
from config import generation_config
from prompts import system_prompt, get_encounter_prompt

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
    if 'selected_option' not in st.session_state:
        st.session_state.selected_option = ""
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

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
        user_prompt = get_encounter_prompt(st.session_state.character['Level'])

        gemini = genai.GenerativeModel(model_name="gemini-1.5-flash",
                                       generation_config=generation_config,
                                       system_instruction=system_prompt,
                                       safety_settings=safety_settings)

        chat_session = gemini.start_chat(history=[
            {
                "role": "user",
                "parts": [user_prompt],
            }
        ])

        # Sende eine initiale Nachricht, um die Chat-Sitzung zu starten
        response = chat_session.send_message(user_prompt)

        if response.text:
            st.session_state.encounter_description = response.text
            st.session_state.chat_history = [
                {"role": "user", "parts": [user_prompt]},
                {"role": "model", "parts": [response.text]}
            ]
        else:
            st.session_state.encounter_description = "No output from Gemini."

    # Beispiel-Encounter
    st.subheader("Begegnung")
    if st.session_state.encounter_description:
        st.write(st.session_state.encounter_description)
    else:
        st.write("Drücke den 'Spiel starten' Button, um ein neues Encounter zu generieren.")

    # Optionen für den Spieler
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Kampf"):
            st.session_state.selected_option = "Kampf"
    with col2:
        if st.button("Hilfe leisten"):
            st.session_state.selected_option = "Hilfe leisten"
    with col3:
        if st.button("Verhandeln"):
            st.session_state.selected_option = "Verhandeln"

    # Verarbeiten der Spielerwahl
    if st.session_state.selected_option:
        player_action = st.session_state.selected_option
        user_message = f"Der Spieler hat sich entschieden für {player_action}"

        new_system_prompt = """
        Reagiere auf die Aktion des Spielers und beschreibe die Konsequenzen der Wahl. 
        """

        # Aktualisieren der Chat-Historie mit der neuen User-Nachricht
        st.session_state.chat_history.append({"role": "user", "parts": [user_message]})

        gemini = genai.GenerativeModel(model_name="gemini-1.5-flash",
                                       generation_config=generation_config,
                                       system_instruction=new_system_prompt,
                                       safety_settings=safety_settings)

        chat_session = gemini.start_chat(history=st.session_state.chat_history)

        response = chat_session.send_message(user_message)

        if response.text:
            st.session_state.encounter_description = response.text
            st.session_state.chat_history.append({"role": "model", "parts": [response.text]})
        else:
            st.session_state.encounter_description = "No output from Gemini."

        # Zurücksetzen der ausgewählten Option
        st.session_state.selected_option = ""

    # Anzeige der gewählten Option (zu Debugging-Zwecken)
    if st.session_state.selected_option:
        st.write(f"Gewählte Option: {st.session_state.selected_option}")

main()
