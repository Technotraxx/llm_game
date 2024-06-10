import streamlit as st

# Initialisierung der Charakterwerte
if 'character' not in st.session_state:
    st.session_state.character = {
        'Name': 'Abenteurer',
        'Level': 1,
        'Gesundheit': 100,
        'Mana': 50,
        'Erfahrung': 0,
        'Gold': 10
    }

# Sidebar zur Darstellung des Charakters
st.sidebar.title("Charakter")
st.sidebar.text(f"Name: {st.session_state.character['Name']}")
st.sidebar.text(f"Level: {st.session_state.character['Level']}")
st.sidebar.text(f"Gesundheit: {st.session_state.character['Gesundheit']}")
st.sidebar.text(f"Mana: {st.session_state.character['Mana']}")
st.sidebar.text(f"Erfahrung: {st.session_state.character['Erfahrung']}")
st.sidebar.text(f"Gold: {st.session_state.character['Gold']}")

# Hauptbereich des Spiels
st.title("Rundenbasiertes Rollenspiel")

# Beispiel Encounter
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
    # Hier würde die Logik zur Verarbeitung der Option und die Anfrage an die LLM erfolgen.
