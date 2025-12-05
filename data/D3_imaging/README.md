# D3 - Imaging Dataset

## Purpose

This dataset contains **dental radiographs** (X-rays) or similar imaging data used to demonstrate:
- How image data differs from tabular data
- Basic image preprocessing
- Using pre-trained models (transfer learning)
- Interpreting model predictions on images

## Expected Structure

### Images

```
D3_imaging/
├── images/
│   ├── class_A/          # e.g., healthy
│   │   ├── img_001.jpg
│   │   ├── img_002.jpg
│   │   └── ...
│   ├── class_B/          # e.g., pathology present
│   │   ├── img_101.jpg
│   │   └── ...
│   └── class_C/          # optional additional class
│       └── ...
├── metadata.csv          # Image-level labels and info
└── README.md             # This file
```

### Metadata CSV

| Column | Description |
|--------|-------------|
| `image_id` | Filename |
| `class` | Label (healthy/pathology/etc) |
| `tooth_region` | Anterior/Posterior/Full mouth |
| `image_quality` | Good/Acceptable/Poor |
| `patient_age` | Age at image capture |

## Potential Image Types

Choose one focus for the chapter:

1. **Periapical radiographs**
   - Task: Detect periapical lesions
   - Classes: Normal, Lesion present

2. **Bitewing radiographs**
   - Task: Detect interproximal caries
   - Classes: No caries, Caries present

3. **Panoramic radiographs**
   - Task: Assess bone loss
   - Classes: Healthy, Mild loss, Severe loss

4. **Intraoral photos**
   - Task: Classify gingival health
   - Classes: Healthy, Gingivitis, Periodontitis

## Image Specifications

- **Format**: JPEG or PNG
- **Size**: Consistent dimensions (e.g., 224x224 for pre-trained models)
- **Color**: Grayscale for radiographs, RGB for photos
- **Quantity**: Minimum 100 images per class for meaningful training

## Usage in Chapters

- **Chapter 15**: Main imaging chapter
- Shows: Loading images, basic augmentation, transfer learning with ResNet/EfficientNet

## Data Source Options

1. **Public datasets**: Search for open dental imaging datasets
2. **Synthetic**: Generated images for educational purposes
3. **Anonymized clinical**: If available with proper ethics approval

## Privacy & Ethics Note

⚠️ **Important**: Any clinical images must be:
- Fully anonymized (no patient identifiers in metadata or EXIF)
- Used with appropriate permissions
- Clearly marked as educational examples

---

## Files in This Folder

*Placeholder - files will be added*

- `images/` - Folder containing images organized by class
- `metadata.csv` - Image-level information
- `data_exploration.ipynb` - Initial image exploration

