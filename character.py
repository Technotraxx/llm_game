# character.py

import streamlit as st

def initialize_character():
    if 'character' not in st.session_state:
        st.session_state.character = {
            'Name': 'Abenteurer',
            'Level': 1,
            'Gesundheit': 100,
            'Mana': 50,
            'Erfahrung': 0,
            'Gold': 10
        }

def display_character():
    st.sidebar.title("Charakter")
    st.sidebar.text(f"Name: {st.session_state.character['Name']}")
    st.sidebar.text(f"Level: {st.session_state.character['Level']}")
    st.sidebar.text(f"Gesundheit: {st.session_state.character['Gesundheit']}")
    st.sidebar.text(f"Mana: {st.session_state.character['Mana']}")
    st.sidebar.text(f"Erfahrung: {st.session_state.character['Erfahrung']}")
    st.sidebar.text(f"Gold: {st.session_state.character['Gold']}")
