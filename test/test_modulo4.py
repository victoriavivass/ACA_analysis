import unittest
import os
import sys
import pandas as pd

# Asegurar que Python puede encontrar modulo4.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modulo4 import suavizar_datos, graficar_suavizado

class TestModulo4(unittest.TestCase):
    """Tests para la suavización y graficado de datos"""

    def setUp(self):
        """Crear un DataFrame ya preparado y suavizado para ambos tests"""
        datos = {
            'dia': ['13/01/2000', '08/02/2000', '12/02/2000'],
            'nivell_perc': [75.1, 80.2, 66.4]
        }
        df = pd.DataFrame(datos)
        self.df_suavizado = suavizar_datos(df)

    def test_suavizar_datos(self):
        """Verifica que se añade la columna 'nivell_perc_suavizado'"""
        self.assertIn('nivell_perc_suavizado', self.df_suavizado.columns)
        self.assertEqual(len(self.df_suavizado), 3)

    def test_graficar_suavizado(self):
        """Verifica que se genera la imagen correctamente a partir del DataFrame suavizado"""
        nombre_archivo = "Maria_Victoria_Vivas_Gutierrez"
        graficar_suavizado(self.df_suavizado, nombre_archivo)
        ruta = f"img/labaells_smoothed_{nombre_archivo}.png"
        self.assertTrue(os.path.exists(ruta))

if __name__ == '__main__':
    unittest.main()