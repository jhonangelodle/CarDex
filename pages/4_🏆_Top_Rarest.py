import streamlit as st
import pandas as pd
from utils.db import load_db

st.set_page_config(page_title="Top Rarest Cars", page_icon="🏆")

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

    # Fade-in animation + gold glow CSS
    st.markdown("""
        <style>
        .fade-in {
            animation: fadeIn 1s ease forwards;
            opacity: 0;
        }
        @keyframes fadeIn {
            from { opacity: 0; transform: translateY(10px); }
            to { opacity: 1; transform: translateY(0); }
        }

        .gold-glow {
            border: 4px solid gold;
            border-radius: 12px;
            box-shadow: 0 0 20px gold, 0 0 40px rgba(255, 215, 0, 0.6);
            padding: 10px;
            display: inline-block;
        }
        </style>
    """, unsafe_allow_html=True)

    # Display each car with staggered animation
    delay = 0.0
    for idx, row in top5.iterrows():
        delay += 0.2  # stagger each reveal

        # Crown for Unicorns
        if row["rarity"] == "Unicorn":
            st.markdown(
                f"""
                <div class="fade-in" style="animation-delay: {delay}s; font-size: 40px; text-align:center;">
                    👑
                </div>
                """,
                unsafe_allow_html=True
            )

        # Title reveal
        st.markdown(
            f"""
            <div class="fade-in" style="animation-delay: {delay}s;">
                <h2>{row['rarity']} — {row['brand']} {row['name']}</h2>
            </div>
            """,
            unsafe_allow_html=True
        )

        # Image reveal with gold glow for Unicorns
        if row["rarity"] == "Unicorn":
            st.markdown(
                f"""
                <div class="fade-in gold-glow" style="animation-delay: {delay + 0.1}s;">
                """,
                unsafe_allow_html=True
            )
            st.image(row["image_path"], width=350)
            st.markdown("</div>", unsafe_allow_html=True)
        else:
            st.markdown(
                f"""
                <div class="fade-in" style="animation-delay: {delay + 0.1}s;">
                """,
                unsafe_allow_html=True
            )
            st.image(row["image_path"], width=350)
            st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("---")
