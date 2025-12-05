# D1 - Core Tabular Dental Dataset

## Purpose

This is the **main dataset** used throughout most chapters of the book. It contains clinical, metabolic, and behavioral variables related to dental outcomes.

## Expected Structure

The dataset should contain patient-level data with features like:

### Patient Demographics
- `patient_id`: Unique identifier
- `age`: Patient age in years
- `sex`: Male/Female
- `smoking_status`: Never/Former/Current
- `smoking_pack_years`: Cumulative smoking exposure

### Clinical Measurements
- `probing_depth`: Average probing depth (mm)
- `clinical_attachment_loss`: Average CAL (mm)
- `bleeding_on_probing`: Percentage of sites (%)
- `plaque_index`: Plaque score (0-3)
- `bone_loss_percentage`: Radiographic bone loss (%)

### Medical History
- `diabetes`: Yes/No
- `hba1c`: If diabetic, HbA1c value
- `hypertension`: Yes/No
- `cardiovascular_disease`: Yes/No
- `medications`: Number of daily medications

### Dental Specifics
- `teeth_present`: Number of teeth
- `implants_present`: Number of implants
- `years_since_treatment`: Time since last major treatment

### Outcomes (Target Variables)
- `periodontitis_severity`: None/Mild/Moderate/Severe
- `tooth_loss_5yr`: Binary (lost tooth within 5 years)
- `implant_failure_5yr`: Binary (implant failed within 5 years)
- `treatment_response`: Good/Moderate/Poor

## Data Format

- **File format**: CSV (preferred) or Parquet
- **Encoding**: UTF-8
- **Missing values**: Use empty cells or `NA`

## Example Row

```csv
patient_id,age,sex,smoking_status,probing_depth,bleeding_on_probing,diabetes,periodontitis_severity
P001,58,Male,Former,4.2,35,Yes,Moderate
```

## Data Source

This dataset will be created as **synthetic/mock data** using tools like Manus AI, designed to be clinically realistic but not from real patients.

## Privacy Note

⚠️ This is synthetic data created for educational purposes only. It does not contain any real patient information.

---

## Files in This Folder

*Placeholder - files will be added when dataset is created*

- `dental_clinical_data.csv` - Main dataset
- `data_dictionary.md` - Variable definitions
- `data_exploration.ipynb` - Initial EDA notebook

