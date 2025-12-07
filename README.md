<div align="center">

<img src="images/ML%20for%20dentists%20banner.png" alt="Machine Learning For Dentists - From Torque to Tensors" width="100%" />

<br />

![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)
![Framework](https://img.shields.io/badge/ML-scikit--learn-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-In%20Development-yellow.svg)

**A practical guide to machine learning for clinicians who want to understand prediction, not just use it.**

[📖 Blueprint](BOOK_REPO_BLUEPRINT.md) • [🤖 AI Guide](AGENT_GUIDE.md) • [📚 Chapters](#-chapters) • [🚀 Quick Start](#-quick-start)

</div>

---

## 👨‍💻 Author

<div align="center">

**Francisco Teixeira Barbosa**

[![GitHub](https://img.shields.io/badge/GitHub-Tuminha-black?style=flat&logo=github)](https://github.com/Tuminha)
[![Kaggle](https://img.shields.io/badge/Kaggle-Profile-20BEFF?style=flat&logo=kaggle&logoColor=white)](https://www.kaggle.com/franciscotbarbosa)
[![Email](https://img.shields.io/badge/Email-cisco%40periospot.com-blue?style=flat&logo=gmail)](mailto:cisco@periospot.com)
[![Twitter](https://img.shields.io/badge/Twitter-cisco__research-1DA1F2?style=flat&logo=twitter)](https://twitter.com/cisco_research)

*Periodontist learning machine learning • Building AI solutions for dentistry* 🦷

</div>

---

## 🎯 What Is This?

This repository hosts:

- **📖 The book manuscript** - Chapter texts in markdown (`CHAPTER_TEXT.md`)
- **💻 Companion code** - Jupyter notebooks for hands-on learning
- **📊 Datasets** - Curated dental data for examples (synthetic/mock)
- **📝 Templates** - Consistent structure for all chapters

### Who Is This For?

- **Dentists and periodontists** curious about ML
- **Residents and PhD students** in dentistry
- **Anyone in healthcare** who wants to understand prediction without becoming a data scientist

### What Will You Learn?

By the end of this book, you will:

- ✅ Understand what "prediction" really means in clinical practice
- ✅ Have intuition for the main ML algorithms (not just black boxes)
- ✅ Be able to run notebooks, tweak parameters, and interpret results
- ✅ Recognize overfitting, bias, and common ML pitfalls
- ✅ Know when to use tabular models vs. images vs. text

---

## 📚 Chapters

### Part I - Why Prediction Matters

| # | Chapter | Description |
|---|---------|-------------|
| 01 | [The Power of Prediction](chapters/01_power_of_prediction/) | Why prediction matters in dentistry |
| 02 | [Data for Clinical Questions](chapters/02_data_for_clinical_questions/) | Understanding your data |

### Part II - Core Algorithms

| # | Chapter | Description |
|---|---------|-------------|
| 03 | [Linear Regression](chapters/03_linear_regression/) | Predicting continuous outcomes |
| 04 | [Logistic Regression](chapters/04_logistic_regression/) | The workhorse of binary classification |
| 05 | [k-Nearest Neighbors](chapters/05_knn/) | Classification by similarity |
| 06 | [Naive Bayes](chapters/06_naive_bayes/) | Probability-based classification |
| 07 | [Decision Trees](chapters/07_decision_trees/) | If-then rules for prediction |
| 08 | [Random Forests](chapters/08_random_forests/) | Wisdom of the crowd |
| 09 | [Gradient Boosting](chapters/09_gradient_boosting/) | Learning from mistakes |
| 10 | [XGBoost](chapters/10_xgboost/) | Extreme gradient boosting |
| 11 | [LightGBM](chapters/11_lightgbm/) | Light gradient boosting |
| 12 | [CatBoost](chapters/12_catboost/) | Categorical boosting |
| 13 | [Clustering](chapters/13_clustering/) | Finding natural groups |
| 14 | [Dimensionality Reduction](chapters/14_dimensionality_reduction/) | Simplifying complex data |

### Part III - Beyond Classic ML

| # | Chapter | Description |
|---|---------|-------------|
| 15 | [Imaging](chapters/15_imaging/) | From pixels to predictions |
| 16 | [Text and NLP](chapters/16_text_nlp/) | From words to embeddings |
| 17 | [ML In Practice](chapters/17_ml_in_practice/) | Deploying models safely |
| 18 | [Pitfalls, Bias, Ethics](chapters/18_pitfalls_bias_ethics/) | What can go wrong |

---

## 🚀 Quick Start

### Option 1: Google Colab (Recommended for Beginners)

Each chapter has a "Open in Colab" button. Click it and you're ready to go!

### Option 2: Local Setup

```bash
# Clone the repository
git clone https://github.com/Tuminha/ml-for-dentists.git
cd ml-for-dentists

# Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Start Jupyter
jupyter notebook
```

### Option 3: Cursor AI

1. Open the repo folder in Cursor
2. Cursor will read `AGENT_GUIDE.md` for context
3. Ask it: "Help me run the Chapter 1 notebook"

---

## 📁 Repository Structure

```
.
├── BOOK_REPO_BLUEPRINT.md    # Project overview
├── AGENT_GUIDE.md            # AI assistant instructions
├── README.md                 # This file
├── requirements.txt          # Python dependencies
├── data/
│   ├── D1_core_tabular/      # Main dental dataset
│   ├── D2_toy_tabular/       # Simple toy dataset
│   ├── D3_imaging/           # Dental radiographs
│   └── D4_text/              # Clinical notes
├── chapters/
│   ├── 01_power_of_prediction/
│   │   ├── README.md         # Chapter overview
│   │   ├── CHAPTER_TEXT.md   # Book prose
│   │   └── *.ipynb           # Notebook
│   └── ...
├── templates/
│   ├── chapter_template.md
│   └── notebook_template.ipynb
└── images/
```

---

## 📊 Canonical Datasets

We use 4 recurring datasets throughout the book:

| ID | Name | Description | Chapters |
|----|------|-------------|----------|
| **D1** | Core Tabular | Dental clinical data (implants, perio, caries) | Most chapters |
| **D2** | Toy Tabular | Small, clean data for intuition | Ch 1, basics |
| **D3** | Imaging | Dental radiographs | Ch 15 |
| **D4** | Text | Clinical notes, abstracts | Ch 16 |

---

## 🎨 Visual Style

All visualizations use the **Periospot brand colors**:

- **Periospot Blue**: `#15365a`
- **Mystic Blue**: `#003049`
- **Periospot Red**: `#6c1410`
- **Crimson Blaze**: `#a92a2a`
- **Vanilla Cream**: `#f7f0da`

---

## 📖 How Each Chapter Is Structured

Every chapter follows the same pattern:

1. **Story** - A clinical vignette that frames the problem
2. **Intuition** - Plain language explanation
3. **Math** - Minimal but correct formulas
4. **Deeper Dive** - For curious readers
5. **Codelab** - Hands-on notebook
6. **Clinical Example** - Real dental scenario
7. **Further Reading** - Resources for more depth

---

## 🤝 Contributing

This is primarily an educational project. If you find errors or have suggestions:

1. Open an issue
2. Or submit a pull request

---

## 📄 License

MIT License - See [LICENSE](LICENSE) for details.

---

<div align="center">

**⭐ Star this repo if you find it helpful! ⭐**

*Building clinical intuition about machine learning, one algorithm at a time* 🦷

</div>

