import streamlit as st
from utils.layout import card_header
from utils.db import load_db, get_stats

st.set_page_config(
    page_title="CarDex",
    page_icon="🏎️",
    layout="wide"
)

def main():
    card_header()
    st.write("Welcome to **CarDex 2.0** — your retro Pokédex for real‑world cars.")

    df = load_db()
    stats = get_stats()

    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Cars Logged", stats["total"])
    with col2:
        st.metric("Unique Brands", stats["unique_brands"])
    with col3:
        st.metric("Rarity Types Logged", len(stats["by_rarity"]))

    st.write("---")
    st.write(
        "Use the pages in the sidebar:\n\n"
        "- **📘 Car Dex** to browse entries\n"
        "- **📸 Add Sighting** to log new cars\n"
        "- **📊 Stats** for analytics\n"
        "- **🏆 Achievements** for goals\n"
        "- **🌟 Hall of Fame** for your best sightings"
    )

if __name__ == "__main__":
    main()
