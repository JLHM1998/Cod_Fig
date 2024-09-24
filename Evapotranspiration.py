# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 16:53:38 2024

@author: joluh
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

# Configurar la fuente globalmente
plt.rcParams['font.family'] = 'Palatino Linotype'
plt.rcParams['font.size'] = 12

# Cargar los datos desde el archivo Excel
file_path = 'Evapotranspiration.xlsx'
df = pd.read_excel(file_path)

# Filtrar los datos por tratamiento
tratamientos = df['Treatments'].unique()

# Crear el gráfico
plt.figure(figsize=(10, 8))

# Colores para cada tratamiento
colores = {
    'CF': 'blue',
    'AWD5': 'green',
    'AWD10': 'gold',
    'AWD20': 'red'
}

# Diccionario para la leyenda con subíndices
legend_labels = {
    'CF': 'CF',
    'AWD5': r'AWD$_{5}$',
    'AWD10': r'AWD$_{10}$',
    'AWD20': r'AWD$_{20}$'
}

# Graficar Evapotranspiración y Transpiración por tratamiento con grosor de línea ajustado
for tratamiento in tratamientos:
    df_trat = df[df['Treatments'] == tratamiento]
    
    # Graficar Evaporación (línea discontinua) con grosor de línea
    plt.plot(df_trat['DPS'], df_trat['Evapo'], linestyle='--', color=colores[tratamiento], linewidth=0.8)
    
    # Graficar Transpiración (línea continua) con grosor de línea
    plt.plot(df_trat['DPS'], df_trat['Trans'], linestyle='-', color=colores[tratamiento], linewidth=0.8)

# Configurar rango del eje X
plt.xlim(30, 156)

# Configurar los ticks del eje X cada 10 unidades
plt.xticks(range(30, 156, 10))

# Crear entradas de la leyenda
evaporation_line = mlines.Line2D([], [], color='black', linestyle='--', linewidth=1, label='Evaporation')
transpiration_line = mlines.Line2D([], [], color='black', linestyle='-', linewidth=1, label='Transpiration')

# Leyenda para tratamientos usando las etiquetas con subíndices
trat_legend = [mlines.Line2D([], [], color=color, linestyle='-', linewidth=1, label=legend_labels[tratamiento]) for tratamiento, color in colores.items()]

# Añadir leyenda personalizada
plt.legend(handles=[evaporation_line, transpiration_line] + trat_legend, loc='upper right')

# Configurar etiquetas y título
plt.xlabel('Days Post Sowing (DPS)')
plt.ylabel('Evapotranspiration and Transpiration (mm d$^{-1}$)')

# Ajustar los márgenes y guardar la figura
plt.tight_layout(pad=1.0)
plt.savefig('Evapotranspiration.png', dpi=600, bbox_inches='tight', pad_inches=0.1)
plt.show()
