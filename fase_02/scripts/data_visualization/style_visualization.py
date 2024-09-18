# style_visualization.py

import matplotlib.pyplot as plt
import matplotlib as mpl
import seaborn as sns
import warnings
import pandas as pd
from scripts.utils.custom_exceptions import CustomException
import sys


def filter_warnings():
    """
    Filter out warnings to prevent cluttering the output during data analysis.
    """
    try:
        warnings.filterwarnings('ignore')
    except Exception as e:
        raise CustomException(f"Error while filtering warnings: {e}", sys)


def setup_matplotlib():
    """
    Set the style and general configurations for Matplotlib visualizations.

    - Applies the 'ggplot' style.
    - Customizes parameters like axis face color, line width, tick colors, grid color, and figure resolution.
    """
    try:
        mpl.style.use('ggplot')  # Set 'ggplot' style for a clean and clear design

        # Customizing the appearance of plots
        mpl.rcParams['axes.facecolor'] = 'white'  # Set the background color of the plots to white
        mpl.rcParams['axes.linewidth'] = 1  # Set axis line width to 1
        mpl.rcParams['xtick.color'] = 'black'  # Set X-axis tick color to black
        mpl.rcParams['ytick.color'] = 'black'  # Set Y-axis tick color to black
        mpl.rcParams['grid.color'] = 'lightgray'  # Set the grid color to light gray
        mpl.rcParams['figure.dpi'] = 150  # Set the resolution of the figures to 150 DPI
        mpl.rcParams['axes.grid'] = True  # Enable the grid in all plots
        mpl.rcParams['font.size'] = 12  # Set the font size to 12 for all text elements
        mpl.rcParams['figure.figsize'] = (8, 4)  # Set the default figure size to 10x6 inches

    except Exception as e:
        raise CustomException(f"Error in setting up Matplotlib configurations: {e}", sys)


def set_color_palette(palette=None):
    """
    Set a custom color palette for Seaborn visualizations.

    Args:
    palette (list, optional): A list of hex color codes to define a custom palette. 
                              If None, a default 'Blues' palette will be used.
    """
    try:
        if palette:
            sns.set_palette(sns.color_palette(palette))  # Apply the custom palette
        else:
            sns.set_palette('Blues')  # Default to the 'Blues' palette

        # Display the palette to confirm it is applied correctly
        sns.palplot(sns.color_palette(palette))

    except Exception as e:
        raise CustomException(f"Error in setting Seaborn color palette: {e}", sys)

    return sns.color_palette(palette)


def activate_inline_visualization():
    """
    Ensure that Matplotlib visualizations appear inline in Jupyter Notebooks.
    This function checks if the code is running in a Jupyter environment.
    """
    try:
        if 'get_ipython' in globals():  # Check if the code is running in a Jupyter environment
            get_ipython().run_line_magic('matplotlib', 'inline')
        else:
            print("Warning: get_ipython not available. Inline visualization is not necessary in VSCode.")
    except Exception as e:
        raise CustomException(f"Error in activating inline visualization: {e}", sys)



def set_pandas_options():
    """
    Configure display options for pandas to control the output of large DataFrames.
    """
    try:
        pd.set_option('display.max_rows', None)  # Show all rows
        pd.set_option('display.max_info_rows', 100)  # Show up to 100 rows in info()
        pd.set_option('display.max_columns', None)  # Show all columns
        pd.set_option('display.width', 1000)  # Set display width

    except Exception as e:
        raise CustomException(f"Error in setting Pandas display options: {e}", sys)


def configure_visualization(palette=None):
    """
    A helper function that configures the entire visualization environment.

    - Filters warnings.
    - Sets up Matplotlib with the defined style and parameters.
    - Activates inline plotting for Jupyter environments.
    - Sets the Seaborn color palette, either custom or default.
    - Configures pandas display options for better output in large datasets.

    Args:
    palette (list, optional): A list of hex color codes to define a custom palette. 
                              If None, a default 'Blues' palette will be used.
    """
    try:
        filter_warnings()
        setup_matplotlib()
        activate_inline_visualization()
        set_color_palette(palette)
        set_pandas_options()

    except Exception as e:
        raise CustomException(f"Error during visualization configuration: {e}", sys)


    