import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
from scipy.signal import savgol_filter


def suavizar_datos(df):
    df = df.copy()  # Evita modificaciones inesperadas en el DataFrame original

    # Ajustar `window_length` para que nunca supere el tamaño del DataFrame
    window_length = min(1500, len(df))
    if window_length % 2 == 0:  # `window_length` debe ser impar
        window_length -= 1

    # Ajustar polyorder para que siempre sea menor que window_length
    polyorder = min(3, window_length - 1)

    if window_length > 1 and polyorder > 0:  # Evita errores con tamaños de ventana demasiado pequeños
        df['nivell_perc_suavizado'] = savgol_filter(df['nivell_perc'], window_length=window_length, polyorder=polyorder)
    else:
        df['nivell_perc_suavizado'] = df['nivell_perc']  # Mantener los datos sin suavizar si no es posible

    return df

def graficar_suavizado(df, nombre_alumno):
    plt.figure(figsize=(10, 5))

    # Graficar la señal original
    plt.plot(df['dia'], df['nivell_perc'], linestyle='-', color='b', label='Señal Original')

    # Graficar la señal suavizada con un trazo más grueso
    plt.plot(df['dia'], df['nivell_perc_suavizado'], linestyle='-', linewidth=4.5, color='orange', label='Señal Suavizada')

    plt.xlabel("Fecha")
    plt.ylabel("Porcentaje Embalsado (%)")
    plt.title("María Victoria Vivas Gutiérrez", fontsize=10, color="gray")
    plt.suptitle("Evolución Suavizada del Volumen de La Baells", fontsize=14)
    plt.legend()

    # Crear carpeta "img" si no existe
    os.makedirs("img", exist_ok=True)

    # Guardar la imagen
    ruta_imagen = f"img/labaells_smoothed_{nombre_alumno}.png"
    plt.savefig(ruta_imagen)
    print(f"Imagen guardada en {ruta_imagen}")

    plt.show()