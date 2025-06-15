import sqlite3
import pandas as pd
import os

# Path to your SQLite DB
DB_PATH = "ctfd.db"
EXPORT_DIR = "ctfd_exports"

# Create export directory
os.makedirs(EXPORT_DIR, exist_ok=True)

# Connect to SQLite
conn = sqlite3.connect(DB_PATH)
cursor = conn.cursor()

# Get list of all tables
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# Export each table
for (table_name,) in tables:
    df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
    file_path = os.path.join(EXPORT_DIR, f"{table_name}.xlsx")
    df.to_excel(file_path, index=False)
    print(f"✅ Exported {table_name} to {file_path}")

conn.close()
