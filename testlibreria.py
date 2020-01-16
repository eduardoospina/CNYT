import unittest
from libreria import *
class TestStringMethods(unittest.TestCase):

    def test_suma(self):
        v = (2,3)
        d = (1,2)
        self.assertEqual(sumacomplejos(v,d), (3,5))
    def test_resta(self):
        v = (5,3)
        d = (3,2)
        self.assertEqual(restacomplejos(v,d), (2,1))
    def test_multicomplejos(self):
        v = (6,3)
        d = (2,1)
        self.assertEqual(multicomplejos(v,d), (9,15))
    def test_multicomplejos(self):
        v = (-2,1)
        d = (1,2)
        self.assertEqual(multicomplejos(v,d), (-4, 0))
    def test_divcomplejos(self):
        v = (3,5)
        d = (3,2)
        self.assertEqual(divcomplejos(v,d), (0.7241379310344828, 0.3103448275862069))
    def test_divcomplejos(self):
        v = (-2,1)
        d = (1,2)
        self.assertEqual(divcomplejos(v,d), (0.0, 1.0))
    def test_modulo(self):
        v = (4,3)
        self.assertEqual(modulo(v), 12.5)
    def test_conjugado(self):
        v = (2,3)
        self.assertEqual(conjugado(v), (2,-3))
    def test_fase(self):
        d = (1,1)
        self.assertEqual(fase(d), 1)
    def test_conversioncap(self):
        d = (2,4)
        self.assertEqual(conversioncap(d), (10.0, 1.1071487177940904))
    

    
if __name__ == '__main__':
    unittest.main()
