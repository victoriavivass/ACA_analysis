import pandas as pd

def calcula_periodos(df):
    """Detecta periodos de sequía cuando el nivel embalsado es menor al 60%."""
    df = df.copy()  # Evita modificar el DataFrame original

    # Verificar que la columna 'dia_decimal' existe
    if 'dia_decimal' not in df.columns:
        return []

    periodos = []
    inicio = None

    for _, row in df.iterrows():
        if row['nivell_perc_suavizado'] < 60:  # Condición de sequía
            if inicio is None:
                inicio = row['dia_decimal']
        else:
            if inicio is not None:
                periodos.append([inicio, row['dia_decimal']])
                inicio = None

    if inicio is not None:  # Si la sequía sigue hasta el final
        periodos.append([inicio, df['dia_decimal'].iloc[-1]])

    # Convertir los valores a números flotantes estándar de Python para una mejor visualización
    periodos = [[float(inicio), float(fin)] for inicio, fin in periodos]

    print(f"\n**Periodos de sequía detectados:** {periodos}")

    return periodos

# Código para ejecutar la función desde el módulo
if __name__ == "__main__":
    # Crear un DataFrame de prueba
    datos = {
        'dia_decimal': [2000.1, 2000.2, 2000.3, 2000.4, 2000.5, 2000.6],
        'nivell_perc_suavizado': [70, 55, 50, 40, 65, 75]  # Simulación de sequía en valores intermedios
    }
    df_test = pd.DataFrame(datos)

    # Ejecutar la función y ver los periodos detectados
    calcula_periodos(df_test)