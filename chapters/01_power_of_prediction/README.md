# Chapter 01 - The Power of Prediction in Dentistry

> Book: Machine Learning For Dentists: From Torque To Tensors

---

## Overview

This is the opening chapter. It sets the stage for everything that follows by answering:
- Why should a clinician care about prediction?
- What does "machine learning" really mean?
- How does this connect to what we already do in clinical practice?

**This chapter is the reference implementation** for all other chapters. It demonstrates the full structure: Story → Intuition → Math → Deeper Dive → Codelab → Clinical Example.

---

## Learning Objectives

By the end of this chapter, you will:

- [x] Understand that clinicians already make predictions (implicitly)
- [x] Know the difference between prediction and explanation
- [x] See that "machine learning" is just systematic prediction
- [x] Run your first notebook and compute a simple baseline
- [x] Appreciate why calibration matters (not just accuracy)

---

## Key Ideas

### Prediction vs. Explanation

| Question Type | Example | What You Need |
|---------------|---------|---------------|
| **Prediction** | "Will this implant survive 10 years?" | Good predictions, don't need to know WHY |
| **Explanation** | "Why did this implant fail?" | Understanding causes, mechanisms |

Most clinical decisions involve prediction. ML excels at prediction.

### The Prediction You Already Make

Every time you tell a patient:
- "This tooth should last another 10 years"
- "You're at high risk for peri-implantitis"
- "I recommend we extract rather than try to save it"

...you're making a prediction. ML just makes this systematic and testable.

### Why "Perfect" Isn't the Goal

- Clinical predictions are never perfect
- The goal is to be **useful**, not perfect
- A model that's 70% accurate might still help if:
  - Current clinical judgment is 60%
  - The cost of mistakes is asymmetric
  - It identifies patients who need extra attention

---

## Dataset Used

- **D2**: Toy tabular dataset
- Purpose: Focus on the *concept* of prediction, not domain complexity
- Simple enough to see the entire pipeline in one notebook

---

## Codelab: Your First ML Notebook

The notebook `01_power_of_prediction.ipynb` demonstrates:

1. **Loading data** - What does a dataset look like?
2. **Features vs. target** - What are we predicting?
3. **Train/test split** - Why we need separate data for evaluation
4. **Baseline model** - The simplest possible prediction (majority class)
5. **Computing accuracy** - How good is our baseline?
6. **The "so what?"** - Connecting metrics to clinical meaning

### How to Run

#### Google Colab (Recommended)
[Open in Colab](#) <!-- Replace with actual link when published -->

#### Local Setup
```bash
cd chapters/01_power_of_prediction
jupyter notebook 01_power_of_prediction.ipynb
```

#### Cursor
1. Open the `ml_for_dentists` folder in Cursor
2. Navigate to `chapters/01_power_of_prediction/`
3. Open `01_power_of_prediction.ipynb`
4. Use Cursor chat to ask questions about any cell

---

## Chapter Structure (Reference)

This chapter demonstrates the standard structure:

```
1. Story           → Clinical vignette that hooks the reader
2. Intuition       → Concept in plain language
3. Math (Gently)   → Minimal formulas, explained
4. Deeper Dive     → For curious readers
5. Codelab         → Hands-on notebook
6. Clinical Example → Back to clinical reality
7. Further Reading → 1-3 resources
```

All subsequent chapters follow this same pattern.

---

## Files in This Folder

| File | Purpose |
|------|---------|
| `README.md` | This file - chapter overview |
| `CHAPTER_TEXT.md` | The actual book prose |
| `01_power_of_prediction.ipynb` | Hands-on notebook |

---

## Clinical Example Preview

**The Implant Survival Question**

A patient asks: "How long will my implant last?"

What you might say:
- "Implants have a 95% survival rate at 10 years"

What you're really doing:
- Predicting this patient's outcome based on population data
- Implicitly assuming this patient is "average"

What ML can add:
- Account for this patient's specific risk factors
- Quantify uncertainty
- Identify patients who need closer follow-up

---

## Coming Up Next

**Chapter 2: Data for Clinical Questions**
- What is tabular data?
- Features, targets, and train/test splits
- Your data determines your predictions

---

## Chapter Status

- [x] README.md written
- [x] CHAPTER_TEXT.md written (template with placeholders for book prose)
- [x] Notebook created
- [x] Structure verified as reference implementation

