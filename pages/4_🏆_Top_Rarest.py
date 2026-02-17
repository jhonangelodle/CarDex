import streamlit as st
import pandas as pd
from utils.db import load_db
from utils.layout import show_logo

st.set_page_config(page_title="Top Rarest Cars", page_icon="🏆")

show_logo()

st.title("🏆 Top 5 Rarest Cars")

df = load_db()

if df.empty:
    st.info("No sightings yet. Log some cars to build your showcase!")
else:
    # Rarity ranking system
    rarity_order = {
        "Common": 1,
        "Uncommon": 2,
        "Rare": 3,
        "Legendary": 4,
        "Unicorn": 5
    }

    df["rarity_score"] = df["rarity"].map(rarity_order)

    # Sort by rarity, then newest first
    top5 = df.sort_values(
        ["rarity_score", "timestamp"], 
        ascending=[False, False]
    ).head(5)

    for idx, row in top5.iterrows():
        st.markdown(f"## {row['rarity']} — {row['brand']} {row['name']}")
        st.image(row["image_path"], width=350)
        st.markdown("---")
