import streamlit as st
from utils.db import load_db, update_entry

st.set_page_config(page_title="CarDex", page_icon="📘")

st.title("📘 Your CarDex")

df = load_db()

st.write(list(df.columns))

if df.empty:
    st.info("No cars logged yet.")
else:
    # Show all logged cars
    for index, row in df.iterrows():
        with st.container():
            st.subheader(f"{row['Brand']} {row['name']} ({row['rarity']})")
            st.image(row["img_path"], width=300)

            # Edit button
            if st.button("✏️ Edit", key=f"edit_{index}"):
                st.session_state["edit_index"] = index

            st.markdown("---")

    # If an edit button was clicked
    if "edit_index" in st.session_state:
        idx = st.session_state["edit_index"]
        car = df.loc[idx]

        st.header("✏️ Edit Car Entry")

        # Pre-filled form using your real column names
        brand = st.text_input("Brand", value=car["Brand"])
        name = st.text_input("Model", value=car["name"])
        rarity = st.selectbox(
            "Rarity",
            ["Common", "Uncommon", "Rare", "Legendary", "Unicorn"],
            index=["Common", "Uncommon", "Rare", "Legendary", "Unicorn"].index(car["rarity"])
        )

        # Save button
        if st.button("💾 Save Changes"):
            update_entry(idx, {
                "Brand": brand,
                "name": name,
                "rarity": rarity
            })
            st.success("Car updated!")
            del st.session_state["edit_index"]
            st.rerun()

        # Cancel button
        if st.button("Cancel"):
            del st.session_state["edit_index"]
            st.rerun()
