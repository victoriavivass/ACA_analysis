import unittest
import os
import sys
import pandas as pd

# Asegurar que Python puede encontrar modulo5.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modulo5 import calcula_periodos

class TestModulo5(unittest.TestCase):
    """Tests para la detección de periodos de sequía"""

    def setUp(self):
        """Crear un DataFrame de prueba antes de cada test"""
        datos = {
            'dia_decimal': [2000.1, 2000.2, 2000.3, 2000.4, 2000.5, 2000.6],
            'nivell_perc_suavizado': [70, 55, 50, 40, 65, 75]  # Simulación de sequía en valores intermedios
        }
        self.df_test = pd.DataFrame(datos)

    def test_calcula_periodos(self):
        """Verifica que la función detecta correctamente los periodos de sequía"""
        periodos = calcula_periodos(self.df_test)
        self.assertEqual(len(periodos), 1, "Debe detectar un único periodo de sequía")
        self.assertAlmostEqual(periodos[0][0], 2000.2, places=2)
        self.assertAlmostEqual(periodos[0][1], 2000.5, places=2)

    def test_sin_sequia(self):
        """Verifica que cuando no hay sequía, retorna una lista vacía"""
        df_sin_sequia = self.df_test.copy()
        df_sin_sequia['nivell_perc_suavizado'] = [80, 85, 90, 95, 100, 99]
        periodos = calcula_periodos(df_sin_sequia)
        self.assertEqual(periodos, [], "No debe detectar periodos de sequía en niveles altos")

    def test_falta_columna_dia_decimal(self):
        """Verifica que la función maneja correctamente la ausencia de 'dia_decimal'"""
        df_faltante = self.df_test.drop(columns=['dia_decimal'])
        periodos = calcula_periodos(df_faltante)
        self.assertEqual(periodos, [], "Debe retornar lista vacía si falta 'dia_decimal'")

if __name__ == '__main__':
    unittest.main()