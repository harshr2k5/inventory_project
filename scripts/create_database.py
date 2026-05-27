import sqlite3
import pandas as pd

# Connect to SQLite DB
conn = sqlite3.connect("inventory.db")

# Read CSV files
products = pd.read_csv("data/products.csv")
sales = pd.read_csv("data/sales.csv")
inventory = pd.read_csv("data/inventory.csv")
suppliers = pd.read_csv("data/suppliers.csv")

# Store tables in database
products.to_sql(
    "products",
    conn,
    if_exists="replace",
    index=False
)

sales.to_sql(
    "sales",
    conn,
    if_exists="replace",
    index=False
)

inventory.to_sql(
    "inventory",
    conn,
    if_exists="replace",
    index=False
)

suppliers.to_sql(
    "suppliers",
    conn,
    if_exists="replace",
    index=False
)

print("SQLite database created successfully!")

conn.close()