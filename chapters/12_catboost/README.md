# Chapter 12 - CatBoost

> Book: Machine Learning For Dentists: From Torque To Tensors

---

## Overview

CatBoost handles categorical features natively and prevents target leakage. This chapter covers:
- Ordered boosting to prevent overfitting
- Native categorical feature handling
- Symmetric trees for speed
- Why CatBoost often wins on clinical data

## Learning Objectives

By the end of this chapter, you will:

- [ ] Understand CatBoost's unique approach to categoricals
- [ ] Know what ordered boosting means
- [ ] Be able to use CatBoost without preprocessing categoricals
- [ ] Compare CatBoost with XGBoost and LightGBM

## Dataset Used

- **D1**: Core tabular dental dataset
- CatBoost excels with mixed numerical/categorical features

## Key Concepts

| Concept | Description |
|---------|-------------|
| Ordered boosting | Uses permutation to prevent target leakage |
| Target encoding | Encodes categoricals using target statistics |
| Symmetric trees | All leaves at same depth (faster) |
| Cat features | Pass categorical columns directly |

## Clinical Relevance

CatBoost is often the best choice for clinical data because:
- Clinical data has many categorical features (diagnosis codes, medications, etc.)
- No need for manual encoding (less preprocessing)
- Robust out-of-the-box performance
- Often requires minimal tuning

## Codelab

The notebook `12_catboost.ipynb` covers:

1. Installing and importing CatBoost
2. Specifying categorical features
3. Training without encoding
4. Key hyperparameters
5. Comparison with XGBoost and LightGBM
6. Visualization and interpretation

### How to Run

- **Colab**: [Open in Colab](#)
- **Cursor**: Open this folder → `12_catboost.ipynb`

---

## Chapter Status

- [ ] CHAPTER_TEXT.md written
- [ ] Notebook created
- [ ] Clinical example finalized

