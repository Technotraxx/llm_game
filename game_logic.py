# game_logic.py

import google.generativeai as genai
import diskcache as dc
import streamlit as st
from config import generation_config
from prompts import system_prompt_encounter, system_prompt_action, get_encounter_prompt, random_events_prompt
from mechanics import calculate_random_events

cache = dc.Cache("cache_dir")

def initialize_game_state():
    if 'api_key' not in st.session_state:
        st.session_state.api_key = None
    if 'encounter_description' not in st.session_state:
        st.session_state.encounter_description = ""
    if 'selected_option' not in st.session_state:
        st.session_state.selected_option = ""
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    if 'response_text' not in st.session_state:
        st.session_state.response_text = ""
    if 'random_events' not in st.session_state:
        st.session_state.random_events = {}
    if 'debug_log' not in st.session_state:
        st.session_state.debug_log = ""
    if 'character' not in st.session_state:
        st.session_state.character = {
            "Name": "Abenteurer",
            "Level": 1,
            "Gesundheit": 100,
            "Mana": 50,
            "Erfahrung": 0,
            "Gold": 10,
            "Stärke": 10,
            "Geschicklichkeit": 10,
            "Intelligenz": 10,
            "Charisma": 10,
            "Verstand": 10,
            "Willenskraft": 10
        }

def log_debug_message(message):
    st.session_state.debug_log += f"{message}\n"

def configure_api_key():
    api_key = st.sidebar.text_input("Enter your API key:", value=st.session_state.api_key)
    if not api_key:
        st.sidebar.error("Please enter your API key.")
        st.stop()
    else:
        st.session_state.api_key = api_key
        genai.configure(api_key=api_key)

def start_encounter():
    user_prompt = get_encounter_prompt(st.session_state.character['Level'])

    cache_key = f"encounter_{user_prompt}"
    if cache_key in cache:
        encounter = cache[cache_key]
        st.session_state.encounter_description = encounter
        st.session_state.chat_history = [
            {"role": "user", "parts": [user_prompt]},
            {"role": "model", "parts": [encounter]}
        ]
        log_debug_message("Encounter aus dem Cache geladen.")
        return

    gemini = genai.GenerativeModel(model_name="gemini-1.5-flash",
                                   generation_config=generation_config,
                                   system_instruction=system_prompt_encounter)

    chat_session = gemini.start_chat(history=[
        {"role": "user", "parts": [user_prompt]}
    ])
    response = chat_session.send_message(user_prompt)

    if response.text:
        st.session_state.encounter_description = response.text
        st.session_state.chat_history = [
            {"role": "user", "parts": [user_prompt]},
            {"role": "model", "parts": [response.text]}
        ]
        cache[cache_key] = response.text
        log_debug_message("Neues Encounter generiert.")
    else:
        st.session_state.encounter_description = "No output from Gemini."
        log_debug_message("Fehler beim Generieren des Encounters.")

def handle_player_action():
    if st.session_state.selected_option:
        player_action = st.session_state.selected_option
        user_message = f"Der Spieler hat sich entschieden für {player_action}"

        # Berechnung der zufälligen Ereignisse
        st.session_state.random_events = calculate_random_events(player_action)
        log_debug_message("Zufällige Ereignisse berechnet:")
        for event, occurred in st.session_state.random_events.items():
            log_debug_message(f"{event}: {'Ja' if occurred else 'Nein'}")
        
        # Erfahrung erhöhen, wenn das Event "Erfahrung" ausgelöst wurde
        if st.session_state.random_events.get("Erfahrung", False):
            st.session_state.character["Erfahrung"] += 1
            log_debug_message("Erfahrungspunkte des Helden wurden um 1 erhöht.")

        # Prompt für LLM erstellen
        random_events_details = "\n".join([f"{event}: {'Ja' if occurred else 'Nein'}" for event, occurred in st.session_state.random_events.items()])
        user_message_with_events = f"{user_message}\n\n{random_events_prompt}\n\n{random_events_details}"

        cache_key = f"response_{user_message_with_events}"
        if cache_key in cache:
            response_text = cache[cache_key]
            st.session_state.response_text = response_text
            st.session_state.chat_history.append({"role": "user", "parts": [user_message_with_events]})
            st.session_state.chat_history.append({"role": "model", "parts": [response_text]})
            log_debug_message(f"Antwort aus dem Cache geladen für Aktion: {player_action}")
            return

        st.session_state.chat_history.append({"role": "user", "parts": [user_message_with_events]})

        gemini = genai.GenerativeModel(model_name="gemini-1.5-flash",
                                       generation_config=generation_config,
                                       system_instruction=system_prompt_action)
        chat_session = gemini.start_chat(history=st.session_state.chat_history)
        response = chat_session.send_message(user_message_with_events)

        if response.text:
            st.session_state.response_text = response.text
            st.session_state.chat_history.append({"role": "model", "parts": [response.text]})
            cache[cache_key] = response.text
            log_debug_message("Antwort von Gemini erhalten.")
        else:
            st.session_state.response_text = "No output from Gemini."
            log_debug_message("Fehler beim Empfangen der Antwort von Gemini.")

        st.session_state.selected_option = ""
