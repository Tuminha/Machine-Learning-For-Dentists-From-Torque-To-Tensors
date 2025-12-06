"""
Periospot Visual Style for Machine Learning For Dentists
=========================================================

This module provides consistent styling for all matplotlib charts
using Periospot brand colors and Bariol font family.

Usage:
    from utils.periospot_style import setup_periospot_style, PERIOSPOT_COLORS
    
    # Apply the style (call once at the start of your notebook)
    setup_periospot_style()
    
    # Access colors
    color = PERIOSPOT_COLORS['periospot_blue']
    
    # Use typography helpers
    from utils.periospot_style import get_font_props
    title_font = get_font_props('h1')
"""

import matplotlib.pyplot as plt
from matplotlib import font_manager
from matplotlib.font_manager import FontProperties
from pathlib import Path
import json
import warnings

# =============================================================================
# FIND PROJECT ROOT AND LOAD CONFIG
# =============================================================================

def _find_project_root():
    """Find the project root directory."""
    possible_roots = [
        Path.cwd(),
        Path.cwd().parent,
        Path(__file__).parent.parent,
    ]
    
    for root in possible_roots:
        if (root / 'brand_palette.json').exists():
            return root
        if (root / 'AGENT_GUIDE.md').exists():
            return root
    
    return Path(__file__).parent.parent


PROJECT_ROOT = _find_project_root()
FONTS_DIR = PROJECT_ROOT / 'assets' / 'fonts'

# =============================================================================
# LOAD BRAND PALETTE
# =============================================================================

def _load_brand_palette():
    """Load the brand palette from JSON."""
    palette_file = PROJECT_ROOT / 'brand_palette.json'
    
    if palette_file.exists():
        with open(palette_file, 'r') as f:
            return json.load(f)
    else:
        # Fallback defaults
        return {
            'colors': {
                'periospot_blue': '#15365a',
                'mystic_blue': '#003049',
                'periospot_red': '#6c1410',
                'crimson_blaze': '#a92a2a',
                'vanilla_cream': '#f7f0da',
                'black': '#000000',
                'white': '#ffffff',
            }
        }


BRAND_PALETTE = _load_brand_palette()

# =============================================================================
# PERIOSPOT BRAND COLORS
# =============================================================================

PERIOSPOT_COLORS = BRAND_PALETTE.get('colors', {})

# Color palette for sequential data (plots with multiple series)
PERIOSPOT_PALETTE = [
    PERIOSPOT_COLORS.get('periospot_blue', '#15365a'),
    PERIOSPOT_COLORS.get('crimson_blaze', '#a92a2a'),
    PERIOSPOT_COLORS.get('periospot_bright_blue', '#1040dd'),
    PERIOSPOT_COLORS.get('periospot_yellow', '#ffc430'),
    PERIOSPOT_COLORS.get('mystic_blue', '#003049'),
    PERIOSPOT_COLORS.get('periospot_light_blue', '#0297ed'),
]

# =============================================================================
# FONT MANAGEMENT
# =============================================================================

# Store registered fonts
_REGISTERED_FONTS = {}

def _register_bariol_fonts():
    """Register all Bariol font variants with matplotlib."""
    global _REGISTERED_FONTS
    
    font_config = BRAND_PALETTE.get('fonts', {})
    font_files = font_config.get('files', {})
    
    for weight_name, filename in font_files.items():
        font_path = FONTS_DIR / filename
        if font_path.exists():
            try:
                font_manager.fontManager.addfont(str(font_path))
                prop = FontProperties(fname=str(font_path))
                font_name = prop.get_name()
                _REGISTERED_FONTS[weight_name] = {
                    'path': font_path,
                    'name': font_name,
                    'properties': prop,
                }
            except Exception as e:
                warnings.warn(f"Could not load font {filename}: {e}")
    
    return len(_REGISTERED_FONTS) > 0


def get_font_props(style='body'):
    """
    Get FontProperties for a specific typography style.
    
    Parameters
    ----------
    style : str
        One of: 'h1', 'h2', 'h3', 'body', 'caption', 'label',
        'chart_title', 'axis_title', 'tick_labels', 'legend', 'annotation'
    
    Returns
    -------
    FontProperties
        Matplotlib FontProperties object configured for the style.
    
    Example
    -------
    >>> ax.set_title('My Title', fontproperties=get_font_props('h1'))
    """
    # Get typography config
    typography = BRAND_PALETTE.get('typography', {})
    matplotlib_typo = BRAND_PALETTE.get('matplotlib', {})
    
    # Check matplotlib styles first, then general typography
    if style in matplotlib_typo:
        config = matplotlib_typo[style]
    elif style in typography:
        config = typography[style]
    else:
        config = typography.get('body', {'font_weight': 'regular', 'size': 11})
    
    # Map weight to font file
    weight = config.get('font_weight', config.get('weight', 'regular'))
    size = config.get('size', 11)
    
    # Get the font path for this weight
    if weight in _REGISTERED_FONTS:
        return FontProperties(
            fname=str(_REGISTERED_FONTS[weight]['path']),
            size=size
        )
    elif 'regular' in _REGISTERED_FONTS:
        return FontProperties(
            fname=str(_REGISTERED_FONTS['regular']['path']),
            size=size,
            weight=weight
        )
    else:
        # Fallback to system font
        return FontProperties(size=size, weight=weight)


