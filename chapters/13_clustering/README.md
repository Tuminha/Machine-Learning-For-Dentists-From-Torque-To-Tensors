# Chapter 13 - Clustering

> Book: Machine Learning For Dentists: From Torque To Tensors

---

## Overview

Clustering finds natural groups in data without labels. This chapter covers:
- Unsupervised learning: no target variable
- k-Means clustering
- Hierarchical clustering
- Evaluating cluster quality

## Learning Objectives

By the end of this chapter, you will:

- [ ] Understand the difference between supervised and unsupervised learning
- [ ] Know how k-Means finds clusters
- [ ] Be able to choose the number of clusters
- [ ] Interpret clustering results clinically

## Dataset Used

- **D1**: Core tabular dental dataset (without using the target)
- Discover patient subgroups

## Key Concepts

| Concept | Clinical Analogy |
|---------|------------------|
| Cluster | Natural patient subgroup |
| Centroid | Typical patient in each group |
| Inertia | How tight/compact clusters are |
| Silhouette | How well-separated clusters are |

## Clinical Relevance

Clustering helps with:
- Patient stratification (finding risk groups)
- Discovering treatment response patterns
- Identifying unusual patient profiles
- Hypothesis generation for further research

## Codelab

The notebook `13_clustering.ipynb` covers:

1. k-Means clustering basics
2. Choosing k (elbow method, silhouette)
3. Visualizing clusters in 2D
4. Hierarchical clustering and dendrograms
5. Interpreting cluster profiles

### How to Run

- **Colab**: [Open in Colab](#)
- **Cursor**: Open this folder → `13_clustering.ipynb`

---

## Chapter Status

- [ ] CHAPTER_TEXT.md written
- [ ] Notebook created
- [ ] Clinical example finalized

