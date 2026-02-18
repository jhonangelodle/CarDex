import streamlit as st
from utils.db import load_db, update_entry

st.set_page_config(page_title="CarDex", page_icon="📘")

st.title("📘 Your CarDex")

df = load_db()

# If editing, show ONLY the edit form
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

    st.stop()  # <-- IMPORTANT: prevents rest of page from rendering


# NORMAL CARDEX PAGE BELOW THIS LINE
if df.empty:
    st.info("No cars logged yet.")
else:
    for index, row in df.iterrows():
        with st.container():
            st.subheader(f"{row['brand']} {row['name']} ({row['rarity']})")
            st.image(row["img_path"], width=300)

            col1, col2, col3 = st.columns(3)

            with col1:
                if st.button("✏️ Edit", key=f"edit_{index}"):
                    st.session_state["edit_index"] = index
                    st.rerun()

            with col2:
                if st.button("🗑 Delete", key=f"delete_{index}"):
                    df = df.drop(index)
                    df.to_csv("database.csv", index=False)
                    st.rerun()

            with col3:
                if st.button("🏆 Add to Hall of Fame", key=f"hof_{index}"):
                    df.at[index, "hof"] = True
                    df.to_csv("database.csv", index=False)
                    st.success("Added to Hall of Fame!")
                    st.rerun()

            st.markdown("---")
