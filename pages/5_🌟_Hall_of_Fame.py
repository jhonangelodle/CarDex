import os
import streamlit as st
from utils.db import get_hof_entries, set_hof, delete_entry
from utils.images import delete_image
from utils.layout import card_header, rarity_badge

st.set_page_config(page_title="CarDex - Hall of Fame", page_icon="🌟", layout="wide")

def main():
    card_header()
    st.subheader("🌟 Hall of Fame")

    df = get_hof_entries()

    if df.empty:
        st.info("No Hall of Fame entries yet. Add some from the main Dex!")
        return

    cols = st.columns(3)

    for i, (_, row) in enumerate(df.iterrows()):
        col = cols[i % 3]
        with col:
            with st.container(border=True):
                st.markdown(f"### ⭐ {row['brand']} {row['name']}")
                rarity_badge(row["rarity"])
                st.write(f"🕒 {row['time']}")

                # Image
                if row["img_path"] and os.path.exists(str(row["img_path"])):
                    st.image(row["img_path"], use_container_width=True)

                # Remove from Hall of Fame
                if st.button("Remove from Hall of Fame", key=f"remove_hof_{row['id']}"):
                    set_hof(row["id"], False)
                    st.rerun()

                # Delete entry
                if st.button("🗑️ Delete Entry", key=f"delete_{row['id']}"):
                    delete_image(row["img_path"])
                    delete_entry(row["id"])
                    st.success("Entry deleted.")
                    st.rerun()

if __name__ == "__main__":
    main()