def get_style_color(style='body'):
    """
    Get the color for a typography style.
    
    Parameters
    ----------
    style : str
        Typography style name.
    
    Returns
    -------
    str
        Hex color code.
    """
    typography = BRAND_PALETTE.get('typography', {})
    matplotlib_typo = BRAND_PALETTE.get('matplotlib', {})
    
    if style in matplotlib_typo:
        color_name = matplotlib_typo[style].get('color', 'black')
    elif style in typography:
        color_name = typography[style].get('color', 'black')
    else:
        color_name = 'black'
    
    return PERIOSPOT_COLORS.get(color_name, color_name)


# =============================================================================
# MAIN SETUP FUNCTION
# =============================================================================

def setup_periospot_style():
    """
    Apply Periospot visual style to matplotlib.
    
    This function:
    1. Registers all Bariol font variants
    2. Sets the color palette to Periospot brand colors
    3. Configures chart aesthetics for clean, professional output
    
    Returns
    -------
    dict
        Configuration info including loaded fonts and colors.
    
    Example
    -------
    >>> from utils.periospot_style import setup_periospot_style
    >>> config = setup_periospot_style()
    >>> print(f"Loaded {config['fonts_loaded']} font variants")
    """
    
    # Register fonts
    fonts_loaded = _register_bariol_fonts()
    
    if fonts_loaded:
        # Get the primary font name (from regular weight)
        if 'regular' in _REGISTERED_FONTS:
            primary_font = _REGISTERED_FONTS['regular']['name']
        else:
            primary_font = list(_REGISTERED_FONTS.values())[0]['name']
        print(f"✓ Loaded Bariol font family ({len(_REGISTERED_FONTS)} variants)")
    else:
        primary_font = 'DejaVu Sans'
        print(f"⚠ Bariol fonts not found. Using: {primary_font}")
        print(f"  (Add Bariol OTF files to assets/fonts/ for brand fonts)")
    
    # Get matplotlib config
    mpl_config = BRAND_PALETTE.get('matplotlib', {})
    
    # ==========================================================================
    # MATPLOTLIB CONFIGURATION
    # ==========================================================================
    
    # Font settings
    plt.rcParams['font.family'] = primary_font
    plt.rcParams['font.size'] = 11
    
    # Title (chart_title style)
    chart_title = mpl_config.get('chart_title', {})
    plt.rcParams['axes.titlesize'] = chart_title.get('size', 16)
    plt.rcParams['axes.titleweight'] = chart_title.get('weight', 'bold')
    plt.rcParams['axes.titlecolor'] = PERIOSPOT_COLORS.get(
        chart_title.get('color', 'periospot_blue'), '#15365a'
    )
    
    # Axis labels (axis_title style)
    axis_title = mpl_config.get('axis_title', {})
    plt.rcParams['axes.labelsize'] = axis_title.get('size', 12)
    plt.rcParams['axes.labelcolor'] = PERIOSPOT_COLORS.get(
        axis_title.get('color', 'mystic_blue'), '#003049'
    )
    
    # Tick labels (tick_labels style)
    tick_labels = mpl_config.get('tick_labels', {})
    plt.rcParams['xtick.labelsize'] = tick_labels.get('size', 10)
    plt.rcParams['ytick.labelsize'] = tick_labels.get('size', 10)
    plt.rcParams['xtick.color'] = PERIOSPOT_COLORS.get(
        tick_labels.get('color', 'mystic_blue'), '#003049'
    )
    plt.rcParams['ytick.color'] = PERIOSPOT_COLORS.get(
        tick_labels.get('color', 'mystic_blue'), '#003049'
    )
    
    # Legend
    legend_config = mpl_config.get('legend', {})
    plt.rcParams['legend.fontsize'] = legend_config.get('size', 10)
    
    # Axes styling
    plt.rcParams['axes.edgecolor'] = PERIOSPOT_COLORS.get('mystic_blue', '#003049')
    plt.rcParams['axes.linewidth'] = 1.2
    plt.rcParams['axes.spines.top'] = False
    plt.rcParams['axes.spines.right'] = False
    
    # Grid
    plt.rcParams['axes.grid'] = True
    plt.rcParams['grid.alpha'] = 0.3
    plt.rcParams['grid.color'] = PERIOSPOT_COLORS.get('mystic_blue', '#003049')
    plt.rcParams['grid.linestyle'] = '--'
    
    # Figure
    plt.rcParams['figure.facecolor'] = 'white'
    plt.rcParams['axes.facecolor'] = 'white'
    plt.rcParams['figure.figsize'] = (10, 6)
    plt.rcParams['figure.dpi'] = 100
    plt.rcParams['savefig.dpi'] = 150
    plt.rcParams['savefig.bbox'] = 'tight'
    
    # Legend styling
    plt.rcParams['legend.frameon'] = True
    plt.rcParams['legend.framealpha'] = 0.9
    plt.rcParams['legend.edgecolor'] = PERIOSPOT_COLORS.get('mystic_blue', '#003049')
    
    # Color cycle for plots
    plt.rcParams['axes.prop_cycle'] = plt.cycler(color=PERIOSPOT_PALETTE)
    
    return {
        'fonts_loaded': len(_REGISTERED_FONTS),
        'font_variants': list(_REGISTERED_FONTS.keys()),
        'primary_font': primary_font,
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
    return PERIOSPOT_COLORS.get(name, PERIOSPOT_COLORS.get('periospot_blue', '#15365a'))


def style_title(ax, title, level='h1'):
    """
    Apply styled title to an axes using typography rules.
    
    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The axes to style.
    title : str
        Title text.
    level : str
        Typography level: 'h1', 'h2', 'h3', or 'chart_title'
    """
    font_props = get_font_props(level)
    color = get_style_color(level)
    ax.set_title(title, fontproperties=font_props, color=color)


def style_labels(ax, xlabel=None, ylabel=None):
    """
    Apply styled axis labels.
    
    Parameters
    ----------
    ax : matplotlib.axes.Axes
        The axes to style.
    xlabel : str, optional
        X-axis label.
    ylabel : str, optional
        Y-axis label.
    """
    font_props = get_font_props('axis_title')
    color = get_style_color('axis_title')
    
    if xlabel:
        ax.set_xlabel(xlabel, fontproperties=font_props, color=color)
    if ylabel:
        ax.set_ylabel(ylabel, fontproperties=font_props, color=color)


def create_styled_figure(nrows=1, ncols=1, figsize=None, **kwargs):
    """
    Create a figure with Periospot styling applied.
    
    Parameters
    ----------
    nrows : int
        Number of subplot rows.
    ncols : int
        Number of subplot columns.
    figsize : tuple, optional
        Figure size (width, height) in inches.
    **kwargs
        Additional arguments passed to plt.subplots()
    
    Returns
    -------
    fig, ax : tuple
        Figure and axes objects.
    """
    if figsize is None:
        figsize = (10, 6) if nrows == 1 and ncols == 1 else (12, 4 * nrows)
    
    fig, ax = plt.subplots(nrows, ncols, figsize=figsize, **kwargs)
    fig.set_facecolor('white')
    
    return fig, ax


# =============================================================================
# TYPOGRAPHY REFERENCE
# =============================================================================

def print_typography_guide():
    """Print a reference guide for the typography system."""
    print("\n" + "="*60)
    print("PERIOSPOT TYPOGRAPHY GUIDE")
    print("="*60)
    
    typography = BRAND_PALETTE.get('typography', {})
    
    print("\n📝 TEXT STYLES (for documents/markdown):\n")
    for style, config in typography.items():
        weight = config.get('font_weight', 'regular')
        size = config.get('size', 11)
        color = config.get('color', 'black')
        desc = config.get('description', '')
        print(f"  {style:12} │ {weight:8} │ {size:2}pt │ {color:20} │ {desc}")
    
    mpl_config = BRAND_PALETTE.get('matplotlib', {})
    
    print("\n📊 CHART STYLES (for matplotlib):\n")
    for style, config in mpl_config.items():
        weight = config.get('weight', 'regular')
        size = config.get('size', 11)
        color = config.get('color', 'black')
        print(f"  {style:15} │ {weight:8} │ {size:2}pt │ {color}")
    
    print("\n" + "="*60)
    print("Usage: get_font_props('style_name') → FontProperties")
    print("       get_style_color('style_name') → hex color")
    print("="*60 + "\n")


# =============================================================================
# QUICK TEST
# =============================================================================

if __name__ == '__main__':
    import numpy as np
    
    # Setup and print info
    config = setup_periospot_style()
    print(f"\nFont variants loaded: {config['font_variants']}")
    
    # Print typography guide
    print_typography_guide()
    
    # Create a sample plot
    fig, ax = create_styled_figure()
    
    x = np.linspace(0, 10, 100)
    ax.plot(x, np.sin(x), label='Implant Success', linewidth=2)
    ax.plot(x, np.cos(x), label='Bone Density', linewidth=2)
    ax.plot(x, np.sin(x) * 0.5 + 0.5, label='Healing Progress', linewidth=2)
    
    style_title(ax, 'Periospot Chart Example', level='chart_title')
    style_labels(ax, xlabel='Time (months)', ylabel='Normalized Value')
    ax.legend()
    
    plt.tight_layout()
    plt.savefig('test_periospot_style.png')
    print("\n✓ Test chart saved to test_periospot_style.png")
