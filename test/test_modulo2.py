import unittest
import os
import sys
import pandas as pd

# Asegurar que Python puede encontrar modulo2.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modulo2 import limpiar_datos

class TestModulo2(unittest.TestCase):
    """Tests para la limpieza de datos"""

    def setUp(self):
        """Crear un DataFrame de prueba antes de cada test"""
        datos = {
            'Dia': ['08/02/2000', '13/01/2000', '12/02/2000'],
            'Estació': ['Embassament de La Baells', 'Embassament de Foix', 'Embassament de Sau'],
            'Nivell absolut (msnm)': [100.5, 200.3, 150.8],
            'Percentatge volum embassat (%)': [80.2, 75.1, 66.4],
            'Volum embassat (hm3)': [31.29, 89.67, 6.60]
        }
        self.df_test = pd.DataFrame(datos)

    def test_filtrado_pantano_baells(self):
        """Verificar que la función limpia y filtra correctamente La Baells"""
        df_resultado = limpiar_datos(self.df_test)
        estaciones_unicas = df_resultado['estacio'].unique()
        self.assertTrue(all("Baells" in est for est in estaciones_unicas))

    def test_columnas_renombradas(self):
        """Verificar que las columnas han sido renombradas correctamente"""
        df_resultado = limpiar_datos(self.df_test)
        columnas_esperadas = {'dia', 'estacio', 'nivell_msnm', 'nivell_perc', 'volum'}
        self.assertTrue(columnas_esperadas.issubset(df_resultado.columns))

if __name__ == '__main__':
    unittest.main()