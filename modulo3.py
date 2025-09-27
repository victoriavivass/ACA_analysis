import pandas as pd
import matplotlib.pyplot as plt
import os
from datetime import datetime as dt
import time

# Función para convertir fechas a valores decimales
def toYearFraction(date):
    def sinceEpoch(date):  # Devuelve segundos desde epoch
        return time.mktime(date.timetuple())

    s = sinceEpoch

    year = date.year
    startOfThisYear = dt(year=year, month=1, day=1)
    startOfNextYear = dt(year=year + 1, month=1, day=1)

    yearElapsed = s(date) - s(startOfThisYear)
    yearDuration = s(startOfNextYear) - s(startOfThisYear)
    fraction = yearElapsed / yearDuration

    return date.year + fraction

# 1️. Convertir 'dia' a datetime y ordenar por fecha
def transformar_fechas(df):
    df = df.copy()  # Crear copia para evitar el warning de pandas
    df['dia'] = pd.to_datetime(df['dia'], format="%d/%m/%Y")
    df.sort_values(by='dia', inplace=True)

    print(f"\nFecha más antigua: {df['dia'].min()}")
    print(f"Fecha más reciente: {df['dia'].max()}")

    return df

# 2️. Crear columna 'dia_decimal' asegurando que 'dia' sea datetime
def agregar_dia_decimal(df):
    df = df.copy()  # Crear copia para evitar problemas con pandas

    # Convertir 'dia' a datetime si aún no lo está
    if df['dia'].dtype == 'object':
        df['dia'] = pd.to_datetime(df['dia'], format="%d/%m/%Y")

    df['dia_decimal'] = df['dia'].apply(toYearFraction)
    return df

# 3️. Graficar evolución del volumen de agua
def graficar_volumen(df, nombre_alumno):
    plt.figure(figsize=(10, 5))
    plt.plot(df['dia'], df['nivell_perc'], marker='o', linestyle='-', color='b', label='Nivel Embalsado (%)')

    plt.xlabel("Fecha")
    plt.ylabel("Porcentaje Embalsado (%)")
    plt.title(f"Evolución del volumen de La Baells - {nombre_alumno}")
    plt.legend()

    # Crear carpeta "img" si no existe
    os.makedirs("img", exist_ok=True)

    # Guardar la imagen con mi nombre (definido en main)
    ruta_imagen = f"img/labaells_{nombre_alumno}.png"
    plt.savefig(ruta_imagen)
    print(f"Imagen guardada en {ruta_imagen}")

    plt.show()
