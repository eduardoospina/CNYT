import unittest
from sim3 import *
class TestStringMethods(unittest.TestCase):
    def test_probabilidad(self):
        v1 = [(1,2),(2,3),(4,5)]
        p = 1
        self.assertEqual(probabilidad(v1, p),((2, 3), '/', (-3, -4)))
    def test_hermitiana(self):
        v2 = [0,1]
        v1 = [1,0]
        m1 = [2,3,4,5]
        m2 = [1,4,5,3]
        m = 2
        self.assertEqual(hermitiana(m1, m2,m,v1, v2),([1, 0]))
    def test_probabilidad2(self):
        v1 = [(1,2),(2,3),(4,5),(6,3),(4,1)]
        p = 4
        self.assertEqual(probabilidad(v1, p),((4, 1), '/', (-8, -16)))
    def test_hermitiana2(self):
        v2 = [1,0]
        v1 = [0,1]
        m1 = [2,9,4,7]
        m2 = [1,4,2,3]
        m = 2
        self.assertEqual(hermitiana(m1, m2,m,v1, v2),([0,1]))
    def test_probabilidad3(self):
        v1 = [(1,2),(2,3),(4,5)]
        p = 1
        self.assertEqual(probabilidad(v1, p),((2, 3), '/', (-3, -4)))
    def test_hermitiana3(self):
        v2 = [0,1]
        v1 = [1,0]
        m1 = [2,3,4,5]
        m2 = [1,4,5,3]
        m = 2
        self.assertEqual(hermitiana(m1, m2,m,v1, v2),([1, 0]))
    def test_probabilidad4(self):
        v1 = [(1,2),(2,3),(4,5),(6,3),(4,1)]
        p = 4
        self.assertEqual(probabilidad(v1, p),((4, 1), '/', (-8, -16)))
    def test_hermitiana4(self):
        v2 = [1,0]
        v1 = [0,1]
        m1 = [2,9,4,7]
        m2 = [1,4,2,3]
        m = 2
        self.assertEqual(hermitiana(m1, m2,m,v1, v2),([0,1]))
    
if __name__ == '__main__':
    unittest.main()
