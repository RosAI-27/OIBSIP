"""Retail Sales EDA - OIBSIP Data Analytics Level 1, Task 1.

Environment:
    Python 3.11.5

This script reproduces the core data preparation and analytical tables used
in notebooks/01_retail_sales_eda.ipynb. Visualisations are intentionally kept
in the notebook so the analytical narrative remains easy to follow.
"""

from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "Retail_Sales.csv"
OUTPUT_PATH = ROOT / "outputs"
OUTPUT_PATH.mkdir(parents=True, exist_ok=True)

# -----------------------------------------------------------------------------
# 1. Load and prepare data
# -----------------------------------------------------------------------------
df_raw = pd.read_csv(DATA_PATH)
df = df_raw.copy()

df = df.rename(columns={"quantiy": "quantity"})
df["sale_date"] = pd.to_datetime(df["sale_date"], errors="coerce")

# Validate and reconstruct total sales only where quantity and unit price exist.
df["calculated_total_sale"] = df["quantity"] * df["price_per_unit"]
df["sales_difference"] = df["total_sale"] - df["calculated_total_sale"]
reconstructable = (
    df["total_sale"].isna()
    & df["quantity"].notna()
    & df["price_per_unit"].notna()
)
df.loc[reconstructable, "total_sale"] = df.loc[
    reconstructable, "quantity"
] * df.loc[reconstructable, "price_per_unit"]

# Derived analytical fields.
df["year"] = df["sale_date"].dt.year
df["month"] = df["sale_date"].dt.month
df["quarter"] = df["sale_date"].dt.to_period("Q").astype(str)
df["profit"] = df["total_sale"] - df["cogs"]

bins = [0, 24, 34, 44, 54, 64, np.inf]
labels = ["Under 25", "25–34", "35–44", "45–54", "55–64", "65+"]
df["age_group"] = pd.cut(df["age"], bins=bins, labels=labels)

# -----------------------------------------------------------------------------
# 2. Analytical tables
# -----------------------------------------------------------------------------
valid_sales = df.dropna(subset=["sale_date", "total_sale"])

monthly = (
    valid_sales.set_index("sale_date")
    .resample("MS")
    .agg(
        revenue=("total_sale", "sum"),
        transactions=("transactions_id", "count"),
        quantity_sold=("quantity", "sum"),
        profit=("profit", "sum"),
    )
    .reset_index()
)
monthly["average_transaction_value"] = (
    monthly["revenue"] / monthly["transactions"]
)
monthly.to_csv(OUTPUT_PATH / "monthly_sales.csv", index=False)

quarterly = (
    valid_sales.groupby("quarter")
    .agg(
        revenue=("total_sale", "sum"),
        transactions=("transactions_id", "count"),
        quantity_sold=("quantity", "sum"),
        profit=("profit", "sum"),
    )
    .reset_index()
)
quarterly.to_csv(OUTPUT_PATH / "quarterly_sales.csv", index=False)

category = (
    df.groupby("category")
    .agg(
        revenue=("total_sale", "sum"),
        transactions=("transactions_id", "count"),
        quantity_sold=("quantity", "sum"),
        average_transaction=("total_sale", "mean"),
        profit=("profit", "sum"),
    )
    .sort_values("revenue", ascending=False)
)
category["profit_margin_pct"] = category["profit"] / category["revenue"] * 100
category.to_csv(OUTPUT_PATH / "category_performance.csv")

gender = (
    df.groupby("gender")
    .agg(
        transactions=("transactions_id", "count"),
        revenue=("total_sale", "sum"),
        average_transaction=("total_sale", "mean"),
    )
    .dropna()
)
gender["revenue_share_pct"] = gender["revenue"] / gender["revenue"].sum() * 100
gender.to_csv(OUTPUT_PATH / "gender_performance.csv")

age = (
    df.dropna(subset=["age_group"])
    .groupby("age_group", observed=True)
    .agg(
        customers=("customer_id", "nunique"),
        transactions=("transactions_id", "count"),
        revenue=("total_sale", "sum"),
        average_transaction=("total_sale", "mean"),
    )
    .reset_index()
)
age.to_csv(OUTPUT_PATH / "age_group_performance.csv", index=False)

customer = (
    df.groupby("customer_id")
    .agg(
        transactions=("transactions_id", "count"),
        revenue=("total_sale", "sum"),
        average_transaction=("total_sale", "mean"),
    )
    .sort_values("revenue", ascending=False)
)
customer["cumulative_revenue_share_pct"] = (
    customer["revenue"].cumsum() / customer["revenue"].sum() * 100
)
customer.to_csv(OUTPUT_PATH / "customer_revenue_concentration.csv")

correlation_cols = [
    "age",
    "quantity",
    "price_per_unit",
    "cogs",
    "total_sale",
    "profit",
]
correlation = df[correlation_cols].corr()
correlation.to_csv(OUTPUT_PATH / "correlation_matrix.csv")

descriptive = pd.DataFrame(
    {
        "mean": df[correlation_cols].mean(),
        "median": df[correlation_cols].median(),
        "mode": df[correlation_cols].mode().iloc[0],
        "std": df[correlation_cols].std(),
    }
)
descriptive.to_csv(OUTPUT_PATH / "descriptive_statistics.csv")

# Compact KPI summary for quick portfolio review.
summary = pd.DataFrame(
    {
        "metric": [
            "transactions",
            "customers",
            "total_revenue",
            "total_profit",
            "top_20_percent_revenue_share_pct",
        ],
        "value": [
            df["transactions_id"].nunique(),
            df["customer_id"].nunique(),
            df["total_sale"].sum(),
            df["profit"].sum(),
            customer.head(max(1, int(np.ceil(len(customer) * 0.20))))["revenue"].sum()
            / customer["revenue"].sum()
            * 100,
        ],
    }
)
summary.to_csv(OUTPUT_PATH / "summary_kpis.csv", index=False)

print("Retail Sales EDA analytical outputs generated successfully.")
print(f"Transactions: {df['transactions_id'].nunique():,}")
print(f"Customers: {df['customer_id'].nunique():,}")
print(f"Revenue: ${df['total_sale'].sum():,.2f}")
print(f"Profit: ${df['profit'].sum():,.2f}")
