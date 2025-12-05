# Chapter 05 - k-Nearest Neighbors

> Book: Machine Learning For Dentists: From Torque To Tensors

---

## Overview

k-Nearest Neighbors (kNN) is one of the simplest and most intuitive algorithms. This chapter covers:
- Classification by similarity
- The importance of feature scaling
- Choosing the right k
- When kNN works well and when it doesn't

## Learning Objectives

By the end of this chapter, you will:

- [ ] Understand how kNN makes predictions
- [ ] Know why feature scaling is essential
- [ ] Be able to choose an appropriate k value
- [ ] Recognize the curse of dimensionality

## Dataset Used

- **D1**: Core tabular dental dataset
- Can use either classification or regression tasks

## Key Concepts

| Concept | Clinical Analogy |
|---------|------------------|
| k neighbors | Looking at similar past patients |
| Distance | How similar two patients are |
| Voting | Majority decision among similar cases |
| Feature scaling | Making measurements comparable |

## Clinical Relevance

kNN is intuitive for clinicians because it mirrors clinical reasoning:
- "This patient looks like these 5 previous patients..."
- "4 out of 5 similar patients had good outcomes..."
- Case-based reasoning we already do mentally

## Codelab

The notebook `05_knn.ipynb` covers:

1. Understanding distance metrics
2. The importance of scaling
3. Choosing k (odd vs. even, small vs. large)
4. Visualization of decision boundaries
5. When kNN struggles (high dimensions)

### How to Run

- **Colab**: [Open in Colab](#)
- **Cursor**: Open this folder → `05_knn.ipynb`

---

## Chapter Status

- [ ] CHAPTER_TEXT.md written
- [ ] Notebook created
- [ ] Clinical example finalized

