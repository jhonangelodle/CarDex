import os
import pandas as pd
from datetime import datetime
from uuid import uuid4

DB_FILE = "cardex_db.csv"

# All columns your app uses
COLUMNS = ["id", "brand", "name", "rarity", "time", "img_path", "hof"]


# -----------------------------
# Database Initialization
# -----------------------------
def init_db():
    """Create the database file if missing, and ensure all columns exist."""
    if not os.path.exists(DB_FILE):
        df = pd.DataFrame(columns=COLUMNS)
        df.to_csv(DB_FILE, index=False)
        return

    df = pd.read_csv(DB_FILE)

    # Ensure all required columns exist
    for col in COLUMNS:
        if col not in df.columns:
            df[col] = None

    df = df[COLUMNS]  # reorder columns
    df.to_csv(DB_FILE, index=False)


# -----------------------------
# Load & Save
# -----------------------------
def load_db():
    init_db()
    return pd.read_csv(DB_FILE)


def save_db(df):
    df.to_csv(DB_FILE, index=False)


# -----------------------------
# Add Entry
# -----------------------------
def add_entry(brand, name, rarity, img_path):
    df = load_db()

    new_row = {
        "id": str(uuid4()),
        "brand": brand,
        "name": name,
        "rarity": rarity,
        "time": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "img_path": img_path,
        "hof": False
    }

    df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
    save_db(df)
    return new_row


# -----------------------------
# Delete Entry
# -----------------------------
def delete_entry(entry_id):
    df = load_db()
    df = df[df["id"] != entry_id]
    save_db(df)


# -----------------------------
# Hall of Fame
# -----------------------------
def set_hof(entry_id, value: bool):
    df = load_db()
    df.loc[df["id"] == entry_id, "hof"] = value
    save_db(df)


def get_hof_entries():
    df = load_db()
    return df[df["hof"] == True]


# -----------------------------
# Stats
# -----------------------------
def get_stats():
    df = load_db()

    if df.empty:
        return {
            "total": 0,
            "unique_brands": 0,
            "by_rarity": {},
            "oldest_time": None,
            "newest_time": None
        }

    by_rarity = df["rarity"].value_counts().to_dict()

    return {
        "total": len(df),
        "unique_brands": df["brand"].nunique(),
        "by_rarity": by_rarity,
        "oldest_time": df["time"].min(),
        "newest_time": df["time"].max()
    }
def update_entry(index, updated_data):
    df = load_db()
    for key, value in updated_data.items():
        df.at[index, key] = value
    df.to_csv(DB_FILE, index=False)
