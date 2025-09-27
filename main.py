from modulo1 import cargar_datos
from modulo2 import limpiar_datos
from modulo3 import transformar_fechas, agregar_dia_decimal, graficar_volumen
from modulo4 import suavizar_datos, graficar_suavizado
from modulo5 import calcula_periodos

nombre_alumno = "Maria_Victoria_Vivas_Gutierrez"

if __name__ == "__main__":
    print("Ejecutando PEC4...")

    # Cargar los datos
    df = cargar_datos()

    if df is not None:
        # Limpiar y filtrar los datos
        df_filtrado = limpiar_datos(df)

        # Transformar fechas y agregar columna decimal
        df_trans = transformar_fechas(df_filtrado)
        df_final = agregar_dia_decimal(df_trans)

        # Graficar evolución del volumen de agua
        graficar_volumen(df_final, "Victoria")

        # Aplicar suavizado de la curva
        df_suavizado = suavizar_datos(df_final)

        # Graficar volumen suavizado
        graficar_suavizado(df_suavizado, "Victoria")

        # Calcular periodos de sequía
        periodos_sequia = calcula_periodos(df_suavizado)
        print("\n Periodos de sequía detectados:")
        for periodo in periodos_sequia:
            print(f"Desde {periodo[0]:.2f} hasta {periodo[1]:.2f}")