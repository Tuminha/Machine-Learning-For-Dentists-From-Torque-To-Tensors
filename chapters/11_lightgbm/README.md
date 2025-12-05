# Chapter 11 - LightGBM

> Book: Machine Learning For Dentists: From Torque To Tensors

---

## Overview

LightGBM offers speed and efficiency for large datasets. This chapter covers:
- Leaf-wise tree growth (vs level-wise)
- Gradient-based one-side sampling (GOSS)
- Exclusive feature bundling
- When to choose LightGBM over XGBoost

## Learning Objectives

By the end of this chapter, you will:

- [ ] Understand leaf-wise vs level-wise growth
- [ ] Know when LightGBM is the better choice
- [ ] Be able to set up and tune LightGBM
- [ ] Compare performance with XGBoost

## Dataset Used

- **D1**: Core tabular dental dataset
- Particularly shines with larger datasets

## Key Concepts

| Concept | Description |
|---------|-------------|
| Leaf-wise growth | Grow the leaf with max delta loss |
| GOSS | Focus on samples with large gradients |
| EFB | Bundle sparse features together |
| Categorical handling | Native support (no encoding needed) |

## Clinical Relevance

LightGBM is excellent when:
- You have larger datasets (thousands+ rows)
- Training speed matters
- You have many categorical features
- Memory is a constraint

## Codelab

The notebook `11_lightgbm.ipynb` covers:

1. Installing and importing LightGBM
2. Basic training workflow
3. Categorical feature handling
4. Key hyperparameters
5. Speed comparison with XGBoost
6. Early stopping and callbacks

### How to Run

- **Colab**: [Open in Colab](#)
- **Cursor**: Open this folder → `11_lightgbm.ipynb`

---

## Chapter Status

- [ ] CHAPTER_TEXT.md written
- [ ] Notebook created
- [ ] Clinical example finalized

