# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 12:12:30 2024

@author: joluh
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Configurar la fuente globalmente
plt.rcParams['font.family'] = 'Palatino Linotype'
plt.rcParams['font.size'] = 12

# Cargar el archivo de Excel
file_path = 'CC.xlsx'  # Cambia esto a la ruta donde esté tu archivo
data = pd.read_excel(file_path)

# Crear un diccionario de colores para los tratamientos
treatment_colors = {
    'CF': 'blue',
    'AWD5': 'green',
    'AWD10': 'gold',
    'AWD20': 'red'
}

# Crear un diccionario para las etiquetas con subíndices
treatment_labels = {
    'CF': 'CF',
    'AWD5': 'AWD$_5$',
    'AWD10': 'AWD$_{10}$',
    'AWD20': 'AWD$_{20}$'
}

# Función para calcular el coeficiente de determinación R^2
def calculate_r_squared(x, y):
    coeffs = np.polyfit(x, y, 1)
    y_pred = np.polyval(coeffs, x)
    residuals = y - y_pred
    ss_res = np.sum(residuals**2)
    ss_tot = np.sum((y - np.mean(y))**2)
    return 1 - (ss_res / ss_tot)

# Crear un gráfico de dispersión
plt.figure(figsize=(10, 8))

# Listas para manejar las leyendas
handles = []
labels = []

# Graficar los datos y ajustar líneas de regresión para cada tratamiento en el orden deseado
for treatment in ['CF', 'AWD5', 'AWD10', 'AWD20']:
    group_data = data[data['Treatments'] == treatment]
    plt.scatter(group_data['SIM'], group_data['OBS'], 
                color=treatment_colors[treatment], label=treatment)
    
    # Realizar regresión lineal para cada tratamiento
    coeffs = np.polyfit(group_data['SIM'], group_data['OBS'], 1)
    x_vals = np.linspace(min(group_data['SIM']), max(group_data['SIM']), 100)
    y_vals = np.polyval(coeffs, x_vals)
    plt.plot(x_vals, y_vals, color=treatment_colors[treatment], linestyle='-', linewidth=1)
    
    # Calcular R^2 y obtener la ecuación
    r_squared = calculate_r_squared(group_data['SIM'], group_data['OBS'])
    slope, intercept = coeffs
    equation = f'y = {slope:.2f}x + {intercept:.2f}'
    
    # Agregar a la leyenda
    handles.append(plt.Line2D([0], [0], color=treatment_colors[treatment], lw=1))
    labels.append(f'{treatment_labels[treatment]}:\n$y = {slope:.2f}x + {intercept:.2f}$\n$R^2$ = {r_squared:.2f}')

# Ajustar una línea de regresión general para todos los datos
all_coeffs = np.polyfit(data['SIM'], data['OBS'], 1)
all_x_vals = np.linspace(min(data['SIM']), max(data['SIM']), 100)
all_y_vals = np.polyval(all_coeffs, all_x_vals)
plt.plot(all_x_vals, all_y_vals, color='black', linestyle='--', linewidth=1.5)

# Calcular R^2 para la tendencia general
all_r_squared = calculate_r_squared(data['SIM'], data['OBS'])
all_slope, all_intercept = all_coeffs
all_equation = f'y = {all_slope:.2f}x + {all_intercept:.2f}'

# Agregar a la leyenda
handles.append(plt.Line2D([0], [0], color='black', linestyle='--', lw=1.5))
labels.append(f'Overall Trend:\n$y = {all_slope:.2f}x + {all_intercept:.2f}$\n$R^2$ = {all_r_squared:.2f}')

# Configuración de la gráfica
plt.xlabel('CC simulated (%)')
plt.ylabel('CC measured (%)')

# Ajustar los ejes
plt.xlim(0, 80)
plt.ylim(-5, 80)

# Agregar leyenda dentro de la figura
plt.legend(handles, labels, title='Treatments', loc='upper left', fontsize=11, bbox_to_anchor=(0.02, 0.98))

# Exportar la figura a 600 DPI sin márgenes
plt.savefig('CC2.png', dpi=600, bbox_inches='tight', pad_inches=0.1)

# Mostrar el gráfico
plt.show()
