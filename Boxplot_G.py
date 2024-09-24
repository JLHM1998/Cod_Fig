# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Configurar la fuente globalmente
plt.rcParams['font.family'] = 'Palatino Linotype'
plt.rcParams['font.size'] = 16

# Leer los datos desde un archivo Excel
ruta_excel = 'G.xlsx'
df = pd.read_excel(ruta_excel)

# Obtener los tratamientos únicos
tratamientos = df['Tratamientos'].unique()

# Crear un subplot con 4 gráficos (1 fila x 4 columnas)
fig, axs = plt.subplots(1, 4, figsize=(24, 6))  # Ajusta el tamaño según sea necesario

# Función para eliminar outliers
def remove_outliers(data):
    Q1 = np.percentile(data, 25)
    Q3 = np.percentile(data, 75)
    IQR = Q3 - Q1
    lower_fence = Q1 - 1.5 * IQR
    upper_fence = Q3 + 1.5 * IQR
    # Filtrar los datos para eliminar los outliers
    return data[(data >= lower_fence) & (data <= upper_fence)]

# Colores elegantes
box_color = '#E3E3E3'  # Gris claro
whisker_color = '#6D6D6D'  # Gris oscuro
median_color = '#0072B2'  # Azul oscuro
trendline_color = '#D55E00'  # Naranja quemado

# Recorrer cada tratamiento y graficarlo
for i, tratamiento in enumerate(tratamientos):
    # Filtrar los datos para el tratamiento actual
    datos_tratamiento = df[df['Tratamientos'] == tratamiento]
    
    # Obtener los valores de ETc para los 14 vuelos
    valores_etc = datos_tratamiento.iloc[:, 1:]
    
    # Crear un dataframe para los datos limpios
    valores_etc_clean = pd.DataFrame()
    
    for col in valores_etc.columns:
        # Eliminar outliers en cada columna y añadir al dataframe limpio
        valores_etc_clean[col] = remove_outliers(valores_etc[col])
    
    # Calcular medias para la línea de tendencia
    medias = valores_etc_clean.mean()
    
    # Graficar en la posición adecuada del subplot
    ax = axs[i]
    
    # Graficar los boxplots sin los outliers
    ax.boxplot([valores_etc[col] for col in valores_etc.columns], labels=valores_etc.columns, 
               patch_artist=True, showfliers=False,  # Aquí desactivamos la visualización de outliers
               boxprops=dict(facecolor=box_color, color='black'),
               whiskerprops=dict(color=whisker_color), capprops=dict(color=whisker_color),
               medianprops=dict(color=median_color))
    
    # Graficar línea de tendencia (delgada) utilizando datos limpios
    ax.plot(valores_etc.columns, medias, marker='o', color=trendline_color, linestyle='-', 
            linewidth=1.0, markersize=7, label='Media de ETc')

    
    # Ajustar títulos y etiquetas
    if i == 0:
        ax.set_ylabel('G (W m$^{-2}$)')  # Etiqueta del eje Y solo en el primer gráfico
    else:
        ax.set_ylabel('')  # Sin etiqueta en los demás gráficos
        ax.tick_params(axis='y', labelleft=False)  # Ocultar ticks y etiquetas del eje Y en los demás gráficos
    
    # Establecer límites del eje Y de 3 a 8
    #ax.set_ylim(2.8, 8.2)
    
    #ax.set_xlabel('Number of UAV flights')
    
    # Ajustar los ticks del eje X para mostrar solo 1, 3, 5,... hasta 13
    ticks = ax.get_xticks()  # Obtén los ticks actuales
    ticks_labels = [str(int(tick)) if int(tick) % 2 == 1 else '' for tick in ticks]  # Etiquetar solo los impares
    ax.set_xticks(ticks)  # Mantener todos los ticks
    ax.set_xticklabels(ticks_labels)  # Cambiar etiquetas según la condición
    
    # Eliminar los números del eje x
    ax.set_xticklabels([])
    
    # Agregar la leyenda
    #ax.legend()
    
    # Añadir título a cada subplot
    # ax.set_title(f'Tratamiento {tratamiento}', fontsize=14)

# Ajustar el layout para que no se sobrepongan las gráficas
plt.tight_layout()

# Guardar el gráfico en formato PNG con 600 dpi
plt.savefig('grafico_G.png', dpi=600, format='png', bbox_inches='tight')

# Mostrar las gráficas
plt.show()


