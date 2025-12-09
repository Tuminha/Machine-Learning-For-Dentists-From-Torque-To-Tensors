# Chapter 04 — Logistic Regression: When the Answer is Yes or No

> **Book**: Machine Learning For Dentists: From Torque To Tensors

---

## Overview

This chapter introduces **logistic regression** — the go-to method for binary classification in medicine. While linear regression predicts continuous numbers (Chapter 03), logistic regression predicts probabilities for categorical outcomes: success vs. failure, disease vs. healthy, yes vs. no.

**Clinical scenario:** Dr. Marco Ferreira wants to know the *probability* of implant success before deciding on immediate loading — a fundamentally different question than predicting bone loss in millimeters.

---

## Learning Objectives

After completing this chapter, you will be able to:

1. **Explain** how logistic regression transforms a linear score into a probability using the sigmoid function
2. **Identify** when to use logistic regression vs. linear regression
3. **Interpret** model outputs: probabilities, odds ratios, and feature importance
4. **Choose** appropriate decision thresholds based on clinical costs
5. **Recognize** common pitfalls: class imbalance, complete separation, multicollinearity

---

## Files in This Folder

| File | Description |
|------|-------------|
| `CHAPTER_TEXT.md` | Complete chapter content with theory and clinical context |
| `04_logistic_regression.ipynb` | Hands-on codelab with synthetic data |
| `README.md` | This file |
| `data/` | Synthetic implant success/failure dataset |
| `figures/` | Generated visualizations from the codelab |

---

## The Codelab

The Jupyter notebook walks you through:

1. **Data Exploration** — Class distribution, feature relationships
2. **The Sigmoid Function** — Visualizing the transformation
3. **Model Training** — Using scikit-learn's LogisticRegression
4. **Odds Ratios** — Converting weights to clinical interpretations
5. **Threshold Analysis** — Precision vs. recall tradeoffs
6. **Model Evaluation** — ROC curve, AUC, confusion matrix
7. **Residual Analysis** — Checking model assumptions

---

## Key Figures Generated

| Figure | What It Shows |
|--------|---------------|
| `01_class_distribution.png` | Balance between success/failure cases |
| `02_sigmoid_function.png` | The sigmoid transformation visualized |
| `03_odds_ratios.png` | Feature importance as odds ratios |
| `04_roc_curve.png` | Model discrimination (AUC) |
| `05_threshold_analysis.png` | Precision-recall tradeoffs |
| `06_confusion_matrix.png` | Classification performance |

---

## Key Takeaways

1. **Same weighted sum, different final step** — Linear score then sigmoid then probability
2. **Outputs probabilities, not just labels** — Much more useful clinically
3. **Weights to Odds Ratios** — Each exp(w) tells you the multiplicative effect on odds
4. **Threshold is a clinical decision** — 0.5 is not always optimal
5. **Class imbalance matters** — Do not trust accuracy alone

---

## Prerequisites

Complete **Chapter 03 (Linear Regression)** first. The concepts build directly on that foundation:
- Feature scaling
- Train/test splits
- Gradient-based optimization
- Model evaluation

---

## Next Chapter

**Chapter 05 — Decision Trees** — A completely different approach that learns if-then rules, mirroring clinical reasoning.

---

## Further Reading

- Hosmer and Lemeshow (2013). *Applied Logistic Regression*
- Geron (2022). *Hands-On Machine Learning*, Chapter 4
- Steyerberg (2019). *Clinical Prediction Models*
- scikit-learn: Logistic Regression documentation

---

*Questions or feedback? Open an issue on GitHub or reach out on Twitter @cisco_research*
