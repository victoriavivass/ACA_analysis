import unittest
import os
import sys
import pandas as pd
import matplotlib.pyplot as plt

# Asegurar que Python puede encontrar modulo3.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modulo3 import transformar_fechas, agregar_dia_decimal, graficar_volumen

class TestModulo3(unittest.TestCase):
    """Tests para la transformación de fechas y generación de gráficos"""

    def setUp(self):
        """Crear un DataFrame de prueba antes de cada test"""
        datos = {
            'dia': ['08/02/2000', '13/01/2000', '12/02/2000'],
            'nivell_perc': [80.2, 75.1, 66.4]
        }
        self.df_test = pd.DataFrame(datos)

    def test_transformar_fechas(self):
        """Verificar que la función transforma correctamente la columna 'dia'"""
        df_resultado = transformar_fechas(self.df_test)
        self.assertEqual(df_resultado['dia'].dtype, 'datetime64[ns]')
        self.assertLessEqual(df_resultado['dia'].min(), df_resultado['dia'].max())

    def test_agregar_dia_decimal(self):
        """Verificar que se agrega correctamente la columna 'dia_decimal'"""
        df_resultado = agregar_dia_decimal(self.df_test)
        self.assertIn('dia_decimal', df_resultado.columns)
        self.assertTrue(df_resultado['dia_decimal'].dtype, 'float64')

    def test_graficar_volumen(self):
        """Verificar que la función de graficado crea un archivo PNG"""
        nombre_archivo = "María Victoria Vivas Gutierrez"
        graficar_volumen(self.df_test, nombre_archivo)
        ruta_imagen = f"img/labaells_{nombre_archivo}.png"
        self.assertTrue(os.path.exists(ruta_imagen))

if __name__ == '__main__':
    unittest.main()