# Periospot Font Assets - Bariol Family

This folder contains the **Bariol** font family used for all Periospot charts and visualizations.

## Available Font Weights

| File | Weight | Use Case |
|------|--------|----------|
| `Bariol_Thin.otf` | Thin | Subtle annotations, watermarks |
| `Bariol_Thin_Italic.otf` | Thin Italic | Emphasized subtle text |
| `Bariol_Light.otf` | Light | Tick labels, captions, annotations |
| `Bariol_Light_Italic.otf` | Light Italic | Emphasized captions |
| `Bariol_Regular.otf` | Regular | Body text, axis labels, legends |
| `Bariol_Bold.otf` | Bold | Titles, headings (H1, H2) |
| `Bariol_Bold_Italic.otf` | Bold Italic | Emphasized titles |

## Typography System

The typography rules are defined in `/brand_palette.json`:

### Document Styles
| Style | Weight | Size | Color | Use |
|-------|--------|------|-------|-----|
| **h1** | Bold | 24pt | periospot_blue | Main titles, chapter headings |
| **h2** | Bold | 18pt | periospot_blue | Section headings |
| **h3** | Regular | 14pt | mystic_blue | Subsection headings |
| **body** | Regular | 11pt | black | Body text, paragraphs |
| **caption** | Light | 9pt | mystic_blue | Figure captions, footnotes |
| **label** | Regular | 10pt | mystic_blue | Axis labels, legend text |

### Chart Styles (Matplotlib)
| Style | Weight | Size | Color |
|-------|--------|------|-------|
| **chart_title** | Bold | 16pt | periospot_blue |
| **axis_title** | Regular | 12pt | mystic_blue |
| **tick_labels** | Light | 10pt | mystic_blue |
| **legend** | Regular | 10pt | black |
| **annotation** | Light | 9pt | mystic_blue |

## Usage in Notebooks

```python
from utils.periospot_style import (
    setup_periospot_style,
    PERIOSPOT_COLORS,
    get_font_props,
    style_title,
    style_labels
)

# Apply the style (loads all Bariol variants)
config = setup_periospot_style()
# Output: ✓ Loaded Bariol font family (7 variants)

# Create a chart with proper styling
fig, ax = plt.subplots()
ax.plot(x, y, color=PERIOSPOT_COLORS['periospot_blue'])

# Apply typography
style_title(ax, 'My Chart Title', level='h1')
style_labels(ax, xlabel='Time', ylabel='Value')

# Or use font properties directly
ax.set_title('Title', fontproperties=get_font_props('chart_title'))
```

## License Note

Bariol is a commercial font. Ensure you have the appropriate license for your use case.
