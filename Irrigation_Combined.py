# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 16:12:36 2024

@author: joluh
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# Configurar la fuente globalmente
plt.rcParams['font.family'] = 'Palatino Linotype'
plt.rcParams['font.size'] = 12

# Cargar el archivo Excel
file_path = 'Irrigation.xlsx'

# Cargar las hojas específicas
df_cumulative = pd.read_excel(file_path, sheet_name='Cumulative')
df_spot = pd.read_excel(file_path, sheet_name='Spot')

# Crear la figura y los subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12), sharex=True)

# Ajustar el eje x en ambos subplots
ax1.set_xlim(20, 140)
ax2.set_xlim(20, 140)

# Graficar los datos de la hoja 'Cumulative'
dps_column = 'DPS'
phase_column = 'Phase'  # Columna con las fases fenológicas
irrigation_columns = ['CF', 'AWD5', 'AWD10', 'AWD20']  # Tratamientos específicos

colors = {
    'CF': 'blue',
    'AWD5': 'green',
    'AWD10': 'gold',
    'AWD20': 'red'
}

line_styles = {
    'Vegetative': 'dotted',
    'Reproductive': 'solid',
    'Ripening': 'dashed',
}

# Graficar las líneas para cada tratamiento y fase
for column in irrigation_columns:
    for phase, style in line_styles.items():
        phase_data = df_cumulative[df_cumulative[phase_column] == phase]
        ax1.plot(phase_data[dps_column], phase_data[column], color=colors[column], linestyle=style)

ax1.set_ylabel('Cumulative Irrigation (m$^{3}$ ha$^{-1}$)')

# Añadir el texto 'a)' en la esquina superior derecha del primer subplot
ax1.text(0.97, 0.92, 'a)', transform=ax1.transAxes, fontsize=14, fontweight='bold', va='top', ha='right')

# Crear leyendas para el gráfico 'Cumulative'
legend_labels = {
    'CF': 'CF',
    'AWD5': r'AWD$_{5}$',
    'AWD10': r'AWD$_{10}$',
    'AWD20': r'AWD$_{20}$'
}

# Primera leyenda (tratamientos)
handles_treatment = [Line2D([0], [0], color=colors[col], lw=2, label=legend_labels[col]) for col in irrigation_columns]

# Segunda leyenda (fases fenológicas)
handles_phase = [Line2D([0], [0], color='black', lw=2, linestyle=line_styles[phase], label=phase) for phase in line_styles]

# Añadir las dos leyendas al gráfico
legend1 = ax1.legend(handles=handles_treatment, title="Treatment", loc='upper left')
ax1.add_artist(legend1)  # Añadir la primera leyenda manualmente para que no se sobrescriba

legend2 = ax1.legend(handles=handles_phase, title="Phenological Phase", loc='lower right')

# Graficar los datos de la hoja 'Spot'
# Definir los estilos de línea y colores para cada tratamiento
phase_colors = {
    'CF': 'blue',
    'AWD5': 'green',
    'AWD10': 'gold',
    'AWD20': 'red'
}
phase_markers = {
    'CF': 'o',
    'AWD5': 's',
    'AWD10': 'D',
    'AWD20': '^'
}

# Filtrar por tratamientos y graficar solo puntos
for treatment, color in phase_colors.items():
    treatment_data = df_spot[['DPS', treatment]]
    ax2.scatter(treatment_data['DPS'], treatment_data[treatment], marker=phase_markers[treatment], color=color, label=treatment, s=35)

# Añadir los puntos específicos de la hoja 'Spot' con marcador negro
spot_points = [38, 61, 65, 75, 79, 88, 92, 103, 107, 123, 127, 147, 149]

# Iterar sobre los puntos específicos y colocarlos a 100 m³ ha⁻¹
for point in spot_points:
    ax2.scatter(point, 100, marker='X', color='black', s=30)  # Altura fija de 100 m³ ha⁻¹

# Añadir la leyenda de los puntos específicos
handles_spot = [Line2D([0], [0], marker='X', color='black', markersize=6, linestyle='None', label='Unmanned Aerial Vehicle (UAV)')]
ax2.legend(handles=handles_spot, loc='upper right')

ax2.set_xlabel('Days Post Sowing (DPS)')
ax2.set_ylabel('Irrigation (m$^{3}$ ha$^{-1}$)')

# Añadir el texto 'b)' en la esquina superior derecha del segundo subplot
ax2.text(0.97, 0.92, 'b)', transform=ax2.transAxes, fontsize=14, fontweight='bold', va='top', ha='right')

# Ajustar los márgenes y guardar la figura
plt.tight_layout(pad=1.0)
plt.savefig('Irrigation_Combined.png', dpi=600, bbox_inches='tight', pad_inches=0.1)
plt.show()
