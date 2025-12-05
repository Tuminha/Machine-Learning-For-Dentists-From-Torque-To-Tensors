# Chapter 08 - Random Forests and Extra Trees

> Book: Machine Learning For Dentists: From Torque To Tensors

---

## Overview

Random Forests combine many trees for better predictions. This chapter covers:
- Why many weak learners beat one strong learner
- Bagging and feature randomness
- Out-of-bag evaluation
- Extra Trees as a faster alternative

## Learning Objectives

By the end of this chapter, you will:

- [ ] Understand the ensemble principle (wisdom of crowds)
- [ ] Know how Random Forests reduce overfitting
- [ ] Be able to interpret feature importance
- [ ] Compare Random Forests vs Extra Trees

## Dataset Used

- **D1**: Core tabular dental dataset
- Excellent for most tabular prediction tasks

## Key Concepts

| Concept | Clinical Analogy |
|---------|------------------|
| Ensemble | Consulting multiple specialists |
| Bagging | Each specialist sees different cases |
| Feature randomness | Each specialist has different expertise |
| Voting | Majority decision among specialists |
| OOB score | Cross-validation for free |

## Clinical Relevance

Random Forests are often the first serious model to try:
- Robust to outliers and noise
- Handle mixed feature types well
- Provide feature importance rankings
- Less tuning needed than single trees

## Codelab

The notebook `08_random_forests.ipynb` covers:

1. Building a Random Forest
2. Understanding n_estimators and max_features
3. Feature importance (permutation vs impurity)
4. Out-of-bag score
5. Extra Trees comparison
6. When to stop adding trees

### How to Run

- **Colab**: [Open in Colab](#)
- **Cursor**: Open this folder → `08_random_forests.ipynb`

---

## Chapter Status

- [ ] CHAPTER_TEXT.md written
- [ ] Notebook created
- [ ] Clinical example finalized

