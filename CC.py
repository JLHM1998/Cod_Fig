# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 01:05:19 2024

@author: joluh
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.lines import Line2D

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

# Función para calcular el coeficiente de correlación R
def calculate_r(x, y):
    coeffs = np.polyfit(x, y, 1)
    y_pred = np.polyval(coeffs, x)
    residuals = y - y_pred
    ss_res = np.sum(residuals**2)
    ss_tot = np.sum((y - np.mean(y))**2)
    return np.sqrt(1 - (ss_res / ss_tot))

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
    
    # Calcular R y obtener la ecuación
    r = calculate_r(group_data['SIM'], group_data['OBS'])
    slope, intercept = coeffs
    equation = f'y = {slope:.2f}x + {intercept:.2f}'
    
    # Agregar a la leyenda
    handles.append(Line2D([0], [0], color=treatment_colors[treatment], lw=1))
    labels.append(f'{treatment_labels[treatment]}:\n$y = {slope:.2f}x + {intercept:.2f}$\n$R$ = {r:.2f}')

# Ajustar una línea de regresión general para todos los datos
all_coeffs = np.polyfit(data['SIM'], data['OBS'], 1)
all_x_vals = np.linspace(min(data['SIM']), max(data['SIM']), 100)
all_y_vals = np.polyval(all_coeffs, all_x_vals)
plt.plot(all_x_vals, all_y_vals, color='black', linestyle='--', linewidth=1.5)

# Calcular R para la tendencia general
all_r = calculate_r(data['SIM'], data['OBS'])
all_slope, all_intercept = all_coeffs
all_equation = f'y = {all_slope:.2f}x + {all_intercept:.2f}'

# Crear línea personalizada para la leyenda de tendencia general
overall_trend_handle = Line2D([0], [0], color='black', linestyle='--', lw=1.5)
overall_trend_label = f'Overall Trend:\n$y = {all_slope:.2f}x + {all_intercept:.2f}$\n$R$ = {all_r:.2f}'

# Configuración de la gráfica
plt.xlabel('CC simulated (%)')
plt.ylabel('CC measured (%)')

# Ajustar los ejes
plt.xlim(0, 80)
plt.ylim(-5, 80)

# Agregar la primera leyenda (tratamientos) en la parte superior izquierda
legend1 = plt.legend(handles, labels, title='Treatments', loc='upper left', fontsize=11, bbox_to_anchor=(0.02, 0.98))

# Agregar la leyenda de la tendencia general en la parte derecha inferior
legend2 = plt.legend([overall_trend_handle], [overall_trend_label], loc='lower right', fontsize=11, bbox_to_anchor=(0.98, 0.02))

# Añadir la primera leyenda de nuevo
plt.gca().add_artist(legend1)

# Exportar la figura a 600 DPI sin márgenes
plt.savefig('CC.png', dpi=600, bbox_inches='tight', pad_inches=0.1)

# Mostrar el gráfico
plt.show()

