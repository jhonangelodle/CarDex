import streamlit as st
from utils.db import load_db, update_entry, delete_entry, set_hof

st.set_page_config(page_title="CarDex", page_icon="📘")

st.title("📘 Your CarDex")

df = load_db()

# -----------------------------
# GOLD GLOW CSS
# -----------------------------
st.markdown("""
    <style>
    .gold-glow {
        border: 4px solid gold;
        border-radius: 12px;
        box-shadow: 0 0 20px gold, 0 0 40px rgba(255, 215, 0, 0.6);
        padding: 10px;
        display: inline-block;
    }
    </style>
""", unsafe_allow_html=True)


# -----------------------------
# EDIT MODE
# -----------------------------
if "edit_index" in st.session_state:
    idx = st.session_state["edit_index"]
    car = df.loc[idx]

    st.header("✏️ Edit Car Entry")

    brand = st.text_input("Brand", value=car["brand"])
    name = st.text_input("Model", value=car["name"])
    rarity = st.selectbox(
        "Rarity",
        ["Common", "Uncommon", "Rare", "Legendary", "Unicorn"],
        index=["Common", "Uncommon", "Rare", "Legendary", "Unicorn"].index(car["rarity"])
    )

    if st.button("💾 Save Changes"):
        update_entry(idx, {
            "brand": brand,
            "name": name,
            "rarity": rarity
        })
        st.success("Car updated!")
        del st.session_state["edit_index"]
        st.rerun()

    if st.button("Cancel"):
        del st.session_state["edit_index"]
        st.rerun()

    st.stop()  # IMPORTANT: prevents the rest of the page from rendering


# -----------------------------
# NORMAL CARDEX VIEW
# -----------------------------
if df.empty:
    st.info("No cars logged yet.")
else:
    for index, row in df.iterrows():
        with st.container():
            st.subheader(f"{row['brand']} {row['name']} ({row['rarity']})")

            # GOLD GLOW FOR UNICORNS
            if row["rarity"] == "Unicorn":
                st.markdown('<div class="gold-glow">', unsafe_allow_html=True)
                st.image(row["img_path"], width=300)
                st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.image(row["img_path"], width=300)

            col1, col2, col3 = st.columns(3)

            # EDIT BUTTON
            with col1:
                if st.button("✏️ Edit", key=f"edit_{index}"):
                    st.session_state["edit_index"] = index
                    st.rerun()

            # DELETE BUTTON
            with col2:
                if st.button("🗑 Delete", key=f"delete_{index}"):
                    delete_entry(row["id"])
                    st.rerun()

            # HALL OF FAME BUTTON
            with col3:
                if st.button("🏆 Add to Hall of Fame", key=f"hof_{index}"):
                    set_hof(row["id"], True)
                    st.success("Added to Hall of Fame!")
                    st.rerun()

            st.markdown("---")
