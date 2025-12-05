# D2 - Toy Tabular Dataset

## Purpose

This is a **simple, small dataset** used when:
- Introducing new concepts where complexity would distract
- Focusing purely on algorithm intuition or math
- Running quick experiments that need fast feedback

## Design Principles

- **Small**: 50-200 rows maximum
- **Clean**: No missing values, no outliers
- **Simple**: 3-5 features only
- **Clear**: Obvious relationships that algorithms can find

## Expected Structure

### Option A: Dental Measurements (Synthetic)

Simple tooth-level measurements:

| Feature | Description | Type |
|---------|-------------|------|
| `tooth_id` | Identifier | ID |
| `pocket_depth` | Probing depth (mm) | Continuous |
| `bone_level` | Bone level (mm) | Continuous |
| `mobility` | Tooth mobility (0-3) | Ordinal |
| `needs_extraction` | Target variable | Binary |

### Option B: Patient Risk (Synthetic)

Simplified patient-level data:

| Feature | Description | Type |
|---------|-------------|------|
| `patient_id` | Identifier | ID |
| `age` | Age in years | Continuous |
| `smoker` | Smoking status | Binary |
| `plaque_score` | Plaque index (0-3) | Ordinal |
| `high_risk` | Target variable | Binary |

## Usage in Chapters

- **Chapter 1**: Introduction to prediction (majority class baseline)
- **Chapter 3-6**: When introducing new algorithms
- **Anytime**: Quick sanity checks before using D1

## Example Data

```csv
tooth_id,pocket_depth,bone_level,mobility,needs_extraction
T001,3.2,8.5,0,0
T002,6.8,4.2,2,1
T003,4.1,7.1,1,0
T004,8.5,2.3,3,1
```

## Data Source

**Fully synthetic** - designed to have clear patterns that make algorithm behavior easy to understand.

---

## Files in This Folder

*Placeholder - files will be added*

- `toy_dental_data.csv` - Main toy dataset
- `generate_toy_data.py` - Script to regenerate if needed

