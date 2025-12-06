# Custom Fonts for Periospot Charts

Place your custom OTF/TTF font files in this folder.

## Supported Formats

- `.otf` - OpenType Font
- `.ttf` - TrueType Font

## Usage

After placing your font file here, use the `periospot_style` module to load it:

```python
from utils.periospot_style import setup_periospot_style

# This will load your custom font and apply Periospot colors
setup_periospot_style()
```

## Font Files

Add your font files here:
- `YourCustomFont.otf` - Main font for charts

## Notes

- The font will be registered with matplotlib automatically
- You can use multiple weights if you have them (Regular, Bold, etc.)

