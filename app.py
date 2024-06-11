import streamlit as st
from character import initialize_character, display_character
from game_logic import initialize_game_state, configure_api_key, start_encounter
from ui import display_encounter, display_response, display_debug_log, update_debug_log

def main():
    st.title("Rundenbasiertes Rollenspiel")

    # Initialisierungen
    initialize_character()
    initialize_game_state()

    # API-Schlüssel konfigurieren
    configure_api_key()

    # Charakter anzeigen
    display_character()

    # Debug-Log anzeigen
    display_debug_log()

    # Button zum Starten des Spiels
    if st.button("Spiel starten"):
        start_encounter()
        update_debug_log()

    # Encounter anzeigen
    display_encounter()

    # Reaktion auf die Spielerwahl anzeigen
    display_response()

if __name__ == "__main__":
    main()
