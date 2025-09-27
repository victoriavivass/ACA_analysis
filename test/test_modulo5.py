import unittest
import os
import sys
import pandas as pd

# Asegurar que Python pueda encontrar modulo5.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modulo5 import calcula_periodos

class TestModulo5(unittest.TestCase):
    """Tests para la detección de periodos de sequía"""

    def setUp(self):
        self.df_sequia = pd.DataFrame({
            'dia_decimal': [2000.1, 2000.2, 2000.3, 2000.4, 2000.5],
            'nivell_perc_suavizado': [70, 55, 50, 65, 75]
        })

        self.df_sin_columna = pd.DataFrame({
            'otra_columna': [1, 2, 3],
            'nivell_perc_suavizado': [50, 45, 40]
        })

        self.df_sin_sequia = pd.DataFrame({
            'dia_decimal': [2001.1, 2001.2, 2001.3],
            'nivell_perc_suavizado': [80, 85, 90]
        })

        self.df_multiple = pd.DataFrame({
            'dia_decimal': [2002.0, 2002.1, 2002.2, 2002.3, 2002.4, 2002.5],
            'nivell_perc_suavizado': [55, 50, 65, 40, 30, 70]
        })

    def test_detecta_un_periodo(self):
        resultado = calcula_periodos(self.df_sequia)
        self.assertEqual(len(resultado), 1)
        self.assertAlmostEqual(resultado[0][0], 2000.2)
        self.assertAlmostEqual(resultado[0][1], 2000.4)

    def test_sin_columna_dia_decimal(self):
        resultado = calcula_periodos(self.df_sin_columna)
        self.assertEqual(resultado, [])

    def test_sin_sequia(self):
        resultado = calcula_periodos(self.df_sin_sequia)
        self.assertEqual(resultado, [])

    def test_varios_periodos(self):
        resultado = calcula_periodos(self.df_multiple)
        self.assertEqual(len(resultado), 2)
        self.assertAlmostEqual(resultado[0][0], 2002.0)
        self.assertAlmostEqual(resultado[0][1], 2002.2)
        self.assertAlmostEqual(resultado[1][0], 2002.3)
        self.assertAlmostEqual(resultado[1][1], 2002.5)

if __name__ == '__main__':
    unittest.main()