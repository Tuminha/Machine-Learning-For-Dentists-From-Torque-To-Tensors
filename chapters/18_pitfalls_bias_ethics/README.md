# Chapter 18 - Pitfalls, Bias, and Ethics

> Book: Machine Learning For Dentists: From Torque To Tensors

---

## Overview

This final chapter addresses what can go wrong. It covers:
- Common ML pitfalls (data leakage, overfitting)
- Survivorship bias (the Abraham Wald story)
- Fairness and bias in clinical ML
- Ethical considerations

## Learning Objectives

By the end of this chapter, you will:

- [ ] Recognize common mistakes in ML projects
- [ ] Understand survivorship bias and selection bias
- [ ] Know how bias can enter clinical models
- [ ] Consider ethical implications of ML in healthcare

## Dataset Used

- **D1**: Core tabular dental dataset
- Examples of things going wrong

## Key Concepts

| Concept | Description |
|---------|-------------|
| Data leakage | Future information contaminating training |
| Survivorship bias | Only seeing successes, not failures |
| Selection bias | Training data doesn't represent reality |
| Fairness | Model performance across subgroups |

## Clinical Relevance

Critical thinking for clinical ML:
- Why did this model fail in practice?
- Who might be harmed by this prediction?
- How do we validate before deployment?
- When should humans override the model?

## The Abraham Wald Story

During WWII, statistician Abraham Wald was asked where to add armor to bombers. The military looked at returning planes and wanted to armor the bullet holes. Wald said the opposite: armor where there are NO holes, because those hits brought down planes that never returned.

This is survivorship bias in action—and it's everywhere in clinical data.

## Codelab

The notebook `18_pitfalls_bias_ethics.ipynb` covers:

1. Creating and detecting data leakage
2. Simulating survivorship bias
3. Checking model fairness across groups
4. Documentation and model cards
5. Checklist before deployment

### How to Run

- **Colab**: [Open in Colab](#)
- **Cursor**: Open this folder → `18_pitfalls_bias_ethics.ipynb`

---

## Chapter Status

- [ ] CHAPTER_TEXT.md written
- [ ] Notebook created
- [ ] Clinical example finalized

