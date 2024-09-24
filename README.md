Thesis Articles: ETc Code Figures
=====================================

This repository contains Python code for generating figures used in the thesis articles related to Evapotranspiration (ETc) studies. The code is organized into separate files for each figure, and each file includes comments to explain the purpose and functionality of the code.

Figures
The following figures are included in this repository:

LAI_NDVI.py: Generates a scatter plot of Leaf Area Index (LAI) vs. Normalized Difference Vegetation Index (NDVI) with exponential curve fitting.
CC2.py and CC.py: Generate scatter plots of Crop Coefficient (CC) simulated vs. measured values with linear regression lines.
ETo.py: Generates a plot of ET0 (reference evapotranspiration) vs. hours in the day.
ETc_Simulated.py: Generates a scatter plot of ETc (crop evapotranspiration) simulated vs. measured values with linear regression lines.
Irrigation.py: Generates a plot of cumulative irrigation vs. days post sowing (DPS) for different treatments.
Boxplot_H.py, Boxplot_LE.py, and Boxplot_Rn.py: Generate box plots of H (sensible heat flux), LE (latent heat flux), and Rn (net radiation) values for different treatments.
Requirements
Python 3.x
NumPy
Pandas
Matplotlib
Scipy
Usage
Clone the repository to your local machine.
Install the required libraries by running pip install -r requirements.txt.
Run each Python file to generate the corresponding figure. For example, python LAI_NDVI.py will generate the LAI vs. NDVI scatter plot.
The figures will be saved as PNG files in the same directory as the Python files.
Notes
The data files used to generate the figures are not included in this repository. You will need to provide your own data files or modify the code to use different data sources.
The code is written in Python 3.x and may not be compatible with earlier versions of Python.
The figures are generated using Matplotlib, which may have different rendering results depending on the system and environment used.