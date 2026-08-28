# OIBSIP — Data Analytics Portfolio

![Status](https://img.shields.io/badge/status-in%20progress-orange)
![Track](https://img.shields.io/badge/track-Data%20Analytics-blue)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-F37626?logo=jupyter&logoColor=white)

A structured portfolio of **Data Analytics projects completed for the OASIS Infobyte internship program**.

The goal of this repository is not simply to collect notebooks, but to demonstrate a repeatable analytics workflow: **understand the problem → inspect and clean the data → explore patterns → quantify findings → communicate insights → recommend actions**.

## 📊 Projects

### Level 1 — Foundations

| Project | Focus | Status |
|---|---|---|
| [EDA on Retail Sales Data](DataAnalytics-L1-EDARetail/) | Exploratory analysis, trends, customer & product insights | 🟡 Planned |
| [Customer Segmentation](DataAnalytics-L1-Segmentation/) | RFM analysis and K-Means clustering | 🟡 Planned |
| [Data Cleaning](DataAnalytics-L1-DataCleaning/) | Data quality assessment and transformation | 🟡 Planned |
| [Sentiment Analysis](DataAnalytics-L1-Sentiment/) | Text preprocessing, TF-IDF and classification | 🟡 Planned |

### Level 2 — Applied Analytics

| Project | Focus | Status |
|---|---|---|
| [House Prices](DataAnalytics-L2-HousePrices/) | Regression and model interpretation | 🟡 Planned |
| [Wine Quality](DataAnalytics-L2-WineQuality/) | Classification and feature importance | 🟡 Planned |
| [Fraud Detection](DataAnalytics-L2-FraudDetection/) | Imbalanced classification and evaluation | 🟡 Planned |
| [Google Play Store Analysis](DataAnalytics-L2-PlayStore/) | App-market analysis and customer review insights | 🟡 Planned |

For the detailed checklist and progress tracker, see [PROJECT_STATUS.md](PROJECT_STATUS.md).

## 🧰 Toolkit

- **Python:** pandas, NumPy, scikit-learn
- **Visualisation:** matplotlib, seaborn
- **Environment:** Jupyter Notebook
- **Version control:** Git & GitHub
- **Analytics:** EDA, statistical summaries, segmentation, NLP, regression, classification

## 📁 Standard Project Structure

Each project follows the same layout so that reviewers can quickly find the work:

```text
DataAnalytics-LX-Project/
├── data/          # Local datasets; large files are intentionally gitignored
├── notebooks/     # Main Jupyter notebooks
├── outputs/       # Selected charts, tables and exported results
├── src/           # Reusable project-specific code
└── README.md      # Problem, methodology, findings and recommendations
```

## 🔬 Approach

Every completed project should document:

1. **Problem & objective** — what question are we answering?
2. **Data understanding** — structure, types, missingness and quality.
3. **Cleaning & preparation** — transformations and the reasoning behind them.
4. **Exploratory analysis** — relevant statistics and visualisations.
5. **Modelling**, when required — baseline, alternatives and evaluation.
6. **Interpretation** — what the results actually mean.
7. **Recommendations** — actionable conclusions rather than chart descriptions.
8. **Limitations** — important caveats and assumptions.

## 📌 Data & Reproducibility

Datasets are **not automatically committed to this repository**. Large files, archives, credentials and environment-specific files are excluded through `.gitignore`.

Each finished project will document its dataset source and the steps required to reproduce the analysis.

## 🎯 Internship Context

This repository follows the Data Analytics task framework supplied for the OASIS Infobyte internship. The selected projects are organised across Level 1 and Level 2 to build breadth while preserving a consistent, reviewable workflow.

## 👤 Author

**RosAI-27**  
Data Science student | Data Analytics & AI

---

> **Portfolio principle:** a polished notebook is useful; a clearly explained analytical decision is better.
