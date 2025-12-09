"""
Generate all figures for Chapter 04 - Logistic Regression
This script is a standalone version to generate figures without running Jupyter.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    roc_auc_score, roc_curve, confusion_matrix,
    precision_recall_curve, average_precision_score
)

# Set random seed
np.random.seed(42)

# Periospot brand colors
PERIOSPOT_COLORS = {
    'periospot_blue': '#15365a',
    'mystic_blue': '#003049',
    'periospot_red': '#6c1410',
    'crimson_blaze': '#a92a2a',
    'vanilla_cream': '#f7f0da',
    'black': '#000000',
    'white': '#ffffff'
}

# Configure matplotlib
plt.rcParams.update({
    'font.family': 'DejaVu Sans',
    'font.size': 12,
    'axes.titlesize': 16,
    'axes.labelsize': 12,
    'xtick.labelsize': 10,
    'ytick.labelsize': 10,
    'figure.facecolor': 'white',
    'axes.facecolor': 'white',
    'axes.edgecolor': PERIOSPOT_COLORS['periospot_blue'],
    'axes.labelcolor': PERIOSPOT_COLORS['mystic_blue'],
    'text.color': PERIOSPOT_COLORS['black']
})

# Create figures directory
Path('figures').mkdir(exist_ok=True)

print("Loading data...")
df = pd.read_csv('data/implant_success_data_training.csv')
print(f"Dataset loaded: {len(df)} samples")

# FIGURE 1: Class Distribution
print("Generating Figure 1: Class Distribution...")
fig, axes = plt.subplots(1, 2, figsize=(12, 5))

class_counts = df['success'].value_counts()
colors = [PERIOSPOT_COLORS['crimson_blaze'], PERIOSPOT_COLORS['periospot_blue']]
bars = axes[0].bar(['Failure (0)', 'Success (1)'], 
                   [class_counts[0], class_counts[1]], 
                   color=colors, edgecolor='white', linewidth=2)
axes[0].set_ylabel('Count')
axes[0].set_title('Class Distribution: Success vs Failure')

for bar, count in zip(bars, [class_counts[0], class_counts[1]]):
    axes[0].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 5,
                 f'{count}', ha='center', fontsize=14, fontweight='bold')

axes[1].pie([class_counts[0], class_counts[1]], 
            labels=['Failure', 'Success'],
            colors=colors,
            autopct='%1.1f%%',
            explode=(0.02, 0.02),
            startangle=90,
            textprops={'fontsize': 12})
axes[1].set_title('Class Proportions')

plt.tight_layout()
plt.savefig('figures/01_class_distribution.png', dpi=150, bbox_inches='tight')
plt.close()

# FIGURE 2: Sigmoid Function
print("Generating Figure 2: Sigmoid Function...")
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

z = np.linspace(-10, 10, 200)
p = sigmoid(z)

fig, ax = plt.subplots(figsize=(12, 6))
ax.plot(z, p, color=PERIOSPOT_COLORS['periospot_blue'], linewidth=3, label='σ(z) = 1/(1+e⁻ᶻ)')
ax.axhline(0.5, color=PERIOSPOT_COLORS['crimson_blaze'], linestyle='--', alpha=0.7, label='p = 0.5')
ax.axvline(0, color=PERIOSPOT_COLORS['mystic_blue'], linestyle=':', alpha=0.7, label='z = 0')
ax.fill_between(z, 0, p, where=(z < 0), alpha=0.2, color=PERIOSPOT_COLORS['crimson_blaze'])
ax.fill_between(z, 0, p, where=(z >= 0), alpha=0.2, color=PERIOSPOT_COLORS['periospot_blue'])

key_z = [-5, -2, 0, 2, 5]
for z_val in key_z:
    p_val = sigmoid(z_val)
    ax.plot(z_val, p_val, 'o', color=PERIOSPOT_COLORS['mystic_blue'], markersize=10)
    ax.annotate(f'({z_val}, {p_val:.2f})', (z_val, p_val), 
                textcoords="offset points", xytext=(0, 15), ha='center', fontsize=9)

ax.set_xlabel('z (linear score)')
ax.set_ylabel('σ(z) = Probability')
ax.set_title('The Sigmoid Function: Transforming Scores to Probabilities', fontweight='bold')
ax.legend(loc='upper left')
ax.set_xlim(-10, 10)
ax.set_ylim(-0.05, 1.05)
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('figures/02_sigmoid_function.png', dpi=150, bbox_inches='tight')
plt.close()

# Prepare data for model
print("Training model...")
feature_columns = [
    'insertion_torque_ncm', 'isq_placement', 'hounsfield_units', 'age',
    'smoking_status', 'diabetes_status', 'implant_length_mm', 'implant_diameter_mm'
]

X = df[feature_columns]
y = df['success']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

model = LogisticRegression(penalty='l2', C=1.0, solver='lbfgs', max_iter=1000, random_state=42)
model.fit(X_train_scaled, y_train)

weights = model.coef_[0]

# FIGURE 3: Odds Ratios
print("Generating Figure 3: Odds Ratios...")
fig, ax = plt.subplots(figsize=(12, 7))

odds_ratios = np.exp(weights)
sorted_idx = np.argsort(odds_ratios)

y_pos = np.arange(len(feature_columns))
colors = [PERIOSPOT_COLORS['crimson_blaze'] if odds_ratios[i] < 1 
          else PERIOSPOT_COLORS['periospot_blue'] for i in sorted_idx]

bars = ax.barh(y_pos, odds_ratios[sorted_idx], color=colors, edgecolor='white', linewidth=2)
ax.set_yticks(y_pos)
ax.set_yticklabels([feature_columns[i] for i in sorted_idx])
ax.axvline(1.0, color=PERIOSPOT_COLORS['mystic_blue'], linestyle='--', linewidth=2, label='OR = 1')

for bar, idx in zip(bars, sorted_idx):
    width = bar.get_width()
    x_pos = width + 0.02 if width > 1 else width - 0.1
    ax.text(x_pos, bar.get_y() + bar.get_height()/2,
            f'{odds_ratios[idx]:.3f}', va='center', fontsize=10, fontweight='bold')

ax.set_xlabel('Odds Ratio')
ax.set_title('Feature Importance: Odds Ratios\n(OR > 1 increases success, OR < 1 decreases)', fontweight='bold')
ax.legend(loc='upper right')

plt.tight_layout()
plt.savefig('figures/03_odds_ratios.png', dpi=150, bbox_inches='tight')
plt.close()

# Generate predictions
y_pred_test = model.predict(X_test_scaled)
y_prob_test = model.predict_proba(X_test_scaled)[:, 1]
y_prob_train = model.predict_proba(X_train_scaled)[:, 1]

# FIGURE 4: ROC Curve
print("Generating Figure 4: ROC Curve...")
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

fpr_train, tpr_train, _ = roc_curve(y_train, y_prob_train)
fpr_test, tpr_test, _ = roc_curve(y_test, y_prob_test)

auc_train = roc_auc_score(y_train, y_prob_train)
auc_test = roc_auc_score(y_test, y_prob_test)

axes[0].plot(fpr_train, tpr_train, color=PERIOSPOT_COLORS['mystic_blue'], 
             linewidth=2, label=f'Training (AUC = {auc_train:.3f})')
axes[0].plot(fpr_test, tpr_test, color=PERIOSPOT_COLORS['crimson_blaze'], 
             linewidth=2, label=f'Test (AUC = {auc_test:.3f})')
axes[0].plot([0, 1], [0, 1], 'k--', linewidth=1, label='Random')
axes[0].fill_between(fpr_test, 0, tpr_test, alpha=0.2, color=PERIOSPOT_COLORS['crimson_blaze'])
axes[0].set_xlabel('False Positive Rate')
axes[0].set_ylabel('True Positive Rate')
axes[0].set_title('ROC Curve', fontweight='bold')
axes[0].legend(loc='lower right')
axes[0].grid(True, alpha=0.3)

precision_curve, recall_curve, _ = precision_recall_curve(y_test, y_prob_test)
ap = average_precision_score(y_test, y_prob_test)

axes[1].plot(recall_curve, precision_curve, color=PERIOSPOT_COLORS['periospot_blue'], 
             linewidth=2, label=f'PR Curve (AP = {ap:.3f})')
axes[1].axhline(y_test.mean(), color=PERIOSPOT_COLORS['crimson_blaze'], 
                linestyle='--', label=f'Baseline = {y_test.mean():.2f}')
axes[1].fill_between(recall_curve, 0, precision_curve, alpha=0.2, color=PERIOSPOT_COLORS['periospot_blue'])
axes[1].set_xlabel('Recall')
axes[1].set_ylabel('Precision')
axes[1].set_title('Precision-Recall Curve', fontweight='bold')
axes[1].legend(loc='lower left')
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('figures/04_roc_curve.png', dpi=150, bbox_inches='tight')
plt.close()

# FIGURE 5: Threshold Analysis
print("Generating Figure 5: Threshold Analysis...")
thresholds = np.arange(0.1, 0.95, 0.05)

threshold_metrics = []
for thresh in thresholds:
    y_pred_thresh = (y_prob_test >= thresh).astype(int)
    threshold_metrics.append({
        'Threshold': thresh,
        'Accuracy': accuracy_score(y_test, y_pred_thresh),
        'Precision': precision_score(y_test, y_pred_thresh, zero_division=0),
        'Recall': recall_score(y_test, y_pred_thresh, zero_division=0),
        'F1': f1_score(y_test, y_pred_thresh, zero_division=0)
    })

threshold_df = pd.DataFrame(threshold_metrics)

fig, axes = plt.subplots(1, 2, figsize=(14, 6))

axes[0].plot(threshold_df['Threshold'], threshold_df['Accuracy'], 
             label='Accuracy', linewidth=2, color=PERIOSPOT_COLORS['periospot_blue'])
axes[0].plot(threshold_df['Threshold'], threshold_df['Precision'], 
             label='Precision', linewidth=2, color=PERIOSPOT_COLORS['crimson_blaze'])
axes[0].plot(threshold_df['Threshold'], threshold_df['Recall'], 
             label='Recall', linewidth=2, color=PERIOSPOT_COLORS['mystic_blue'])
axes[0].plot(threshold_df['Threshold'], threshold_df['F1'], 
             label='F1 Score', linewidth=2, linestyle='--', color='black')
axes[0].axvline(0.5, color='gray', linestyle=':', alpha=0.7, label='t=0.5')
axes[0].set_xlabel('Threshold')
axes[0].set_ylabel('Score')
axes[0].set_title('Metrics vs. Threshold', fontweight='bold')
axes[0].legend(loc='lower center')
axes[0].grid(True, alpha=0.3)

axes[1].plot(threshold_df['Recall'], threshold_df['Precision'], 
             'o-', color=PERIOSPOT_COLORS['periospot_blue'], linewidth=2, markersize=6)
axes[1].set_xlabel('Recall')
axes[1].set_ylabel('Precision')
axes[1].set_title('Precision-Recall Tradeoff', fontweight='bold')
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('figures/05_threshold_analysis.png', dpi=150, bbox_inches='tight')
plt.close()

# FIGURE 6: Confusion Matrices
print("Generating Figure 6: Confusion Matrices...")
fig, axes = plt.subplots(1, 3, figsize=(15, 5))

thresholds_to_show = [0.3, 0.5, 0.7]
titles = ['Conservative (t=0.3)', 'Default (t=0.5)', 'Strict (t=0.7)']

for ax, thresh, title in zip(axes, thresholds_to_show, titles):
    y_pred_thresh = (y_prob_test >= thresh).astype(int)
    cm = confusion_matrix(y_test, y_pred_thresh)
    
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax,
                xticklabels=['Pred Fail', 'Pred Success'],
                yticklabels=['Actual Fail', 'Actual Success'],
                annot_kws={'size': 14})
    ax.set_title(title, fontweight='bold')

plt.tight_layout()
plt.savefig('figures/06_confusion_matrix.png', dpi=150, bbox_inches='tight')
plt.close()

print("\n✅ All figures generated successfully!")
print(f"\nModel Performance:")
print(f"  Accuracy: {accuracy_score(y_test, y_pred_test):.1%}")
print(f"  ROC-AUC: {auc_test:.3f}")
print(f"  F1 Score: {f1_score(y_test, y_pred_test):.3f}")

# List figures
print("\nGenerated figures:")
for f in sorted(Path('figures').glob('*.png')):
    print(f"  • {f}")

