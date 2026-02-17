import streamlit as st
from utils.db import add_entry
from utils.images import save_uploaded_image
from utils.layout import card_header

st.set_page_config(page_title="CarDex - Add", page_icon="📸", layout="centered")

BRANDS = [
    "McLaren", "Ferrari", "Lamborghini", "Porsche",
    "Koenigsegg", "Pagani", "Bugatti", "Other"
]

RARITIES = ["Common", "Uncommon", "Rare", "Legendary", "Unicorn"]

def main():
    card_header()
    st.subheader("📸 Log a New Sighting")

    with st.form("add_sighting_form", clear_on_submit=True):
        uploaded_file = st.file_uploader("Upload Car Photo", type=["jpg", "jpeg", "png"])

        brand_choice = st.selectbox("Brand", BRANDS)
        if brand_choice == "Other":
            brand = st.text_input("Type Brand Name")
        else:
            brand = brand_choice

        model = st.text_input("Model Name")
        rarity = st.selectbox("Rarity", RARITIES)

        submitted = st.form_submit_button("LOG SIGHTING 🚀")

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

if __name__ == "__main__":
    main()
