import os
import streamlit as st
from utils.db import load_db, delete_entry, set_hof
from utils.images import delete_image
from utils.layout import rarity_badge, card_header

st.set_page_config(page_title="CarDex - Dex", page_icon="📘", layout="wide")

def main():
    card_header()
    st.subheader("📘 Car Dex")

    df = load_db()
    if df.empty:
        st.info("No cars logged yet. Go to **📸 Add Sighting** to log your first one!")
        return

    # Filters
    with st.sidebar:
        st.header("🔎 Search & Filter")
        search = st.text_input("Search brand or model")
        rarity_options = sorted(df["rarity"].dropna().unique().tolist())
        rarity_filter = st.multiselect("Filter by rarity", rarity_options, default=rarity_options)
        sort_option = st.selectbox("Sort by", ["Newest", "Oldest", "Brand", "Rarity"])

    filtered = df.copy()

    # Search filter
    if search:
        mask = (
            filtered["brand"].str.contains(search, case=False, na=False) |
            filtered["name"].str.contains(search, case=False, na=False)
        )
        filtered = filtered[mask]

    # Rarity filter
    if rarity_filter:
        filtered = filtered[filtered["rarity"].isin(rarity_filter)]

    # Sorting
    if sort_option == "Newest":
        filtered = filtered.sort_values("time", ascending=False)
    elif sort_option == "Oldest":
        filtered = filtered.sort_values("time", ascending=True)
    elif sort_option == "Brand":
        filtered = filtered.sort_values("brand", ascending=True)
    elif sort_option == "Rarity":
        filtered = filtered.sort_values("rarity", ascending=True)

    if filtered.empty:
        st.warning("No entries match your filters.")
        return

    # Card grid layout
    cols = st.columns(3)
    for i, (_, row) in enumerate(filtered.iterrows()):
        col = cols[i % 3]
        with col:
            with st.container(border=True):
                st.markdown(f"### {row['brand']} {row['name']}")
                rarity_badge(row["rarity"])
                st.write(f"🕒 {row['time']}")

                # Image
                if row["img_path"] and os.path.exists(str(row["img_path"])):
                    st.image(row["img_path"], use_container_width=True)

                # Hall of Fame toggle
                if row.get("hof") == True:
                    st.success("🌟 Hall of Fame")
                    if st.button("Remove from Hall of Fame", key=f"remove_hof_{row['id']}"):
                        set_hof(row["id"], False)
                        st.rerun()
                else:
                    if st.button("Add to Hall of Fame ⭐", key=f"add_hof_{row['id']}"):
                        set_hof(row["id"], True)
                        st.rerun()

                # Delete button
                if st.button("🗑️ Delete Entry", key=f"delete_{row['id']}"):
                    delete_image(row["img_path"])
                    delete_entry(row["id"])
                    st.success("Entry deleted.")
                    st.rerun()

if __name__ == "__main__":
    main()
