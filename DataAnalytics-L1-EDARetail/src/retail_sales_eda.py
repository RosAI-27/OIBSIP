"""Retail Sales EDA - OIBSIP Data Analytics Level 1 Task 1.

Python 3.11.15
The script reproduces the core transformations, KPIs and analytical tables
used in notebooks/01_retail_sales_eda.ipynb.
"""
from pathlib import Path
import pandas as pd
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "Retail_Sales.csv"
OUTPUT_PATH = ROOT / "outputs"
OUTPUT_PATH.mkdir(exist_ok=True)

# Load and preserve the raw data.
df_raw = pd.read_csv(DATA_PATH)
df = df_raw.copy()
df = df.rename(columns={"quantiy": "quantity"})
df["sale_date"] = pd.to_datetime(df["sale_date"], errors="coerce")

# Derived fields.
df["year"] = df["sale_date"].dt.year
df["month"] = df["sale_date"].dt.month
df["quarter"] = df["sale_date"].dt.to_period("Q").astype(str)
df["profit"] = df["total_sale"] - df["cogs"]

bins = [0, 24, 34, 44, 54, 64, np.inf]
labels = ["Under 25", "25–34", "35–44", "45–54", "55–64", "65+"]
df["age_group"] = pd.cut(df["age"], bins=bins, labels=labels)

# Monthly KPIs.
monthly = (df.dropna(subset=["sale_date", "total_sale"])
           .set_index("sale_date")
           .resample("MS")
           .agg(revenue=("total_sale", "sum"),
                transactions=("transactions_id", "count"),
                quantity_sold=("quantity", "sum"),
                profit=("profit", "sum"))
           .reset_index())
monthly["average_transaction_value"] = monthly["revenue"] / monthly["transactions"]
monthly.to_csv(OUTPUT_PATH / "monthly_sales.csv", index=False)

# Quarterly KPIs.
quarterly = (df.dropna(subset=["sale_date", "total_sale"])
             .groupby("quarter")
             .agg(revenue=("total_sale", "sum"),
                  transactions=("transactions_id", "count"),
                  quantity_sold=("quantity", "sum"),
                  profit=("profit", "sum"))
             .reset_index())
quarterly.to_csv(OUTPUT_PATH / "quarterly_sales.csv", index=False)

# Category performance.
category = (df.groupby("category")
            .agg(revenue=("total_sale", "sum"),
                 transactions=("transactions_id", "count"),
                 quantity_sold=("quantity", "sum"),
                 average_transaction=("total_sale", "mean"),
                 profit=("profit", "sum"))
            .sort_values("revenue", ascending=False))
category["profit_margin_pct"] = category["profit"] / category["revenue"] * 100
category.to_csv(OUTPUT_PATH / "category_performance.csv")

# Gender performance.
gender = (df.groupby("gender")
          .agg(transactions=("transactions_id", "count"),
               revenue=("total_sale", "sum"),
               average_transaction=("total_sale", "mean")))
gender["revenue_share_pct"] = gender["revenue"] / gender["revenue"].sum() * 100
gender.to_csv(OUTPUT_PATH / "gender_performance.csv")

# Age-group performance.
age = (df.dropna(subset=["age_group"])
       .groupby("age_group", observed=True)
       .agg(customers=("customer_id", "nunique"),
            transactions=("transactions_id", "count"),
            revenue=("total_sale", "sum"),
            average_transaction=("total_sale", "mean"))
       .reset_index())
age.to_csv(OUTPUT_PATH / "age_group_performance.csv", index=False)

# Customer concentration.
customer = (df.groupby("customer_id")
            .agg(transactions=("transactions_id", "count"),
                 revenue=("total_sale", "sum"),
                 average_transaction=("total_sale", "mean"))
            .sort_values("revenue", ascending=False))
customer["cumulative_revenue_share_pct"] = customer["revenue"].cumsum() / customer["revenue"].sum() * 100
customer.to_csv(OUTPUT_PATH / "customer_revenue_concentration.csv")

# Correlations.
correlation_cols = ["age", "quantity", "price_per_unit", "cogs", "total_sale", "profit"]
df[correlation_cols].corr().to_csv(OUTPUT_PATH / "correlation_matrix.csv")

# Descriptive statistics.
descriptive = pd.DataFrame({
    "mean": df[correlation_cols].mean(),
    "median": df[correlation_cols].median(),
    "mode": df[correlation_cols].mode().iloc[0],
    "std": df[correlation_cols].std(),
})
descriptive.to_csv(OUTPUT_PATH / "descriptive_statistics.csv")

print("Retail Sales EDA outputs generated successfully.")
print(f"Transactions: {df['transactions_id'].nunique():,}")
print(f"Customers: {df['customer_id'].nunique():,}")
print(f"Revenue: ${df['total_sale'].sum():,.2f}")
print(f"Profit: ${df['profit'].sum():,.2f}")
