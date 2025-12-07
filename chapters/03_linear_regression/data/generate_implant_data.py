"""
Generate synthetic implant dataset for Linear Regression chapter.

This script creates a realistic dataset of dental implant cases
with features that influence marginal bone loss (MBL) after 1 year.

The data is SYNTHETIC - designed for educational purposes only.
It does not represent real patient data.
"""

import numpy as np
import pandas as pd
from pathlib import Path

# Set random seed for reproducibility
np.random.seed(42)

# Number of cases
N_CASES = 500

# =============================================================================
# GENERATE FEATURES
# =============================================================================

# Patient demographics
patient_id = [f"P{str(i).zfill(4)}" for i in range(1, N_CASES + 1)]
age = np.random.normal(55, 12, N_CASES).clip(25, 85).astype(int)
sex = np.random.choice(['Male', 'Female'], N_CASES, p=[0.45, 0.55])
smoking_status = np.random.choice(
    ['Never', 'Former', 'Current'], 
    N_CASES, 
    p=[0.55, 0.30, 0.15]
)

# Diabetes status (correlated with age slightly)
diabetes_prob = 0.15 + (age - 40) * 0.003  # Higher probability with age
diabetes_prob = diabetes_prob.clip(0.05, 0.40)
diabetes = np.random.binomial(1, diabetes_prob).astype(bool)

# HbA1c (only meaningful for diabetics, but generate for all)
hba1c = np.where(
    diabetes,
    np.random.normal(7.2, 0.8, N_CASES).clip(5.7, 10.0),
    np.random.normal(5.4, 0.3, N_CASES).clip(4.5, 5.6)
)

# Implant site characteristics
hounsfield_units = np.random.normal(450, 150, N_CASES).clip(150, 850).astype(int)
bone_type = pd.cut(
    hounsfield_units,
    bins=[0, 300, 500, 700, 1000],
    labels=['D4 (Very soft)', 'D3 (Soft)', 'D2 (Normal)', 'D1 (Dense)']
)

# Surgical parameters
insertion_torque = np.random.normal(35, 10, N_CASES).clip(15, 60).astype(int)
isq_placement = np.random.normal(68, 8, N_CASES).clip(45, 85).astype(int)

# Implant characteristics
implant_length = np.random.choice([8, 10, 11.5, 13], N_CASES, p=[0.15, 0.35, 0.30, 0.20])
implant_diameter = np.random.choice([3.5, 4.0, 4.5, 5.0], N_CASES, p=[0.20, 0.40, 0.30, 0.10])

# =============================================================================
# GENERATE TARGET: Marginal Bone Loss (MBL) at 1 year
# =============================================================================

# True underlying relationship (what we want the model to discover)
# MBL is influenced by:
# - Higher torque → slightly more MBL (overstressing bone)
# - Higher ISQ → less MBL (better stability)
# - Higher HU → less MBL (denser bone)
# - Smoking → more MBL
# - Diabetes (uncontrolled) → more MBL
# - Age → slight increase in MBL

# Base MBL
mbl_base = 0.8  # mm baseline

# Feature contributions
mbl_torque = (insertion_torque - 35) * 0.015  # +0.015 mm per Ncm above 35
mbl_isq = (isq_placement - 68) * -0.012  # -0.012 mm per ISQ point above 68
mbl_hu = (hounsfield_units - 450) * -0.0008  # -0.0008 mm per HU above 450
mbl_age = (age - 55) * 0.005  # +0.005 mm per year above 55
mbl_smoking = np.where(smoking_status == 'Current', 0.35, 
                        np.where(smoking_status == 'Former', 0.10, 0))
mbl_diabetes = np.where(diabetes & (hba1c > 7.5), 0.25, 
                         np.where(diabetes, 0.10, 0))

# Total MBL with noise
noise = np.random.normal(0, 0.25, N_CASES)  # Random variation
marginal_bone_loss = (
    mbl_base + mbl_torque + mbl_isq + mbl_hu + 
    mbl_age + mbl_smoking + mbl_diabetes + noise
).clip(0.1, 3.5)  # Realistic range

# Round to 2 decimal places
marginal_bone_loss = np.round(marginal_bone_loss, 2)

# =============================================================================
# CREATE DATAFRAME
# =============================================================================

df = pd.DataFrame({
    'patient_id': patient_id,
    'age': age,
    'sex': sex,
    'smoking_status': smoking_status,
    'diabetes': diabetes,
    'hba1c': np.round(hba1c, 1),
    'hounsfield_units': hounsfield_units,
    'bone_type': bone_type,
    'insertion_torque_ncm': insertion_torque,
    'isq_placement': isq_placement,
    'implant_length_mm': implant_length,
    'implant_diameter_mm': implant_diameter,
    'marginal_bone_loss_mm': marginal_bone_loss
})

# Add some missing values to make it realistic
# About 3% missing in some columns
missing_mask = np.random.random(N_CASES) < 0.03
df.loc[missing_mask, 'hba1c'] = np.nan

missing_mask = np.random.random(N_CASES) < 0.02
df.loc[missing_mask, 'isq_placement'] = np.nan

# =============================================================================
# SAVE DATASET
# =============================================================================

output_dir = Path(__file__).parent
output_file = output_dir / 'implant_bone_loss.csv'

df.to_csv(output_file, index=False)

print(f"✓ Generated {len(df)} synthetic implant cases")
print(f"✓ Saved to: {output_file}")
print(f"\nDataset summary:")
print(f"  - Features: {df.shape[1] - 2} (excluding patient_id and target)")
print(f"  - Target: marginal_bone_loss_mm")
print(f"  - Target range: {df['marginal_bone_loss_mm'].min():.2f} - {df['marginal_bone_loss_mm'].max():.2f} mm")
print(f"  - Target mean: {df['marginal_bone_loss_mm'].mean():.2f} mm")
print(f"\nMissing values:")
print(df.isnull().sum()[df.isnull().sum() > 0])

# =============================================================================
# ALSO CREATE A SMALLER "TOY" VERSION FOR QUICK DEMOS
# =============================================================================

df_toy = df.head(50).copy()
df_toy.to_csv(output_dir / 'implant_bone_loss_toy.csv', index=False)
print(f"\n✓ Also created toy version with 50 cases")

