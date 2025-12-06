"""
Periospot Visual Style for Machine Learning For Dentists
=========================================================

This module provides consistent styling for all matplotlib charts
using Periospot brand colors and custom fonts.

Usage:
    from utils.periospot_style import setup_periospot_style, PERIOSPOT_COLORS
    
    # Apply the style (call once at the start of your notebook)
    setup_periospot_style()
    
    # Or with a custom font file
    setup_periospot_style(font_path='assets/fonts/YourFont.otf')
"""

import matplotlib.pyplot as plt
from matplotlib import font_manager
from pathlib import Path
import warnings

# =============================================================================
# PERIOSPOT BRAND COLORS
# =============================================================================

PERIOSPOT_COLORS = {
    'periospot_blue': '#15365a',
    'mystic_blue': '#003049',
    'periospot_red': '#6c1410',
    'crimson_blaze': '#a92a2a',
    'vanilla_cream': '#f7f0da',
    'black': '#000000',
    'white': '#ffffff',
}

# Color palette for sequential data (e.g., multiple lines in a plot)
PERIOSPOT_PALETTE = [
    '#15365a',  # periospot_blue
    '#a92a2a',  # crimson_blaze
    '#003049',  # mystic_blue
    '#6c1410',  # periospot_red
    '#f7f0da',  # vanilla_cream (for backgrounds)
]

# =============================================================================
# FONT SETUP
# =============================================================================

def _find_font_file(font_path=None):
    """
    Find the custom font file.
    
    Parameters
    ----------
    font_path : str or Path, optional
        Path to a custom OTF/TTF font file.
        If None, looks for fonts in assets/fonts/
    
    Returns
    -------
    Path or None
        Path to the font file, or None if not found.
    """
    if font_path:
        path = Path(font_path)
        if path.exists():
            return path
        else:
            warnings.warn(f"Font file not found: {font_path}")
            return None
    
    # Look for fonts in the default location
    # Try to find the project root (look for README.md or AGENT_GUIDE.md)
    possible_roots = [
        Path.cwd(),
        Path.cwd().parent,
        Path(__file__).parent.parent,
    ]
    
    for root in possible_roots:
        fonts_dir = root / 'assets' / 'fonts'
        if fonts_dir.exists():
            # Look for OTF or TTF files
            for ext in ['*.otf', '*.ttf', '*.OTF', '*.TTF']:
                fonts = list(fonts_dir.glob(ext))
                if fonts:
                    return fonts[0]  # Return first font found
    
    return None


def _register_font(font_path):
    """
    Register a font with matplotlib.
    
    Parameters
    ----------
    font_path : Path
        Path to the font file.
    
    Returns
    -------
    str
        The font family name.
    """
    font_path = Path(font_path)
    
    # Add the font to matplotlib
    font_manager.fontManager.addfont(str(font_path))
    
    # Get the font name
    prop = font_manager.FontProperties(fname=str(font_path))
    font_name = prop.get_name()
    
    return font_name


# =============================================================================
# MAIN SETUP FUNCTION
# =============================================================================

