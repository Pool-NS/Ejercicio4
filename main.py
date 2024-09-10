import unittest
from geometria import Geometria

class TestGeometria(unittest.TestCase):
    def setUp(self):
        self.geo = Geometria()

    def test_area_cuadrado(self):
        self.assertEqual(self.geo.area('cuadrado', 4), 16)
        self.assertEqual(self.geo.area('cuadrado', 5), 25)

    def test_area_rectangulo(self):
        self.assertEqual(self.geo.area('rectangulo', 4, 5), 20)
        self.assertEqual(self.geo.area('rectangulo', 7, 3), 21)

    def test_perimetro_cuadrado(self):
        self.assertEqual(self.geo.perimetro('cuadrado', 4), 16)
        self.assertEqual(self.geo.perimetro('cuadrado', 5), 20)

    def test_perimetro_rectangulo(self):
        self.assertEqual(self.geo.perimetro('rectangulo', 4, 5), 18)
        self.assertEqual(self.geo.perimetro('rectangulo', 7, 3), 20)

if __name__ == '__main__':
    unittest.main()
