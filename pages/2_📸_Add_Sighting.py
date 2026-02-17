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
