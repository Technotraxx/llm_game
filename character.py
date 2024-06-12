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
    character = st.session_state.character

    character_html = f"""
    <div style="background-color:#f2f2f2;padding:10px;border-radius:10px;">
        <h3 style="text-align:center;">Charakter</h3>
        <p><strong>Name:</strong> {character['Name']}</p>
        <p><strong>Level:</strong> {character['Level']}</p>
        <p><strong>Gesundheit:</strong> {character['Gesundheit']}</p>
        <p><strong>Mana:</strong> {character['Mana']}</p>
        <p><strong>Erfahrung:</strong> {character['Erfahrung']}</p>
        <p><strong>Gold:</strong> {character['Gold']}</p>
        <h4 style="text-align:center;">Eigenschaften</h4>
        <p><strong>Stärke:</strong> {character['Stärke']}</p>
        <p><strong>Geschicklichkeit:</strong> {character['Geschicklichkeit']}</p>
        <p><strong>Intelligenz:</strong> {character['Intelligenz']}</p>
        <p><strong>Charisma:</strong> {character['Charisma']}</p>
        <p><strong>Verstand:</strong> {character['Verstand']}</p>
        <p><strong>Willenskraft:</strong> {character['Willenskraft']}</p>
    </div>
    """
    st.sidebar.markdown(character_html, unsafe_allow_html=True)
