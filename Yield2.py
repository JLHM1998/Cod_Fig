import matplotlib.pyplot as plt
import numpy as np

# Configurar la fuente globalmente
plt.rcParams['font.family'] = 'Palatino Linotype'
plt.rcParams['font.size'] = 12

# Colores para revistas Q1
field_color = '#1f77b4'   # Azul oscuro
aquacrop_color = '#ff7f0e' # Naranja oscuro
irrigation_color = 'skyblue' # Verde oscuro para el riego acumulado

# Data
treatments = ['CF', 'AWD$_{5}$', 'AWD$_{10}$', 'AWD$_{20}$']
field_yield = [14.012, 11.853, 13.722, 12.912]
aquacrop_yield = [14.25, 12.84, 13.58, 13.10]  # Ajuste de valores para estar en la misma escala
irrigation = [19971.17, 14268.09, 14340.8, 14468.56]  # Riego acumulado en m3 ha-1

# Bar chart
x = np.arange(len(treatments))
width = 0.35

fig, ax1 = plt.subplots(figsize=(8, 6))

# Gráfico para el Yield
bars1 = ax1.bar(x - width/2, field_yield, width, label='Field (14% moisture)', color=field_color)
bars2 = ax1.bar(x + width/2, aquacrop_yield, width, label='AquaCrop Simulated (14% moisture)', color=aquacrop_color)

# Eje y de la izquierda
ax1.set_ylabel('Yield (kg ha$^{-1}$)')
ax1.set_xticks(x)
ax1.set_xticklabels(treatments)
ax1.set_ylim(0, 18)

# Ubicar la leyenda dentro del gráfico
ax1.legend(loc='upper left', fontsize=10)

# Añadir las etiquetas de valor en las barras
for bar in bars1:
    height = bar.get_height()
    ax1.annotate(f'{height:.2f}',
                 xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 3),
                 textcoords="offset points",
                 ha='center', va='bottom')

for bar in bars2:
    height = bar.get_height()
    ax1.annotate(f'{height:.2f}',
                 xy=(bar.get_x() + bar.get_width() / 2, height),
                 xytext=(0, 3),
                 textcoords="offset points",
                 ha='center', va='bottom')

# Crear un segundo eje y para el riego acumulado
ax2 = ax1.twinx()
ax2.plot(x, irrigation, color=irrigation_color, marker='o', linestyle='-', linewidth=2, label='Irrigation (m$^{3}$ ha$^{-1}$)')

# Eje y de la derecha
ax2.set_ylabel('Irrigation (m$^{3}$ ha$^{-1}$)')
ax2.set_ylim(0, 23000)

# Leyenda para el segundo eje y
ax2.legend(loc='upper right', fontsize=10)

# Guardar la figura
plt.savefig('Yield_Comparison_with_Irrigation.png', dpi=600, bbox_inches='tight', pad_inches=0.1)
plt.show()
