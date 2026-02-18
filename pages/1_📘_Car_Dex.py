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

    st.stop()


# -----------------------------
# FILTERS + SORTING
# -----------------------------
st.subheader("🔍 Filters & Sorting")

colA, colB, colC, colD = st.columns(4)

with colA:
    brand_filter = st.selectbox(
        "Brand",
        ["All"] + sorted(df["brand"].dropna().unique().tolist())
    )

with colB:
    rarity_filter = st.selectbox(
        "Rarity",
        ["All", "Common", "Uncommon", "Rare", "Legendary", "Unicorn"]
    )

with colC:
    hof_filter = st.selectbox(
        "Hall of Fame",
        ["All", "Only HOF", "Exclude HOF"]
    )

with colD:
    sort_by = st.selectbox(
        "Sort By",
        ["Newest", "Oldest", "Brand A→Z", "Brand Z→A", "Rarity Rank"]
    )

# View mode selector
view_mode = st.radio(
    "View Mode",
    ["List View", "Grid View"],
    horizontal=True
)


# -----------------------------
# APPLY FILTERS
# -----------------------------
filtered_df = df.copy()

if brand_filter != "All":
    filtered_df = filtered_df[filtered_df["brand"] == brand_filter]

if rarity_filter != "All":
    filtered_df = filtered_df[filtered_df["rarity"] == rarity_filter]

if hof_filter == "Only HOF":
    filtered_df = filtered_df[filtered_df["hof"] == True]
elif hof_filter == "Exclude HOF":
    filtered_df = filtered_df[filtered_df["hof"] == False]


# -----------------------------
# APPLY SORTING
# -----------------------------
rarity_order = {
    "Common": 1,
    "Uncommon": 2,
    "Rare": 3,
    "Legendary": 4,
    "Unicorn": 5
}

if sort_by == "Newest":
    filtered_df = filtered_df.sort_values("time", ascending=False)
elif sort_by == "Oldest":
    filtered_df = filtered_df.sort_values("time", ascending=True)
elif sort_by == "Brand A→Z":
    filtered_df = filtered_df.sort_values("brand", ascending=True)
elif sort_by == "Brand Z→A":
    filtered_df = filtered_df.sort_values("brand", ascending=False)
elif sort_by == "Rarity Rank":
    filtered_df = filtered_df.sort_values(
        by="rarity",
        key=lambda col: col.map(rarity_order)
    )


# -----------------------------
# GRID VIEW FUNCTION
# -----------------------------
def render_grid(df):
    cols = st.columns(3)

    for i, (idx, row) in enumerate(df.iterrows()):
        col = cols[i % 3]

        with col:
            st.subheader(f"{row['brand']} {row['name']} ({row['rarity']})")

            if row["rarity"] == "Unicorn":
                st.markdown('<div class="gold-glow">', unsafe_allow_html=True)
                st.image(row["img_path"], width=250)
                st.markdown('</div>', unsafe_allow_html=True)
            else:
                st.image(row["img_path"], width=250)

            if st.button("✏️ Edit", key=f"edit_grid_{i}"):
                st.session_state["edit_index"] = idx
                st.rerun()

            if st.button("🗑 Delete", key=f"delete_grid_{i}"):
                delete_entry(row["id"])
                st.rerun()

            if st.button("🏆 HOF", key=f"hof_grid_{i}"):
                set_hof(row["id"], True)
                st.rerun()


# -----------------------------
# DISPLAY CARDEX LIST
# -----------------------------
if filtered_df.empty:
    st.info("No cars match your filters.")
else:
    if view_mode == "Grid View":
        render_grid(filtered_df)
    else:
        for index, row in filtered_df.iterrows():
            with st.container():
                st.subheader(f"{row['brand']} {row['name']} ({row['rarity']})")

                if row["rarity"] == "Unicorn":
                    st.markdown('<div class="gold-glow">', unsafe_allow_html=True)
                    st.image(row["img_path"], width=300)
                    st.markdown('</div>', unsafe_allow_html=True)
                else:
                    st.image(row["img_path"], width=300)

                col1, col2, col3 = st.columns(3)

                with col1:
                    if st.button("✏️ Edit", key=f"edit_{index}"):
                        st.session_state["edit_index"] = index
                        st.rerun()

                with col2:
                    if st.button("🗑 Delete", key=f"delete_{index}"):
                        delete_entry(row["id"])
                        st.rerun()

                with col3:
                    if st.button("🏆 Add to Hall of Fame", key=f"hof_{index}"):
                        set_hof(row["id"], True)
                        st.success("Added to Hall of Fame!")
                        st.rerun()

                st.markdown("---")
