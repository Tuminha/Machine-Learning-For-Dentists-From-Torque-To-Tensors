"""
Synthetic Implant Success/Failure Dataset Generator

This script generates a realistic synthetic dataset for predicting
implant success vs. failure (binary classification).

Features are based on clinical factors known to influence implant outcomes:
- Insertion torque (Ncm)
- ISQ (Implant Stability Quotient) at placement
- Bone density (Hounsfield Units)
- Patient age
- Smoking status (binary)
- Diabetes status (binary)
- Implant length (mm)
- Implant diameter (mm)

The success probability is modeled using a logistic function with
clinically plausible relationships.

Author: Francisco Teixeira Barbosa
Project: Machine Learning For Dentists
"""

import numpy as np
import pandas as pd
from pathlib import Path

# Set random seed for reproducibility
np.random.seed(42)

def generate_implant_success_data(n_samples: int = 500) -> pd.DataFrame:
    """
    Generate synthetic implant success/failure data.
    
    Args:
        n_samples: Number of implant cases to generate
        
    Returns:
        DataFrame with features and binary success outcome
    """
    
    # Generate patient demographics
    age = np.random.normal(55, 12, n_samples).clip(25, 85)
    
    # Smoking status (30% smokers, realistic for dental population)
    smoking_status = np.random.binomial(1, 0.30, n_samples)
    
    # Diabetes status (15% diabetic)
    diabetes_status = np.random.binomial(1, 0.15, n_samples)
    
    # Generate implant characteristics
    # Insertion torque: 15-50 Ncm, normally distributed
    insertion_torque = np.random.normal(35, 8, n_samples).clip(15, 50)
    
    # ISQ at placement: 50-85, correlated with torque
    isq_placement = (
        0.4 * insertion_torque + 
        np.random.normal(50, 8, n_samples)
    ).clip(45, 85)
    
    # Bone density (Hounsfield Units): 300-1200
    # Smokers and diabetics tend to have lower bone density
    hounsfield_units = (
        np.random.normal(700, 150, n_samples) - 
        80 * smoking_status - 
        60 * diabetes_status
    ).clip(250, 1200)
    
    # Implant dimensions
    implant_length = np.random.choice([8.0, 10.0, 11.5, 13.0], n_samples, 
                                       p=[0.15, 0.35, 0.35, 0.15])
    implant_diameter = np.random.choice([3.5, 4.0, 4.5, 5.0], n_samples,
                                         p=[0.20, 0.40, 0.30, 0.10])
    
    # Calculate implant surface area (simplified cylinder approximation)
    implant_surface = np.pi * implant_diameter * implant_length
    
    # Generate success probability using logistic function
    # Based on clinical factors with plausible relationships
    
    # Normalize features for logistic model
    torque_norm = (insertion_torque - 35) / 8
    isq_norm = (isq_placement - 65) / 10
    hu_norm = (hounsfield_units - 700) / 150
    age_norm = (age - 55) / 12
    length_norm = (implant_length - 10.5) / 2
    
    # Log-odds calculation (linear predictor)
    # Positive weights increase success probability
    # Negative weights decrease success probability
    log_odds = (
        0.8 * torque_norm +        # Higher torque → better
        1.2 * isq_norm +           # Higher ISQ → better (most important)
        0.5 * hu_norm +            # Better bone density → better
        -0.3 * age_norm +          # Older age → slightly worse
        -1.5 * smoking_status +    # Smoking → much worse
        -0.8 * diabetes_status +   # Diabetes → worse
        0.3 * length_norm +        # Longer implants → slightly better
        0.5                        # Intercept (base success rate ~62%)
    )
    
    # Add some noise to make it realistic
    log_odds += np.random.normal(0, 0.4, n_samples)
    
    # Convert log-odds to probability using sigmoid
    success_prob = 1 / (1 + np.exp(-log_odds))
    
    # Generate binary outcomes based on probability
    success = np.random.binomial(1, success_prob)
    
    # Create DataFrame
    df = pd.DataFrame({
        'patient_id': [f'PAT-{i+1:04d}' for i in range(n_samples)],
        'age': np.round(age, 1),
        'smoking_status': smoking_status,
        'diabetes_status': diabetes_status,
        'insertion_torque_ncm': np.round(insertion_torque, 1),
        'isq_placement': np.round(isq_placement, 1),
        'hounsfield_units': np.round(hounsfield_units, 0).astype(int),
        'implant_length_mm': implant_length,
        'implant_diameter_mm': implant_diameter,
        'implant_surface_mm2': np.round(implant_surface, 1),
        'success': success,
        'success_probability_true': np.round(success_prob, 4)  # For validation
    })
    
    return df


def main():
    """Generate and save the dataset."""
    
    # Generate data
    print("Generating synthetic implant success/failure dataset...")
    df = generate_implant_success_data(n_samples=500)
    
    # Summary statistics
    print(f"\nDataset Summary:")
    print(f"  Total samples: {len(df)}")
    print(f"  Success rate: {df['success'].mean():.1%}")
    print(f"  Failure rate: {1 - df['success'].mean():.1%}")
    print(f"\nClass distribution:")
    print(df['success'].value_counts())
    
    # Feature ranges
    print(f"\nFeature ranges:")
    numeric_cols = ['age', 'insertion_torque_ncm', 'isq_placement', 
                    'hounsfield_units', 'implant_length_mm', 'implant_diameter_mm']
    for col in numeric_cols:
        print(f"  {col}: {df[col].min():.1f} - {df[col].max():.1f}")
    
    # Save to CSV
    output_path = Path(__file__).parent / 'implant_success_data.csv'
    df.to_csv(output_path, index=False)
    print(f"\nDataset saved to: {output_path}")
    
    # Also save a version without the true probability (for realistic training)
    df_train = df.drop(columns=['success_probability_true'])
    train_path = Path(__file__).parent / 'implant_success_data_training.csv'
    df_train.to_csv(train_path, index=False)
    print(f"Training dataset (without true probabilities) saved to: {train_path}")


if __name__ == '__main__':
    main()