def setup_periospot_style(font_path=None, use_custom_font=True):
    """
    Apply Periospot visual style to matplotlib.
    
    This function:
    1. Sets the color palette to Periospot brand colors
    2. Loads and applies a custom font (if available)
    3. Configures chart aesthetics for clean, professional output
    
    Parameters
    ----------
    font_path : str or Path, optional
        Path to a custom OTF/TTF font file.
        If None and use_custom_font=True, looks in assets/fonts/
    use_custom_font : bool, default True
        Whether to try loading a custom font.
        If False or no font is found, uses 'DejaVu Sans'.
    
    Returns
    -------
    dict
        Configuration info including font name and colors.
    
    Example
    -------
    >>> from utils.periospot_style import setup_periospot_style
    >>> config = setup_periospot_style()
    >>> print(f"Using font: {config['font_family']}")
    """
    
    font_family = 'DejaVu Sans'  # Default fallback
    
    # Try to load custom font
    if use_custom_font:
        font_file = _find_font_file(font_path)
        if font_file:
            try:
                font_family = _register_font(font_file)
                print(f"✓ Loaded custom font: {font_family}")
            except Exception as e:
                warnings.warn(f"Could not load font {font_file}: {e}")
                print(f"⚠ Using default font: {font_family}")
        else:
            print(f"ℹ No custom font found. Using: {font_family}")
            print(f"  (Add an OTF/TTF file to assets/fonts/ to use a custom font)")
    
    # ==========================================================================
    # MATPLOTLIB CONFIGURATION
    # ==========================================================================
    
    # Font settings
    plt.rcParams['font.family'] = font_family
    plt.rcParams['font.size'] = 11
    
    # Title and labels
    plt.rcParams['axes.titlesize'] = 16
    plt.rcParams['axes.titleweight'] = 'bold'
    plt.rcParams['axes.titlecolor'] = PERIOSPOT_COLORS['periospot_blue']
    plt.rcParams['axes.labelsize'] = 12
    plt.rcParams['axes.labelcolor'] = PERIOSPOT_COLORS['mystic_blue']
    
    # Tick labels
    plt.rcParams['xtick.labelsize'] = 10
    plt.rcParams['ytick.labelsize'] = 10
    plt.rcParams['xtick.color'] = PERIOSPOT_COLORS['mystic_blue']
    plt.rcParams['ytick.color'] = PERIOSPOT_COLORS['mystic_blue']
    
    # Axes
    plt.rcParams['axes.edgecolor'] = PERIOSPOT_COLORS['mystic_blue']
    plt.rcParams['axes.linewidth'] = 1.2
    plt.rcParams['axes.spines.top'] = False
    plt.rcParams['axes.spines.right'] = False
    
    # Grid
    plt.rcParams['axes.grid'] = True
    plt.rcParams['grid.alpha'] = 0.3
    plt.rcParams['grid.color'] = PERIOSPOT_COLORS['mystic_blue']
    plt.rcParams['grid.linestyle'] = '--'
    
    # Figure
    plt.rcParams['figure.facecolor'] = 'white'
    plt.rcParams['axes.facecolor'] = 'white'
    plt.rcParams['figure.figsize'] = (10, 6)
    plt.rcParams['figure.dpi'] = 100
    plt.rcParams['savefig.dpi'] = 150
    plt.rcParams['savefig.bbox'] = 'tight'
    
    # Legend
    plt.rcParams['legend.frameon'] = True
    plt.rcParams['legend.framealpha'] = 0.9
    plt.rcParams['legend.edgecolor'] = PERIOSPOT_COLORS['mystic_blue']
    
    # Color cycle for plots
    plt.rcParams['axes.prop_cycle'] = plt.cycler(color=PERIOSPOT_PALETTE[:4])
    
    return {
        'font_family': font_family,
        'colors': PERIOSPOT_COLORS,
        'palette': PERIOSPOT_PALETTE,
    }


# =============================================================================
# CONVENIENCE FUNCTIONS
# =============================================================================

def get_color(name):
    """
    Get a Periospot color by name.
    
    Parameters
    ----------
    name : str
        Color name (e.g., 'periospot_blue', 'crimson_blaze')
    
    Returns
    -------
    str
        Hex color code.
    """
    return PERIOSPOT_COLORS.get(name, PERIOSPOT_COLORS['periospot_blue'])


def apply_periospot_title(ax, title, subtitle=None):
    """
    Apply a styled title to an axes.
    
    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The axes to add the title to.
    title : str
        Main title text.
    subtitle : str, optional
        Subtitle text (displayed below main title).
    """
    ax.set_title(title, fontweight='bold', color=PERIOSPOT_COLORS['periospot_blue'])
    
    if subtitle:
        ax.text(
            0.5, 1.02, subtitle,
            transform=ax.transAxes,
            ha='center', va='bottom',
            fontsize=10,
            color=PERIOSPOT_COLORS['mystic_blue'],
            style='italic'
        )


# =============================================================================
# QUICK TEST
# =============================================================================

if __name__ == '__main__':
    # Quick test of the style
    import numpy as np
    
    setup_periospot_style()
    
    # Create a sample plot
    fig, ax = plt.subplots()
    
    x = np.linspace(0, 10, 100)
    ax.plot(x, np.sin(x), label='Implant Success Rate', linewidth=2)
    ax.plot(x, np.cos(x), label='Bone Density', linewidth=2)
    
    ax.set_xlabel('Time (years)')
    ax.set_ylabel('Normalized Value')
    ax.set_title('Sample Periospot Chart')
    ax.legend()
    
    plt.tight_layout()
    plt.savefig('test_periospot_style.png')
    print("✓ Test chart saved to test_periospot_style.png")

