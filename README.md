# Inventory Replenishment & Demand Forecasting System

A data-driven inventory planning and replenishment optimization system simulating quick-commerce warehouse operations using Python, SQLite, SQL, Excel, and Power BI.

## Features

- Demand forecasting across multiple SKUs
- Inventory replenishment optimization
- Reorder Point (ROP) calculation
- Economic Order Quantity (EOQ) optimization
- Safety Stock estimation
- SQL-based operational analytics
- KPI tracking and inventory reporting
- Automated replenishment recommendation logic
- Excel-based operational reporting

---

## Tech Stack

- Python
- SQLite
- SQL
- pandas
- NumPy
- Excel
- Power BI

---

## KPIs Tracked

- Inventory Turnover
- Fill Rate
- Stock Coverage
- Stockout Risk
- Replenishment Performance

---

## Project Structure

```text
inventory_project/
│
├── data/
│   ├── products.csv
│   ├── sales.csv
│   ├── inventory.csv
│   ├── suppliers.csv
│   └── replenishment_report.xlsx
│
├── scripts/
│   ├── generate_data.py
│   ├── create_database.py
│   ├── inventory_analysis.py
│   └── forecasting.py
│
├── dashboards/
│
├── inventory.db
│
├── requirements.txt
│
├── README.md
│
└── .gitignore
```

---

## Setup Instructions

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Pipeline

### 1. Generate Data

```bash
python scripts/generate_data.py
```

### 2. Create SQLite Database

```bash
python scripts/create_database.py
```

### 3. Run Inventory Analytics

```bash
python scripts/inventory_analysis.py
```

### 4. Run Forecasting Module

```bash
python scripts/forecasting.py
```

---

## Analytics & Optimization Modules

### Demand Forecasting
- Demand trend analysis
- Consumption pattern tracking
- SKU-level forecasting

### Inventory Optimization
- Reorder Point (ROP)
- Economic Order Quantity (EOQ)
- Safety Stock calculation

### KPI Monitoring
- Inventory turnover
- Fill rate
- Stock coverage
- Stockout risk

### Replenishment Recommendation Engine
- Automated reorder recommendation logic
- Inventory planning support
- Operational reporting

---

## Future Improvements

- Power BI dashboards
- Streamlit frontend
- Advanced forecasting models
- Multi-city warehouse optimization
- Supplier reliability analytics
- Real-time inventory alerts
