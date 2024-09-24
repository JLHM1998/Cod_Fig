# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 17:00:58 2024
@author: joluh
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D

# Configurar la fuente globalmente
plt.rcParams['font.family'] = 'Palatino Linotype'
plt.rcParams['font.size'] = 12

# Cargar los datos desde el archivo Excel
file_path = 'ETo.xlsx'
df = pd.read_excel(file_path)

# Crear la figura y subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 10))

# Definir los marcadores para cada DPS
markers = ['o', 's', 'D', '^', 'v', '<', '>']

# Graficar para la fase vegetativa
vegetative_DPS = ['38_DPS', '61_DPS', '65_DPS', '75_DPS', '79_DPS', '88_DPS', '92_DPS']
for i, dps in enumerate(vegetative_DPS):
    ax1.plot(df['Prom_Hours(ETc)'], df[dps], marker=markers[i], linestyle='--', linewidth=0.5, 
             label=dps.replace('_DPS', ' DPS'), color='yellowgreen', markersize=4)  # Modificar etiqueta

ax1.set_ylabel('ET$_{0}$ (mm h$^{-1}$)')
ax1.set_xlim(0, 25)
ax1.set_xticks(range(1, 25))  # Mantiene los ticks, pero elimina las etiquetas
ax1.set_xticklabels([])  # Elimina las etiquetas del eje X
ax1.text(0.97, 0.95, 'a)', transform=ax1.transAxes, fontsize=14, fontweight='bold', va='top', ha='right')

# Crear línea personalizada para la leyenda de Vegetative
line_vegetative = Line2D([0], [0], color='yellowgreen', lw=1, linestyle='--')

# Agregar la leyenda original para los DPS
legend1 = ax1.legend(loc='upper left')

# Crear y agregar la leyenda adicional para Vegetative
legend2 = ax1.legend([line_vegetative], ['Vegetative'], loc='center right', title="Phase", bbox_to_anchor=(0.96, 0.7))

# Añadir la primera leyenda de nuevo
ax1.add_artist(legend1)

# Graficar para las fases de maduración y maduración tardía
maturation_DPS = ['103_DPS', '107_DPS', '123_DPS', '127_DPS']
ripening_DPS = ['147_DPS', '149_DPS']

# Graficar la fase de maduración con diferentes marcadores
for i, dps in enumerate(maturation_DPS):
    ax2.plot(df['Prom_Hours(ETc)'], df[dps], marker=markers[i], linestyle='--', linewidth=0.5, 
             label=dps.replace('_DPS', ' DPS'), color='orange', markersize=4)  # Modificar etiqueta

# Graficar la fase de maduración tardía con diferentes marcadores
for i, dps in enumerate(ripening_DPS):
    ax2.plot(df['Prom_Hours(ETc)'], df[dps], marker=markers[i + len(maturation_DPS)], linestyle='--', 
             linewidth=0.5, label=dps.replace('_DPS', ' DPS'), color='dimgrey', markersize=4)  # Modificar etiqueta

ax2.set_xlabel('Hours in the day')
ax2.set_ylabel('ET$_{0}$ (mm h$^{-1}$)')
ax2.set_xlim(0, 25)
ax2.set_xticks(range(1, 25))
ax2.text(0.97, 0.95, 'b)', transform=ax2.transAxes, fontsize=14, fontweight='bold', va='top', ha='right')

# Crear líneas personalizadas para las leyendas de Maturation y Ripening
line_maturation = Line2D([0], [0], color='orange', lw=1, linestyle='--')
line_ripening = Line2D([0], [0], color='dimgrey', lw=1, linestyle='--')

# Agregar la leyenda original para los DPS
legend3 = ax2.legend(loc='upper left')

# Crear y agregar las leyendas adicionales para Maturation y Ripening
legend4 = ax2.legend([line_maturation, line_ripening], ['Reproductive', 'Ripening'], loc='center right', title="Phases", bbox_to_anchor=(0.96, 0.7))

# Añadir la primera leyenda de nuevo
ax2.add_artist(legend3)

# Ajustar los márgenes y guardar la figura
plt.tight_layout(pad=1.0)
plt.savefig('ETo_figure.png', dpi=600, bbox_inches='tight', pad_inches=0.1)
plt.show()
