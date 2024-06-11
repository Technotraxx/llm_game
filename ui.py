# ui.py

import streamlit as st
from character import display_character
from game_logic import start_encounter, handle_player_action

def display_encounter():
    st.subheader("Begegnung")
    if st.session_state.encounter_description:
        st.write(st.session_state.encounter_description)
        display_action_buttons()
    else:
        st.write("Drücke den 'Spiel starten' Button, um ein neues Encounter zu generieren.")

def display_action_buttons():
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
    
    handle_player_action()

def display_response():
    if st.session_state.response_text:
        st.subheader("Reaktion:")
        st.write(st.session_state.response_text)

    if "debug_random_events" in st.session_state and st.session_state.debug_random_events:
        st.subheader("Zufällige Ereignisse (Debug):")
        for event, occurred in st.session_state.debug_random_events.items():
            st.write(f"{event}: {'Ja' if occurred else 'Nein'}")

def display_debug_log():
    st.sidebar.subheader("Debug Log")
    st.sidebar.text_area("Log", st.session_state.debug_log, height=300)
