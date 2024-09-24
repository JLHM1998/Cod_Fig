# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 09:54:36 2024

@author: joluh
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import matplotlib.cm as cm

# Configurar la fuente globalmente
plt.rcParams['font.family'] = 'Palatino Linotype'
plt.rcParams['font.size'] = 12

# Cargar los datos desde el archivo de Excel
file_path = 'NDVI_IAF.xlsx'
data = pd.read_excel(file_path)

# Definir la función de ajuste exponencial
def exp_func(x, a, b):
    return a * np.exp(b * x)

# Generar una paleta de colores basada en el número de grupos únicos de DPS
unique_dps = data['DPS'].unique()
num_colors = len(unique_dps)
colors = cm.viridis(np.linspace(0, 1, num_colors))

# Preparar la figura
plt.figure(figsize=(8, 6))

# Almacenar todos los datos juntos para la regresión final
all_ndvi = []
all_lai = []

# Iterar sobre cada grupo de DPS único
for i, (dps, group) in enumerate(data.groupby('DPS')):
    ndvi = group['NDVI_Green_Seacker']
    lai = group['IAF_Extractive_Method']
    
    all_ndvi.extend(ndvi)
    all_lai.extend(lai)
    
    # Ajustar la curva para cada subconjunto de datos
    params, covariance = curve_fit(exp_func, ndvi, lai)
    
    # Crear la gráfica de dispersión
    plt.scatter(ndvi, lai, color=colors[i], label=f'{dps} DPS')
    
    # Dibujar la curva ajustada
    ndvi_fit = np.linspace(min(ndvi), max(ndvi), 100)
    lai_fit = exp_func(ndvi_fit, *params)
    plt.plot(ndvi_fit, lai_fit, color=colors[i], linestyle='--', 
             label=f'$y = {params[0]:.4f}e^{{{params[1]:.4f}x}}$\n$R^2 = {1 - np.sum((lai - exp_func(ndvi, *params))**2) / np.sum((lai - np.mean(lai))**2):.4f}$')

# Convertir todos los datos a numpy array para la regresión final
all_ndvi = np.array(all_ndvi)
all_lai = np.array(all_lai)

# Ajustar la curva de regresión final con todos los datos
final_params, final_covariance = curve_fit(exp_func, all_ndvi, all_lai)

# Dibujar la curva de regresión final
ndvi_fit_all = np.linspace(min(all_ndvi), max(all_ndvi), 100)
lai_fit_all = exp_func(ndvi_fit_all, *final_params)
plt.plot(ndvi_fit_all, lai_fit_all, color='black', linestyle='-', linewidth=2,
         label=f'**$y = {final_params[0]:.4f}e^{{{final_params[1]:.4f}x}}$**\n**$R^2 = {1 - np.sum((all_lai - exp_func(all_ndvi, *final_params))**2) / np.sum((all_lai - np.mean(all_lai))**2):.4f}$**')

# Personalizar la gráfica
plt.xlabel('NDVI')
plt.ylabel('LAI (m$^{2}$ / m$^{2}$)')
plt.xlim(0.3, 0.81)
plt.ylim(-0.2, 6)

# Ajustar la leyenda para que se muestre dentro del área de la gráfica
plt.legend(loc='upper left', fontsize=10, frameon=True, ncol=2, columnspacing=1)

# Guardar la imagen con 600 dpi y sin espacios en blanco alrededor
plt.savefig('ndvi_lai_plot_final.png', dpi=600, bbox_inches='tight', pad_inches=0.1)

# Mostrar la gráfica
plt.show()



