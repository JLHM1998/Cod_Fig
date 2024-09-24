# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 17:03:37 2024

@author: joluh
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import string

# Configurar la fuente globalmente
plt.rcParams['font.family'] = 'Palatino Linotype'
plt.rcParams['font.size'] = 24

# Archivos de Excel y variables en orden
archivos_excel = ['T.xlsx', 'HR.xlsx', 'WS.xlsx', 'RS.xlsx']
variables = ['T (ºC)', 'HR (%)', 'WS (W m$^{-1}$)', 'RS (W m$^{-2}$)']

# Crear un subplot con 4 gráficos (2 filas x 2 columnas)
fig, axs = plt.subplots(2, 2, figsize=(20, 15))

# Función para eliminar outliers
def remove_outliers(data):
    Q1 = np.percentile(data.dropna(), 25)  # Ignorar NaN en el cálculo
    Q3 = np.percentile(data.dropna(), 75)
    IQR = Q3 - Q1
    lower_fence = Q1 - 1.5 * IQR
    upper_fence = Q3 + 1.5 * IQR
    return data[(data >= lower_fence) & (data <= upper_fence)]

# Colores elegantes
box_color = '#E3E3E3'  # Gris claro
whisker_color = '#6D6D6D'  # Gris oscuro
median_color = '#0072B2'  # Azul oscuro
trendline_color = '#D55E00'  # Naranja quemado

# Enumerar las subplots con letras
letters = string.ascii_lowercase

# Índice de subfigura
idx_figura = 0

# Iterar sobre los archivos Excel y variables
for idx_variable, (archivo, variable) in enumerate(zip(archivos_excel, variables)):
    # Leer los datos del archivo Excel
    df = pd.read_excel(archivo, header=None)  # Usar header=None si no hay encabezado en el archivo

    # Verificar si hay suficientes datos
    if df.empty:
        print(f"El archivo {archivo} está vacío o no se pudo cargar correctamente.")
        continue

    # Transponer si es necesario para asegurar que las columnas correspondan a los vuelos
    if df.shape[0] < df.shape[1]:  # Si hay más columnas que filas, transponer
        df = df.T

    # Eliminar filas completamente vacías o con todos los valores NaN
    df.dropna(how='all', inplace=True)

    # Eliminar outliers
    datos_clean = df.apply(remove_outliers, axis=0)

    # Calcular medias para la línea de tendencia por número de vuelos (columnas en tu archivo)
    medias = datos_clean.mean(axis=0)

    # Determinar las coordenadas del subplot en la cuadrícula
    row = idx_variable // 2
    col = idx_variable % 2

    # Graficar en la posición adecuada del subplot
    ax = axs[row, col]

    # Asegurar que las etiquetas coincidan con los datos
    labels = range(1, len(df.columns) + 1)  # Etiquetas basadas en el número de columnas

    # Graficar los boxplots sin los outliers
    ax.boxplot([datos_clean[col].dropna() for col in datos_clean.columns],
               labels=labels,  # Asegurarse de que las etiquetas correspondan a las columnas
               patch_artist=True, showfliers=False,
               boxprops=dict(facecolor=box_color, color='black'),
               whiskerprops=dict(color=whisker_color), capprops=dict(color=whisker_color),
               medianprops=dict(color=median_color))

    # Graficar línea de tendencia utilizando datos limpios
    ax.plot(labels, medias, marker='o', color=trendline_color, linestyle='-', 
            linewidth=1.0, markersize=5, label=f'Media de {variable}')

    # Ajustar títulos y etiquetas
    ax.set_ylabel(variable)  # Etiqueta del eje Y en todas las columnas

    if row == 1:  # Última fila
        ticks = ax.get_xticks()  # Obtén los ticks actuales
        ticks_labels = [str(int(tick)) if int(tick) % 2 == 1 else '' for tick in ticks]  # Etiquetar solo los impares
        ax.set_xticks(ticks)  # Mantener todos los ticks
        ax.set_xticklabels(ticks_labels)  # Cambiar etiquetas según la condición
        ax.set_xlabel('Number of UAV flights')  # Etiqueta del eje X solo en la última fila
    else:
        ax.set_xticklabels([])  # Eliminar etiquetas del eje X en las demás filas
        ax.set_xlabel('')  # Sin etiqueta del eje X en la primera fila

    # Añadir una letra a cada subplot en la parte superior derecha
    ax.text(0.96, 0.93, f'{letters[idx_figura]})', transform=ax.transAxes, 
            size=24, weight='bold', ha='center', va='center')

    # Avanzar al siguiente subplot
    idx_figura += 1

# Ajustar el layout para que no se sobrepongan las gráficas
plt.tight_layout()

# Guardar el gráfico en formato PNG con 600 dpi
plt.savefig('grafico_meteo.png', dpi=600, format='png', bbox_inches='tight')

# Mostrar las gráficas
plt.show()
