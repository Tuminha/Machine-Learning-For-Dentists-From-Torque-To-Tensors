# Chapter 18 - Pitfalls, Bias, and Ethics

> Book: Machine Learning For Dentists: From Torque To Tensors

---

## 1. Story

*[To be written - clinical vignette about a model that failed in practice]*

---

## 2. Intuition

*[To be written - why models can be right in training but wrong in reality]*

---

## 3. Math (Gently)

*[To be written - base rate fallacy, calibration errors]*

---

## 4. Deeper Dive

*[To be written - fairness metrics, model cards, regulatory landscape]*

---

## 5. Codelab Summary

*[To be written - overview of notebook contents]*

---

## 6. Clinical Example

*[To be written - real examples of ML failures in healthcare]*

---

## 7. Further Reading

*[To be added]*

---

## The Abraham Wald Story

During World War II, the US military wanted to reinforce bomber planes to reduce losses. They examined returning aircraft and noted where bullet holes clustered—fuselage, wings, tail—and proposed adding armor there.

Statistician Abraham Wald saw the flaw: they were only looking at planes that **survived**. The holes showed where planes could be hit and still return. The missing data—planes shot down—would show hits in critical areas like the engine.

Wald recommended armoring the **un-hit** areas on returning planes.

**Lesson for clinical ML:**
- The patients in your database are often survivors
- Patients who died, moved away, or stopped treatment are missing
- Your model learns from what you see, not what you don't see

Always ask: **Who is NOT in my data?**

