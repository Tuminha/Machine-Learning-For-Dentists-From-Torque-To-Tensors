# D4 - Text Dataset

## Purpose

This dataset contains **clinical text data** used to demonstrate:
- Basic text preprocessing (tokenization, cleaning)
- Bag of words and TF-IDF representations
- Word embeddings
- Introduction to transformer models and LLMs

## Expected Content Types

Choose one or combine:

### Option A: Clinical Notes (Synthetic)

Short clinical notes documenting patient visits:

```
Patient presents with chief complaint of bleeding gums for 3 months.
Medical history: Type 2 diabetes, controlled with metformin.
Examination reveals generalized moderate periodontitis with 4-6mm pockets
in posterior regions. BOP 45%. Recommended SRP and 3-month recall.
```

### Option B: Paper Abstracts

Abstracts from dental research papers:

```
OBJECTIVE: To evaluate the effectiveness of photodynamic therapy as
an adjunct to scaling and root planing in chronic periodontitis.
METHODS: Randomized controlled trial with 60 patients...
RESULTS: Significant reduction in probing depth (p<0.05)...
CONCLUSION: PDT may provide additional benefits...
```

### Option C: Patient Questions

Common patient questions and concerns:

```
"My dentist says I need a deep cleaning. Is this the same as a regular cleaning?"
"I'm worried about the implant my dentist recommended. How long do they last?"
"Is it normal to have some bleeding when I floss?"
```

## Data Structure

### Main Dataset

| Column | Description |
|--------|-------------|
| `text_id` | Unique identifier |
| `text` | The actual text content |
| `category` | Classification label (if applicable) |
| `source_type` | clinical_note / abstract / question |
| `word_count` | Number of words |

### Example Classification Tasks

1. **Sentiment**: Positive/Negative/Neutral patient feedback
2. **Topic**: Treatment type (implant/perio/endo/ortho)
3. **Urgency**: Emergency/Routine in clinical notes
4. **Evidence level**: Type of study from abstracts

## Usage in Chapters

- **Chapter 16**: Main NLP chapter
- Shows: Text cleaning, vectorization, classification, embeddings

## Text Specifications

- **Language**: English
- **Quantity**: 200-500 documents minimum
- **Length**: Variable (50-500 words typical)
- **Format**: CSV with text in dedicated column

## Privacy & Ethics Note

⚠️ **Important**:
- Clinical notes must be **fully synthetic** or properly anonymized
- No real patient information
- Abstracts from published papers are generally safe to use (cite sources)

---

## Files in This Folder

*Placeholder - files will be added*

- `clinical_texts.csv` - Main text dataset
- `text_preprocessing.ipynb` - Initial text exploration
- `stopwords_dental.txt` - Custom stopwords for dental domain (optional)

