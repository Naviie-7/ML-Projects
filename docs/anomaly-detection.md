# Credit Card Fraud Detection

[Open the notebook](../Anomaly_Detection.ipynb)

## Objective and approach

Detect unusual transactions without using fraud examples to estimate the normal distribution. Train on 60% of legitimate transactions, divide the remaining normal transactions and fraud examples between validation and test sets, log-transform transaction amounts, and estimate an independent Gaussian distribution for each input feature.

The detector multiplies feature densities to score a transaction. A log-spaced threshold search maximizes validation F1; the selected threshold is then evaluated on the separate test split. Precision-recall plots show the tradeoff.

## Run

Install `requirements.txt`, place `creditcard.csv` at the repository root following [dataset setup](../DATASETS.md), and run the notebook from top to bottom.

## Saved results

The original saved test output reports precision **0.366**, recall **0.378**, and F1 **0.372**, with 93 true positives and 161 false positives among 254 flagged transactions. These are results from the supplied notebook, not a new run.

![Saved precision-recall tradeoff](images/anomaly-detection.png)

## Limitations and next steps

The model assumes independent Gaussian features. Multiplying many tiny densities can underflow to zero, which is visible in the saved diagnostics. Log-density scoring would improve numerical stability. A chronological split, alternative anomaly detectors, and a stronger supervised baseline would help assess generalization. The final plot loop reuses the threshold variable; rerun the threshold-selection cells before repeating evaluation.
