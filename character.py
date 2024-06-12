# character.py

import streamlit as st

def initialize_character():
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

def display_character():
    st.sidebar.subheader("Charakter")
    st.sidebar.text(f"Name: {st.session_state.character['Name']}")
    st.sidebar.text(f"Level: {st.session_state.character['Level']}")
    st.sidebar.text(f"Gesundheit: {st.session_state.character['Gesundheit']}")
    st.sidebar.text(f"Mana: {st.session_state.character['Mana']}")
    st.sidebar.text(f"Erfahrung: {st.session_state.character['Erfahrung']}")
    st.sidebar.text(f"Gold: {st.session_state.character['Gold']}")
    st.sidebar.text(f"Stärke: {st.session_state.character['Stärke']}")
    st.sidebar.text(f"Geschicklichkeit: {st.session_state.character['Geschicklichkeit']}")
    st.sidebar.text(f"Intelligenz: {st.session_state.character['Intelligenz']}")
    st.sidebar.text(f"Charisma: {st.session_state.character['Charisma']}")
    st.sidebar.text(f"Verstand: {st.session_state.character['Verstand']}")
    st.sidebar.text(f"Willenskraft: {st.session_state.character['Willenskraft']}")
