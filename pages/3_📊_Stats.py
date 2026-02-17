import streamlit as st
import pandas as pd
from utils.db import load_db, get_stats
from utils.layout import card_header

st.set_page_config(page_title="CarDex - Stats", page_icon="📊", layout="wide")

def main():
    card_header()
    st.subheader("📊 Stats & Analytics")

    df = load_db()
    stats = get_stats()

    if df.empty:
        st.info("No data yet. Log some cars first!")
        return

    # Top metrics
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Cars Logged", stats["total"])
    with col2:
        st.metric("Unique Brands", stats["unique_brands"])
    with col3:
        st.metric("Rarity Types Logged", len(stats["by_rarity"]))

    st.write("---")

    # Charts
    col_a, col_b = st.columns(2)

    with col_a:
        st.markdown("#### Cars by Rarity")
        rarity_counts = pd.Series(stats["by_rarity"])
        st.bar_chart(rarity_counts)

    with col_b:
        st.markdown("#### Top Brands")
        top_brands = df["brand"].value_counts().head(10)
        st.bar_chart(top_brands)

    st.write("---")
    st.markdown("#### Raw Data")
    st.dataframe(df.sort_values("time", ascending=False), use_container_width=True)

if __name__ == "__main__":
    main()
