import sqlite3
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

conn = sqlite3.connect("inventory.db")

query = """
SELECT
    Date,
    SKU_ID,
    SUM(Units_Sold) AS Daily_Sales
FROM sales
GROUP BY Date, SKU_ID
"""

df = pd.read_sql(query, conn)

# Example SKU
sku = "SKU001"

sku_df = df[df["SKU_ID"] == sku].copy()

sku_df["Day_Number"] = np.arange(len(sku_df))

X = sku_df[["Day_Number"]]
y = sku_df["Daily_Sales"]

model = LinearRegression()

model.fit(X, y)

future_days = np.array(
    range(len(sku_df), len(sku_df) + 7)
).reshape(-1, 1)

forecast = model.predict(future_days)

forecast_df = pd.DataFrame({
    "Future_Day": range(1, 8),
    "Forecasted_Demand": forecast
})

print(forecast_df)

conn.close()