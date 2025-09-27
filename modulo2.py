import pandas as pd
from modulo1 import cargar_datos
import re

def limpiar_datos(df):
    # 1️. Renombrar columnas con un diccionario
    columnas_nuevas = {
        'Dia': 'dia',
        'Estació': 'estacio',
        'Nivell absolut (msnm)': 'nivell_msnm',
        'Percentatge volum embassat (%)': 'nivell_perc',
        'Volum embassat (hm3)': 'volum'
    }
    df.rename(columns=columnas_nuevas, inplace=True)

    # 2️. Mostrar valores únicos de los pantanos antes de la limpieza
    print("\nValores únicos de los pantanos antes de la limpieza:")
    print(df['estacio'].unique())

    # 3️. Renombrar nombres de pantanos con expresiones regulares
    df['estacio'] = df['estacio'].apply(lambda x: re.sub(r'Embassament de |\s*\(.*\)', '', x))

    # 4️. Mostrar valores únicos de los pantanos después de la limpieza
    print("\nValores únicos de los pantanos después de la limpieza:")
    print(df['estacio'].unique())

    # 5️. Filtrar solo datos de La Baells
    df_baells = df[df['estacio'].str.contains("Baells", case=False, na=False)]

    print("\nDatos filtrados de La Baells:")
    print(df_baells.head())

    return df_baells