# Chapter 03 — Linear Regression: Predicting Numbers from Patterns

> **Book**: Machine Learning For Dentists: From Torque To Tensors

---

## 📖 Chapter Overview

Linear regression is one of the most fundamental and interpretable machine learning algorithms. In this chapter, we use it to **predict marginal bone loss (MBL)** around dental implants based on patient characteristics and surgical parameters.

### Clinical Question

> "How much bone will I lose around the implant in the first year?"

This is the question Dr. Helena Soares' patient asks — and the question linear regression helps answer.

---

## 🎯 Learning Objectives

After completing this chapter, you will be able to:

1. **Explain** what linear regression does in plain language
2. **Identify** when linear regression is (and isn't) appropriate
3. **Interpret** model weights and understand feature importance
4. **Apply** linear regression to tabular clinical data in Python
5. **Critically evaluate** the limitations of the model

---

## 📁 Files in This Folder

| File | Description |
|------|-------------|
| `CHAPTER_TEXT.md` | Full chapter text with theory, math, and clinical examples |
| `03_linear_regression.ipynb` | Hands-on codelab notebook |
| `README.md` | This file |
| `data/` | Synthetic implant dataset |
| `figures/` | Generated visualizations |

---

## 📊 Dataset

We use a **synthetic dataset** of 500 dental implant cases with:

**Features:**
- Patient demographics (age, smoking, diabetes)
- Bone characteristics (Hounsfield units)
- Surgical parameters (insertion torque, ISQ)
- Implant specifications (length, diameter)

**Target:** Marginal bone loss at 1-year follow-up (mm)

⚠️ **Note**: This is synthetic data for educational purposes only.

---

## 🚀 How to Run

### Option 1: Google Colab (Recommended)
[Open in Colab](#) *(Link to be added)*

### Option 2: Local
```bash
cd chapters/03_linear_regression
jupyter notebook 03_linear_regression.ipynb
```

### Option 3: Cursor AI
1. Open this folder in Cursor
2. Open `03_linear_regression.ipynb`
3. Ask for help with specific cells

---

## 📈 Key Concepts

### The Linear Regression Formula

$$
\hat{y} = w_1 x_1 + w_2 x_2 + ... + w_D x_D + b
$$

- **ŷ (y-hat)**: Predicted value (MBL in mm)
- **x₁, x₂, ...**: Features (torque, ISQ, HU, age)
- **w₁, w₂, ...**: Learned weights
- **b**: Bias (baseline prediction)

### What the Weights Mean

| Weight Sign | Meaning |
|-------------|---------|
| Positive | ↑ Feature → ↑ MBL |
| Negative | ↑ Feature → ↓ MBL |

### Model Evaluation

- **MSE**: Mean Squared Error (lower is better)
- **R²**: Variance explained (0-1, higher is better)

---

## 🔬 Suggested Experiments

After completing the notebook, try:

1. **Add more features**: Include `hba1c` or `implant_length_mm`
2. **Change train/test split**: What happens with 50% test data?
3. **Remove scaling**: How do weights change without StandardScaler?
4. **Subset analysis**: Train only on non-smokers

---

## 📚 Further Reading

- **Burkov, A. (2019).** *The Hundred-Page Machine Learning Book.* Chapter 3.
- **Géron, A. (2022).** *Hands-On Machine Learning with Scikit-Learn, Keras, and TensorFlow.* Chapter 4.
- **scikit-learn:** [Linear Models Documentation](https://scikit-learn.org/stable/modules/linear_model.html)

---

## ➡️ Next Chapter

**Chapter 04 — Logistic Regression**: Predicting categories (success/failure) instead of numbers!
