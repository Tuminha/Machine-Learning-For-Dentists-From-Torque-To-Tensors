# Chapter 06 - Naive Bayes

> Book: Machine Learning For Dentists: From Torque To Tensors

---

## Overview

Naive Bayes brings probability theory to classification. This chapter covers:
- Bayes' theorem in plain language
- Why "naive" isn't always bad
- When Naive Bayes excels
- Connections to clinical probability reasoning

## Learning Objectives

By the end of this chapter, you will:

- [ ] Understand Bayes' theorem intuitively
- [ ] Know what the "naive" assumption means
- [ ] Be able to apply Naive Bayes to classification
- [ ] Connect probabilistic thinking to clinical diagnosis

## Dataset Used

- **D1**: Core tabular dental dataset
- Works well with categorical features

## Key Concepts

| Concept | Clinical Analogy |
|---------|------------------|
| Prior probability | Base rate of disease in population |
| Likelihood | How often we see this symptom given disease |
| Posterior | Updated probability after seeing evidence |
| Independence | Assuming symptoms don't interact (naive) |

## Clinical Relevance

Bayesian thinking is fundamental to clinical diagnosis:
- "Given these symptoms, what's the probability of this diagnosis?"
- Pre-test probability → Test result → Post-test probability
- Naive Bayes makes this formal and computational

## Codelab

The notebook `06_naive_bayes.ipynb` covers:

1. Bayes' theorem step by step
2. Gaussian vs. Categorical Naive Bayes
3. When independence assumption breaks
4. Comparison with logistic regression
5. Probabilistic outputs and calibration

### How to Run

- **Colab**: [Open in Colab](#)
- **Cursor**: Open this folder → `06_naive_bayes.ipynb`

---

## Chapter Status

- [ ] CHAPTER_TEXT.md written
- [ ] Notebook created
- [ ] Clinical example finalized

