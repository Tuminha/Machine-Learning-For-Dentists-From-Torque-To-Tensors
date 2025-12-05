# Chapter 04 - Logistic Regression

> Book: Machine Learning For Dentists: From Torque To Tensors

---

## Overview

Logistic regression is the workhorse of binary classification in medicine. This chapter covers:
- Predicting binary outcomes (disease/no disease, success/failure)
- Understanding probability outputs
- Choosing classification thresholds
- Clinical interpretation of odds ratios

## Learning Objectives

By the end of this chapter, you will:

- [ ] Understand how logistic regression differs from linear regression
- [ ] Be able to interpret odds ratios and log-odds
- [ ] Know how to choose and evaluate classification thresholds
- [ ] Evaluate models using accuracy, precision, recall, and AUC

## Dataset Used

- **D1**: Core tabular dental dataset
- Target: Binary outcome (e.g., periodontitis yes/no, implant failure yes/no)

## Key Concepts

| Concept | Clinical Analogy |
|---------|------------------|
| Probability | Likelihood of disease (0-100%) |
| Odds ratio | How much risk increases with a factor |
| Threshold | Cutoff for classifying as positive |
| Sensitivity | Catching all true cases |
| Specificity | Avoiding false alarms |

## Clinical Relevance

Logistic regression answers questions like:
- "What's the probability this patient develops periodontitis?"
- "How much does diabetes increase implant failure risk?"
- "Which patients should receive intensive follow-up?"

## Codelab

The notebook `04_logistic_regression.ipynb` covers:

1. Binary classification basics
2. Probability outputs and thresholds
3. Confusion matrix interpretation
4. ROC curves and AUC
5. Odds ratio interpretation

### How to Run

- **Colab**: [Open in Colab](#)
- **Cursor**: Open this folder → `04_logistic_regression.ipynb`

---

## Chapter Status

- [ ] CHAPTER_TEXT.md written
- [ ] Notebook created
- [ ] Clinical example finalized

