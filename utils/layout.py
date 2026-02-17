import streamlit as st

# Colors for rarity badges
RARITY_COLORS = {
    "Common": "#9E9E9E",
    "Uncommon": "#4CAF50",
    "Rare": "#2196F3",
    "Legendary": "#9C27B0",
    "Unicorn": "#FF9800"
}

# -----------------------------
# Header
# -----------------------------
def card_header():
    st.markdown(
        """
        <h1 style="text-align:center; margin-bottom:0;">CarDex</h1>
        <p style="text-align:center; font-size:0.9rem; margin-top:0;">
            Retro Pokédex for Real‑World Cars
        </p>
        """,
        unsafe_allow_html=True
    )

# -----------------------------
# Rarity Badge
# -----------------------------
def rarity_badge(rarity: str):
    color = RARITY_COLORS.get(rarity, "#9E9E9E")
    st.markdown(
        f"""
        <span style="
            background-color:{color};
            padding:4px 8px;
            border-radius:999px;
            color:white;
            font-size:0.8rem;
        ">
            {rarity}
        </span>
        """,
        unsafe_allow_html=True
    )

# -----------------------------
# Achievement Badge
# -----------------------------
def achievement_badge(text, unlocked=True):
    opacity = 1.0 if unlocked else 0.3
    st.markdown(
        f"""
        <div style="
            display:inline-block;
            margin:4px;
            padding:6px 10px;
            border-radius:999px;
            background-color:rgba(255,59,48,{opacity});
            color:white;
            font-size:0.8rem;
        ">
            {text}
        </div>
        """,
        unsafe_allow_html=True
    )
