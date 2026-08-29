# Retail Sales — Exploratory Data Analysis

OASIS Infobyte Data Analytics — Level 1, Task 1.

## Objective
Perform exploratory data analysis on retail sales data to uncover sales trends, customer behaviour, category performance, and actionable business insights.

## Environment
- Python 3.11.5
- pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

## Project Structure

```text
DataAnalytics-L1-EDARetail/
├── data/Retail_Sales.csv
├── notebooks/01_retail_sales_eda.ipynb
├── outputs/
│   ├── visualizations/
│   ├── descriptive_statistics.csv
│   ├── monthly_sales.csv
│   ├── quarterly_sales.csv
│   ├── category_performance.csv
│   ├── gender_performance.csv
│   ├── age_group_performance.csv
│   ├── customer_revenue_concentration.csv
│   ├── correlation_matrix.csv
│   └── summary_kpis.csv
├── src/retail_sales_eda.py
└── README.md
```

## Analysis Covered
- Initial inspection and data-quality checks
- Missing-value assessment and sales validation
- Descriptive statistics
- Monthly and quarterly sales trends
- Category revenue, volume, average transaction value and profit margin
- Gender and age-group analysis
- Customer revenue concentration
- Correlation analysis and heatmap
- Bivariate relationships
- Additional high-revenue-period analysis
- Findings, recommendations and limitations

## Key Findings
- Q4 is the strongest revenue quarter in both observed years, although Q4 revenue declined year over year.
- Category leadership depends on the KPI: Electronics leads revenue, Clothing leads transaction volume, while Beauty leads average transaction value and profit margin.
- The top 20% of customers account for 44.74% of revenue, so the dataset does not show a classic 80/20 revenue distribution.
- Correlations involving total sales and profit are partly structural because total sales is derived from quantity and unit price, and profit is derived from sales minus COGS.

## Dataset Limitation
The dataset contains category information but no individual product identifier/name. Therefore, a true Top-10-products ranking cannot be produced without inventing information.

## Reproducibility
The notebook uses `../data/Retail_Sales.csv` and exports charts to `outputs/visualizations/`. The companion script reproduces the core analytical tables and writes CSV outputs to `outputs/`.
