# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 12:43:12 2024

@author: joluh
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Configurar la fuente globalmente
plt.rcParams['font.family'] = 'Palatino Linotype'
plt.rcParams['font.size'] = 14

# Cargar los datos desde el archivo Excel
file_path = 'Evapo.xlsx'
data = pd.read_excel(file_path)

# Definir las etiquetas personalizadas para los tratamientos
labels = ['CF', 'AWD$_{5}$', 'AWD$_{10}$', 'AWD$_{20}$']

# Función para eliminar outliers
def remove_outliers(data):
    Q1 = np.percentile(data.dropna(), 25)  # Ignorar NaN en el cálculo
    Q3 = np.percentile(data.dropna(), 75)
    IQR = Q3 - Q1
    lower_fence = Q1 - 1.5 * IQR
    upper_fence = Q3 + 1.5 * IQR
    return data[(data >= lower_fence) & (data <= upper_fence)]

# Crear la figura y los ejes
fig, ax = plt.subplots(figsize=(10, 6))

# Eliminar outliers y preparar los datos para el boxplot
datos_clean = [remove_outliers(data[col].dropna()) for col in data.columns]

# Graficar el boxplot sin outliers
ax.boxplot(datos_clean, patch_artist=True, showfliers=False,
           boxprops=dict(facecolor='#E3E3E3', color='black'),
           whiskerprops=dict(color='#6D6D6D'), capprops=dict(color='#6D6D6D'),
           medianprops=dict(color='#0072B2'))

# Calcular medias para la línea de tendencia
medias = [d.mean() for d in datos_clean]

# Graficar la línea de tendencia
ax.plot(range(1, len(labels) + 1), medias, marker='o', color='#D55E00', linestyle='-', 
        linewidth=1.0, markersize=5, label='Mean')

# Configurar las etiquetas de los ejes
ax.set_ylabel('Evapotranspiration (mm d$^{-1}$)')
ax.set_xticklabels(labels)

# Configurar los límites del eje y (ajusta según sea necesario)
ax.set_ylim(2, 8)

# Añadir leyenda para la línea de tendencia
ax.legend()

# Guardar la imagen con 600 dpi
plt.savefig('Evapo_grafico_boxplot.png', dpi=600, bbox_inches='tight', pad_inches=0.1)

# Mostrar la gráfica
plt.show()

