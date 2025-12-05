# Chapter 01 - The Power of Prediction in Dentistry

> Book: Machine Learning For Dentists: From Torque To Tensors

---

## 1. Story

*[Placeholder - To be written in ChatGPT and pasted here]*

**Draft prompt for ChatGPT:**

> Write a 2-3 paragraph clinical vignette for the opening of a chapter about prediction in dentistry. 
> The story should feature a periodontist facing a clinical decision where prediction (even implicit prediction) 
> is central. Perhaps a patient asking about implant prognosis, or a decision about whether to extract or 
> try to save a tooth. The tone should be warm, relatable, and show that clinicians already make predictions 
> every day—they just don't call it that.

**Example structure:**

> Dr. [Name] studied the radiograph. The patient, a 58-year-old with controlled diabetes, had asked the question 
> every implant patient asks: "How long will it last?"
> 
> The honest answer was: "I don't know for certain." But that's not what patients want to hear, and it's not 
> entirely true either. Dr. [Name] knew, based on years of training and experience, that certain factors mattered: 
> smoking history, bone quality, glycemic control, oral hygiene habits...
> 
> What Dr. [Name] was doing—without calling it that—was making a prediction.

---

## 2. Intuition

*[Placeholder - To be written in ChatGPT and pasted here]*

### What is Prediction?

Prediction is using what we know to estimate what we don't know.

- **In clinical terms:** Using patient information to estimate future outcomes
- **In ML terms:** Using features (X) to estimate a target (y)

### Clinicians Already Predict

Every prognosis, every risk assessment, every treatment recommendation involves prediction:

| Clinical Action | The Prediction |
|-----------------|----------------|
| "This tooth needs extraction" | It won't survive long-term |
| "You're high risk for perio" | Disease will progress without intervention |
| "Let's watch this lesion" | It's unlikely to cause problems soon |

### Why Systematize This?

- **Consistency:** Different clinicians, same patient → same prediction
- **Transparency:** Know exactly what factors drove the prediction
- **Improvement:** Test and improve predictions over time
- **Communication:** Share predictions across clinicians and with patients

---

## 3. Math (Gently)

*[Placeholder - To be refined in ChatGPT]*

### The Simplest Prediction: Majority Class

If 70% of patients in your clinic have good outcomes, the simplest prediction is:

> "Predict good outcome for everyone"

This gives you 70% accuracy... without looking at any patient features!

**Mathematical notation:**

$$
\hat{y} = \text{mode}(y_{\text{train}})
$$

Where:
- $\hat{y}$ = predicted outcome (y-hat)
- $y_{\text{train}}$ = outcomes in training data
- $\text{mode}$ = most common value

### Why This Matters

The baseline tells us: **How hard is this problem?**

- If baseline is 95%: The problem might be too easy (or data is imbalanced)
- If baseline is 50%: Random guessing; our model needs to do much better
- If baseline is 70%: We have room to improve, but not infinitely

### Accuracy Formula

$$
\text{Accuracy} = \frac{\text{Correct Predictions}}{\text{Total Predictions}}
$$

**Clinical translation:** Out of 100 patients, how many did we classify correctly?

---

## 4. Deeper Dive

*[Placeholder - To be written in ChatGPT]*

### Prediction vs. Explanation

These are different goals:

| | Prediction | Explanation |
|---|------------|-------------|
| **Question** | What will happen? | Why did it happen? |
| **Goal** | Accuracy | Understanding |
| **Complexity OK?** | Yes, if it predicts well | No, need interpretable |
| **Example** | "Will this implant fail?" | "Why did this implant fail?" |

ML is primarily a **prediction** tool. Sometimes explanation follows, but prediction comes first.

### Why Perfect Prediction is Impossible

Clinical outcomes depend on factors we can't measure:
- Patient compliance (actual, not reported)
- Random biological variation
- Future events (trauma, other diseases)
- Measurement error

The goal isn't perfection—it's **useful improvement** over current practice.

### Calibration: Beyond Accuracy

A model that says "80% risk" should be correct about 80% of the time among patients with that prediction.

This is **calibration**, and it's often more important than accuracy for clinical decisions.

---

## 5. Codelab Summary

*[This section describes what the notebook covers]*

### Notebook: `01_power_of_prediction.ipynb`

**What you'll do:**

1. **Load a simple dataset** - See what tabular data looks like
2. **Identify features and target** - What are we predicting?
3. **Split into train/test** - Why we need separate evaluation data
4. **Create a baseline model** - Predict the majority class
5. **Calculate accuracy** - How good is the baseline?
6. **Reflect** - What does this mean clinically?

**Key takeaway:** Before trying fancy algorithms, always establish a baseline. If your complex model can't beat "predict the most common class," something is wrong.

### Suggested Experiments

After running the notebook:

1. **Change the test size:** What happens to accuracy if you use 50% for testing instead of 20%?
2. **Check class balance:** What percentage of your data is each class?
3. **Think clinically:** If this were real patient data, what would a 70% accuracy baseline mean?

---

## 6. Clinical Example

*[Placeholder - To be expanded in ChatGPT]*

### Predicting 5-Year Implant Survival

**Scenario:**

A periodontist wants to identify patients at higher risk of implant failure before placement. Using data from 500 previous implant cases, they want to build a simple risk model.

**What we have:**
- Patient demographics (age, sex, smoking)
- Medical history (diabetes, medications)
- Dental history (periodontitis, bone quality)
- Outcome: Did the implant survive 5 years? (Yes/No)

**The baseline:**
- 92% of implants in the dataset survived 5 years
- So the baseline prediction is: "Predict survival for everyone"
- Baseline accuracy: 92%

**The challenge:**
- 92% sounds great, but we're missing ALL the failures
- The 8% who fail are the ones we need to identify
- Accuracy alone is misleading when classes are imbalanced

**Lesson:** Always look beyond accuracy. In clinical ML, what you predict wrong often matters more than what you predict right.

---

## 7. Further Reading

### For Conceptual Understanding

1. **Statistical Rethinking by Richard McElreath** - Chapter 1 on statistical thinking (not dentistry-specific, but excellent foundation)

2. **"Why Most Published Research Findings Are False" by John Ioannidis** - Understanding prediction and validation in medical research

### For Dental/Clinical ML

3. **Artz et al. (2023)** - "Machine Learning in Periodontology: A Systematic Review" - Overview of ML applications in your field

### Quick Intro

4. **StatQuest on YouTube** - "Machine Learning Fundamentals" playlist - Visual, beginner-friendly explanations

---

## Notes for Author

*[Remove this section before publishing]*

### Status
- [ ] Story: Draft needed from ChatGPT
- [ ] Intuition: Skeleton complete, needs refinement
- [ ] Math: Basic formulas in place
- [ ] Deeper Dive: Skeleton complete
- [ ] Codelab: Notebook created
- [ ] Clinical Example: Placeholder complete
- [ ] Further Reading: Needs real citations

### Questions to Resolve
- Specific clinical vignette details
- Real references vs. placeholder
- Level of math detail appropriate for audience

