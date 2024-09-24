# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 11:24:38 2024

@author: joluh
"""

import matplotlib.pyplot as plt
import numpy as np

# Configurar la fuente globalmente
plt.rcParams['font.family'] = 'Palatino Linotype'
plt.rcParams['font.size'] = 12

# Colores para revistas Q1
field_color = '#1f77b4'   # Azul oscuro
aquacrop_color = '#ff7f0e' # Naranja oscuro

# Data
treatments = ['CF', 'AWD$_{5}$', 'AWD$_{10}$', 'AWD$_{20}$']
field_yield = [14.012, 11.853, 13.722, 12.912]
aquacrop_yield = [14.143, 12.467, 12.284, 10.542]

# Bar chart
x = np.arange(len(treatments))
width = 0.35

fig, ax = plt.subplots(figsize=(8, 6))
bars1 = ax.bar(x - width/2, field_yield, width, label='Field (14% moisture)', color=field_color)
bars2 = ax.bar(x + width/2, aquacrop_yield, width, label='AquaCrop Simulated (14% moisture)', color=aquacrop_color)

# Labels and title
#ax.set_xlabel('Treatments')
ax.set_ylabel('Yield (kg ha$^{-1}$)')
#ax.set_title('Comparison of Measured vs AquaCrop Simulated Yield')
ax.set_xticks(x)
ax.set_xticklabels(treatments)

# Ajustar los límites del eje Y para crear más espacio en la parte superior
ax.set_ylim(0, 17)

# Ubicar la leyenda dentro del gráfico, en la esquina superior derecha
ax.legend(loc='upper right', fontsize=10)

# Add value labels on bars
for bar in bars1:
    height = bar.get_height()
    ax.annotate(f'{height:.2f}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),  # 3 points of vertical offset
                textcoords="offset points",
                ha='center', va='bottom')

for bar in bars2:
    height = bar.get_height()
    ax.annotate(f'{height:.2f}',
                xy=(bar.get_x() + bar.get_width() / 2, height),
                xytext=(0, 3),
                textcoords="offset points",
                ha='center', va='bottom')

# Guardar la figura
plt.savefig('Yield_Comparison_Field_vs_AquaCrop.png', dpi=600, bbox_inches='tight', pad_inches=0.1)
plt.show()


