# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 01:05:19 2024

@author: joluh
"""

import pandas as pd
import matplotlib.pyplot as plt

# Configurar la fuente globalmente
plt.rcParams['font.family'] = 'Palatino Linotype'
plt.rcParams['font.size'] = 12

# Cargar el archivo Excel
file_path = 'Irrigation.xlsx'
df = pd.read_excel(file_path, sheet_name='Cumulative')

# Definir la columna de DPS y los tratamientos específicos que quieres graficar
dps_column = 'DPS'
phase_column = 'Phase'  # Columna con las fases fenológicas
irrigation_columns = ['CF', 'AWD5', 'AWD10', 'AWD20']  # Tratamientos específicos

# Definir los colores para cada tratamiento
colors = {
    'CF': 'blue',
    'AWD5': 'green',
    'AWD10': 'yellow',
    'AWD20': 'red'
}

# Definir diferentes estilos de línea para las fases fenológicas
line_styles = {
    'Vegetative': 'dotted',
    'Reproductive': 'solid',
    'Ripening': 'dashed',
}

# Crear la figura y los ejes
plt.figure(figsize=(10, 6))

# Graficar las líneas para cada tratamiento y fase
for column in irrigation_columns:
    for phase, style in line_styles.items():
        phase_data = df[df[phase_column] == phase]
        plt.plot(phase_data[dps_column], phase_data[column], color=colors[column], linestyle=style)

# Personalizar etiquetas y leyenda
plt.xlabel('Days Post Sowing (DPS)')
plt.ylabel('Cumulative Irrigation (mm)')

# Crear una leyenda simplificada con subíndices para los tratamientos
legend_labels = {
    'CF': 'CF',
    'AWD5': r'AWD$_{5}$',
    'AWD10': r'AWD$_{10}$',
    'AWD20': r'AWD$_{20}$'
}

# Primera leyenda (tratamientos)
handles_treatment = [plt.Line2D([0], [0], color=colors[col], lw=2, label=legend_labels[col]) for col in irrigation_columns]
plt.legend(handles=handles_treatment, title="Treatment", loc='upper left')

# Segunda leyenda (fases fenológicas)
handles_phase = [plt.Line2D([0], [0], color='black', lw=2, linestyle=line_styles[phase], label=phase) for phase in line_styles]
plt.legend(handles=handles_phase, title="Phenological Phase", loc='lower right')

# Añadir las dos leyendas al gráfico
plt.gca().add_artist(plt.legend(handles=handles_treatment, title="Treatment", loc='upper left'))
plt.legend(handles=handles_phase, title="Phenological Phase", loc='lower right')

plt.grid(False)

# Exportar la figura a 600 DPI sin márgenes
plt.savefig('Irrigation_Cumulative.png', dpi=600, bbox_inches='tight', pad_inches=0.1)

# Mostrar el gráfico
plt.show()
