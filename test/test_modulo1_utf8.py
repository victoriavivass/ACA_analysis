import unittest
import sys
import os
import unittest
import os
import sys

# Asegurar que Python puede encontrar modulo1.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from modulo1 import cargar_datos

class TestModulo1(unittest.TestCase):
    """Tests para la carga de datos"""

    def test_cargar_datos(self):
        """Verifica que cargar_datos() retorna un DataFrame con datos"""
        df = cargar_datos()
        self.assertIsNotNone(df, "El DataFrame no debería ser None")
        self.assertGreater(len(df), 0, "El DataFrame debería tener datos")
        self.assertIn('Dia', df.columns, "Falta la columna 'Dia' en el DataFrame")
        self.assertIn('Volum embassat (hm3)', df.columns, "Falta la columna 'Volum embassat (hm3)' en el DataFrame")

if __name__ == '__main__':
    unittest.main()