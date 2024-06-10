# game_logic.py

import google.generativeai as genai
import diskcache as dc
import streamlit as st
from config import generation_config
from prompts import system_prompt_encounter, system_prompt_action

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
    else:
        st.session_state.encounter_description = "No output from Gemini."

def handle_player_action():
    if st.session_state.selected_option:
        player_action = st.session_state.selected_option
        user_message = f"Der Spieler hat sich entschieden für {player_action}"

        st.session_state.chat_history.append({"role": "user", "parts": [user_message]})
        
        gemini = genai.GenerativeModel(model_name="gemini-1.5-flash",
                                       generation_config=generation_config,
                                       system_instruction=system_prompt_action)
        chat_session = gemini.start_chat(history=st.session_state.chat_history)
        response = chat_session.send_message(user_message)
        
        if response.text:
            st.session_state.response_text = response.text
            st.session_state.chat_history.append({"role": "model", "parts": [response.text]})
        else:
            st.session_state.response_text = "No output from Gemini."
        
        st.session_state.selected_option = ""
