import streamlit as st
from utils.db import add_entry
from utils.images import save_uploaded_image

st.set_page_config(page_title="Add Sighting", page_icon="📸")

st.title("📸 Add a New Car Sighting")

with st.form("add_car_form"):
    brand = st.text_input("Brand")
    model = st.text_input("Model")
    rarity = st.selectbox("Rarity", ["Common", "Uncommon", "Rare", "Legendary", "Unicorn"])
    uploaded_file = st.file_uploader("Upload a photo", type=["jpg", "jpeg", "png"])

    submitted = st.form_submit_button("Log Sighting")

if submitted:
    if not uploaded_file:
        st.error("Please upload a photo.")
    elif not brand:
        st.error("Please enter a brand.")
    elif not model:
        st.error("Please enter a model name.")
    else:
        img_path = save_uploaded_image(uploaded_file)
        entry = add_entry(brand, model, rarity, img_path)

        st.success(f"Secured {entry['brand']} {entry['name']}!")

        # 🎉 Confetti animation
        st.snow()
