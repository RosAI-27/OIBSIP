# Dataset

## Source
- **Platform:** Kaggle
- **Dataset:** Credit Card Fraud Detection
- **URL:** https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud

## Description
An anonymized credit-card transaction dataset containing 284,807 transactions, with a highly imbalanced fraud class. The features include anonymized principal components plus `Time`, `Amount`, and the binary `Class` target.

## Intended use
Study class imbalance, establish a legitimate baseline, compare suitable classification approaches, and evaluate fraud detection using metrics that do not hide poor minority-class performance (for example precision, recall, F1, PR-AUC, and ROC-AUC).

## Files
Download the dataset from Kaggle and place `creditcard.csv` in this directory. Raw datasets are intentionally excluded from Git via the repository `.gitignore`.

## Reproducibility
Record the dataset version/date and train/test split strategy used for the final analysis in the project README or notebook metadata.
