# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 14:40:13 2024

@author: joluh
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import string

# Configurar la fuente globalmente
plt.rcParams['font.family'] = 'Palatino Linotype'
plt.rcParams['font.size'] = 24

# Archivos de Excel y variables en orden inverso
archivos_excel = ['ETc.xlsx', 'Rn.xlsx', 'LE.xlsx', 'G.xlsx', 'H.xlsx'][::-1]
variables = ['ET$_{c}$ (mm d$^{-1}$)', 'Rn (W m$^{-2}$)', 'LE (W m$^{-2}$)', 'G (W m$^{-2}$)', 'H (W m$^{-2}$)'][::-1]

# Crear un subplot con 20 gráficos (5 filas x 4 columnas)
fig, axs = plt.subplots(5, 4, figsize=(30, 25))

# Función para eliminar outliers
def remove_outliers(data):
    Q1 = np.percentile(data, 25)
    Q3 = np.percentile(data, 75)
    IQR = Q3 - Q1
    lower_fence = Q1 - 1.5 * IQR
    upper_fence = Q3 + 1.5 * IQR
    return data[(data >= lower_fence) & (data <= upper_fence)]

# Colores elegantes
box_color = '#E3E3E3'  # Gris claro
whisker_color = '#6D6D6D'  # Gris oscuro
median_color = '#0072B2'  # Azul oscuro
trendline_color = '#D55E00'  # Naranja quemado

# Nombres de las columnas de tratamientos con subíndices
column_titles = ['CF', 'AWD$_5$', 'AWD$_{10}$', 'AWD$_{20}$']

# Enumerar las subplots con letras
letters = string.ascii_lowercase

# Índice de subfigura
idx_figura = 0

# Iterar sobre los archivos y variables, asignando cada archivo a una fila
for idx_archivo, ruta_excel in enumerate(archivos_excel):
    # Leer los datos desde un archivo Excel
    df = pd.read_excel(ruta_excel)

    # Obtener los tratamientos únicos
    tratamientos = df['Tratamientos'].unique()

    # Para cada tratamiento, crear un gráfico
    for i, tratamiento in enumerate(tratamientos):
        # Filtrar los datos para el tratamiento actual
        datos_tratamiento = df[df['Tratamientos'] == tratamiento]

        # Obtener los valores correspondientes para los vuelos
        valores_etc = datos_tratamiento.iloc[:, 1:]

        # Crear un dataframe para los datos limpios
        valores_etc_clean = pd.DataFrame()

        for col in valores_etc.columns:
            # Eliminar outliers en cada columna y añadir al dataframe limpio
            valores_etc_clean[col] = remove_outliers(valores_etc[col])

        # Calcular medias para la línea de tendencia
        medias = valores_etc_clean.mean()

        # Determinar las coordenadas del subplot en la cuadrícula
        row = idx_archivo
        col = i

        # Graficar en la posición adecuada del subplot
        ax = axs[row, col]

        # Graficar los boxplots sin los outliers
        ax.boxplot([valores_etc[col] for col in valores_etc.columns], labels=valores_etc.columns,
                   patch_artist=True, showfliers=False,
                   boxprops=dict(facecolor=box_color, color='black'),
                   whiskerprops=dict(color=whisker_color), capprops=dict(color=whisker_color),
                   medianprops=dict(color=median_color))

        # Graficar línea de tendencia utilizando datos limpios
        ax.plot(valores_etc.columns, medias, marker='o', color=trendline_color, linestyle='-', 
                linewidth=1.0, markersize=5, label=f'Media de {variables[idx_archivo]}')

        # Ajustar títulos y etiquetas
        if col == 0:
            ax.set_ylabel(variables[idx_archivo])  # Etiqueta del eje Y en la primera columna
        else:
            ax.set_ylabel('')  # Sin etiqueta en las demás columnas
            ax.tick_params(axis='y', labelleft=False)

        # Ajustar los ticks del eje X para mostrar solo 1, 3, 5,... hasta 13 solo en la última fila
        if row == 4:  # Última fila
            ticks = ax.get_xticks()  # Obtén los ticks actuales
            ticks_labels = [str(int(tick)) if int(tick) % 2 == 1 else '' for tick in ticks]  # Etiquetar solo los impares
            ax.set_xticks(ticks)  # Mantener todos los ticks
            ax.set_xticklabels(ticks_labels)  # Cambiar etiquetas según la condición
            ax.set_xlabel('Number of UAV Flights')  # Etiqueta del eje X solo en la última fila
        else:
            ax.set_xticklabels([])  # Eliminar etiquetas del eje X en las demás filas
            ax.set_xlabel('')  # Sin etiqueta del eje X en las demás filas

        # Añadir una letra a cada subplot en la parte superior derecha
        ax.text(0.96, 0.93, f'{letters[idx_figura]})', transform=ax.transAxes, 
                size=24, weight='bold', ha='center', va='center')

        # Avanzar al siguiente subplot
        idx_figura += 1

# Añadir títulos de columna para los tratamientos
for ax, col_title in zip(axs[0], column_titles):
    ax.set_title(col_title, size=24, pad=20)

# Ajustar el layout para que no se sobrepongan las gráficas
plt.tight_layout()

# Guardar el gráfico en formato PNG con 600 dpi
plt.savefig('grafico_completo.png', dpi=600, format='png', bbox_inches='tight')

# Mostrar las gráficas
plt.show()
