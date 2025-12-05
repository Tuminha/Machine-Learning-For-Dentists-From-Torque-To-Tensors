# Chapter 03 - Linear Regression

> Book: Machine Learning For Dentists: From Torque To Tensors

---

## Overview

Linear regression is the foundation of predictive modeling. This chapter introduces:
- Predicting continuous outcomes (e.g., probing depth, bone loss percentage)
- Understanding the relationship between features and outcomes
- Interpreting coefficients in clinical terms

## Learning Objectives

By the end of this chapter, you will:

- [ ] Understand what linear regression does and when to use it
- [ ] Be able to interpret regression coefficients
- [ ] Know how to evaluate regression models (R², MSE, MAE)
- [ ] Recognize when linear regression is inappropriate

## Dataset Used

- **D1**: Core tabular dental dataset
- Target: A continuous outcome (e.g., probing depth, attachment loss)

## Key Concepts

| Concept | Description |
|---------|-------------|
| Slope (β) | How much Y changes when X increases by 1 |
| Intercept | Baseline value when all features are 0 |
| R² | Proportion of variance explained |
| Residuals | Difference between predicted and actual |

## Clinical Relevance

Linear regression can help answer questions like:
- "How much does smoking affect attachment loss?"
- "What's the expected bone loss given patient characteristics?"
- "Which factors contribute most to disease progression?"

## Codelab

The notebook `03_linear_regression.ipynb` covers:

1. Simple linear regression (one feature)
2. Multiple linear regression (many features)
3. Interpreting coefficients
4. Model evaluation metrics

### How to Run

- **Colab**: [Open in Colab](#)
- **Cursor**: Open this folder → `03_linear_regression.ipynb`

---

## Chapter Status

- [ ] CHAPTER_TEXT.md written
- [ ] Notebook created
- [ ] Clinical example finalized

