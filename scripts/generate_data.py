import pandas as pd
import numpy as np

np.random.seed(42)

# -------------------------------
# PRODUCTS DATA
# -------------------------------

categories = [
    "Dairy",
    "Snacks",
    "Beverages",
    "Personal Care",
    "Staples"
]

suppliers = [
    "FreshFarm",
    "QuickSupply",
    "UrbanFoods",
    "DailyNeeds",
    "MetroWholesale"
]

product_catalog = {
    "Dairy": [
        "Milk",
        "Cheese",
        "Butter",
        "Curd",
        "Paneer"
    ],

    "Snacks": [
        "Chips",
        "Biscuits",
        "Nachos",
        "Popcorn",
        "Chocolate"
    ],

    "Beverages": [
        "Cola",
        "Juice",
        "Coffee",
        "Tea",
        "Energy Drink"
    ],

    "Personal Care": [
        "Shampoo",
        "Soap",
        "Toothpaste",
        "Face Wash",
        "Body Lotion"
    ],

    "Staples": [
        "Rice",
        "Wheat Flour",
        "Sugar",
        "Salt",
        "Cooking Oil"
    ]
}

products = []

for i in range(1, 101):

    category = np.random.choice(categories)

    product = {
        "SKU_ID": f"SKU{i:03}",

        "Product_Name": np.random.choice(
            product_catalog[category]
        ),

        "Category": category,

        "Supplier": np.random.choice(suppliers),

        "Unit_Price": round(
            np.random.uniform(20, 500),
            2
        )
    }

    products.append(product)

df_products = pd.DataFrame(products)

# -------------------------------
# SUPPLIERS DATA
# -------------------------------

supplier_data = []

for supplier in suppliers:

    supplier_data.append({
        "Supplier": supplier,
        "Lead_Time_Days": np.random.randint(1, 7),
        "Reliability_Score": round(
            np.random.uniform(0.8, 0.99),
            2
        )
    })

df_suppliers = pd.DataFrame(supplier_data)

# -------------------------------
# INVENTORY DATA
# -------------------------------

warehouses = [
    "Mumbai_DC",
    "Pune_DC",
    "Bangalore_DC"
]

inventory_data = []

for _, row in df_products.iterrows():

    for warehouse in warehouses:

        inventory_data.append({
            "SKU_ID": row["SKU_ID"],
            "Warehouse": warehouse,
            "Current_Stock": np.random.randint(50, 500),
            "In_Transit": np.random.randint(0, 100)
        })

df_inventory = pd.DataFrame(inventory_data)

# -------------------------------
# SALES DATA
# -------------------------------

dates = pd.date_range(
    start="2025-01-01",
    end="2025-06-30"
)

sales_data = []

for date in dates:

    for _, row in df_products.iterrows():

        for warehouse in warehouses:

            base_demand = np.random.randint(5, 40)

            # Weekend demand spike
            if date.weekday() >= 5:
                base_demand *= 1.3

            # Summer beverage spike
            if (
                row["Category"] == "Beverages"
                and date.month in [4, 5, 6]
            ):
                base_demand *= 1.5

            # Festival spike
            if (
                date.month == 3
                and date.day in range(20, 31)
            ):
                base_demand *= 1.8

            demand = max(
                0,
                int(np.random.normal(base_demand, 5))
            )

            sales_data.append({
                "Date": date,
                "SKU_ID": row["SKU_ID"],
                "Warehouse": warehouse,
                "Units_Sold": demand
            })

df_sales = pd.DataFrame(sales_data)

# -------------------------------
# SAVE FILES
# -------------------------------

df_products.to_csv(
    "data/products.csv",
    index=False
)

df_suppliers.to_csv(
    "data/suppliers.csv",
    index=False
)

df_inventory.to_csv(
    "data/inventory.csv",
    index=False
)

df_sales.to_csv(
    "data/sales.csv",
    index=False
)

print("Synthetic datasets generated successfully!")