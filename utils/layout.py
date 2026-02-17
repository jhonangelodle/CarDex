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
import streamlit as st

def show_new_entry_banner():
    st.markdown(
        """
        <div style="
            padding: 12px 20px;
            background: linear-gradient(90deg, #FF4B4B, #FF8A00);
            color: white;
            border-radius: 8px;
            font-size: 20px;
            font-weight: bold;
            text-align: center;
            margin-top: 15px;
            animation: slideDown 0.6s ease-out;
        ">
            🚗 New Entry Registered!
        </div>

        <style>
        @keyframes slideDown {
            0% { transform: translateY(-20px); opacity: 0; }
            100% { transform: translateY(0); opacity: 1; }
        }
        </style>
        """,
        unsafe_allow_html=True
    )
import streamlit as st

def fire_celebration():
    st.markdown(
        """
        <div style="
            padding: 14px 20px;
            background: #ff6a00;
            color: white;
            border-radius: 10px;
            font-size: 22px;
            font-weight: bold;
            text-align: center;
            margin-top: 15px;
            animation: popIn 0.4s ease-out;
        ">
            🔥 New Entry Registered! 🔥
        </div>

        <style>
        @keyframes popIn {
            0% { transform: scale(0.6); opacity: 0; }
            100% { transform: scale(1); opacity: 1; }
        }
        </style>
        """,
        unsafe_allow_html=True
    )
