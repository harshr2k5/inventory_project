import sqlite3
import pandas as pd
import numpy as np

# --------------------------------
# CONNECT DATABASE
# --------------------------------

conn = sqlite3.connect("inventory.db")

# --------------------------------
# DEMAND ANALYSIS
# --------------------------------

query = """
SELECT
    s.SKU_ID,
    p.Product_Name,
    p.Category,
    p.Supplier,
    AVG(s.Units_Sold) AS Avg_Daily_Demand,
    SUM(s.Units_Sold) AS Total_Demand
FROM sales s
JOIN products p
ON s.SKU_ID = p.SKU_ID
GROUP BY s.SKU_ID;
"""

demand_df = pd.read_sql(query, conn)

# --------------------------------
# LOAD INVENTORY DATA
# --------------------------------

inventory_query = """
SELECT
    SKU_ID,
    SUM(Current_Stock) AS Current_Stock
FROM inventory
GROUP BY SKU_ID;
"""

inventory_df = pd.read_sql(
    inventory_query,
    conn
)

# --------------------------------
# LOAD SUPPLIER DATA
# --------------------------------

suppliers_df = pd.read_sql(
    "SELECT * FROM suppliers",
    conn
)

# --------------------------------
# MERGE DATA
# --------------------------------

merged = demand_df.merge(
    suppliers_df,
    on="Supplier"
)

merged = merged.merge(
    inventory_df,
    on="SKU_ID"
)

# --------------------------------
# INVENTORY METRICS
# --------------------------------

# Safety Stock
merged["Safety_Stock"] = (
    1.65
    * np.sqrt(merged["Lead_Time_Days"])
    * 10
)

# Reorder Point
merged["ROP"] = (
    merged["Avg_Daily_Demand"]
    * merged["Lead_Time_Days"]
) + merged["Safety_Stock"]

# EOQ Calculation
ordering_cost = 200
holding_cost = 15

merged["EOQ"] = np.sqrt(
    (
        2
        * merged["Total_Demand"]
        * ordering_cost
    )
    / holding_cost
)

# Reorder Recommendation
merged["Reorder_Required"] = (
    merged["Current_Stock"]
    < merged["ROP"]
)

# Inventory Turnover
merged["Inventory_Turnover"] = (
    merged["Total_Demand"]
    / merged["Current_Stock"]
)

# Stock Coverage
merged["Stock_Coverage_Days"] = (
    merged["Current_Stock"]
    / merged["Avg_Daily_Demand"]
)

# --------------------------------
# SAVE REPORT
# --------------------------------

merged.to_excel(
    "data/replenishment_report.xlsx",
    index=False
)

print(
    merged[
        [
            "SKU_ID",
            "Avg_Daily_Demand",
            "Current_Stock",
            "ROP",
            "EOQ",
            "Reorder_Required"
        ]
    ].head()
)

print(
    "\nReplenishment report generated successfully!"
)

conn.close()