import pandas as pd
import requests
from io import StringIO

def cargar_datos():
    url = "https://analisi.transparenciacatalunya.cat/api/views/gn9e-3qhr/rows.csv?accessType=DOWNLOAD"

    # Descargar los datos con requests
    response = requests.get(url, verify=True)
    if response.status_code == 200:
        data = StringIO(response.text)
        df = pd.read_csv(data)

        print("Primeras 5 filas del dataset:")
        print(df.head())

        # Mostrar la informacin completa del dataset
        print("\nInformacin del DataFrame:")
        df.info()

        return df
    else:
        print("Error al obtener el dataset, cdigo:", response.status_code)
        return None

    return df  # Retornamos el DataFrame para que otros mdulos lo usen
