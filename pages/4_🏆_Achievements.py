import streamlit as st
from utils.db import load_db
from utils.layout import card_header, achievement_badge

st.set_page_config(page_title="CarDex - Achievements", page_icon="🏆", layout="centered")

def main():
    card_header()
    st.subheader("🏆 Achievements")

    df = load_db()
    total = len(df)
    brands = df["brand"].nunique() if not df.empty else 0

    # Achievement conditions
    has_legendary = not df[df["rarity"] == "Legendary"].empty
    has_unicorn = not df[df["rarity"] == "Unicorn"].empty
    has_ferrari = not df[df["brand"].str.contains("Ferrari", case=False, na=False)].empty
    has_10 = total >= 10
    has_50 = total >= 50

    st.markdown("#### Milestones")
    achievement_badge("First Car Logged", unlocked=(total >= 1))
    achievement_badge("10 Cars Logged", unlocked=has_10)
    achievement_badge("50 Cars Logged", unlocked=has_50)

    st.markdown("#### Rarity Hunter")
    achievement_badge("Spotted a Legendary", unlocked=has_legendary)
    achievement_badge("Spotted a Unicorn", unlocked=has_unicorn)

    st.markdown("#### Brand Collector")
    achievement_badge("Spotted a Ferrari", unlocked=has_ferrari)
    achievement_badge("5+ Unique Brands", unlocked=(brands >= 5))
    achievement_badge("10+ Unique Brands", unlocked=(brands >= 10))

    st.write("---")
    st.write(f"Total cars logged: **{total}** | Unique brands: **{brands}**")

if __name__ == "__main__":
    main()
