import unittest
from sim2 import *
class TestStringMethods(unittest.TestCase):
    def test_probabilidad(self):
        v1 = [(1,2),(2,3),(4,5)]
        p = 1
        self.assertEqual(probabilidad(v1, p),((2, 3), '/', (-3, -4)))
    def test_transitar(self):
        v2 = [1,2,3,4,5,6]
        v1 = [8,6,4,3,2,4]
        self.assertEqual(transitar(v1, v2),(78, 67))
    def test_probabilidad2(self):
        v1 = [(1,2),(2,3),(4,5),(6,3),(4,1)]
        p = 4
        self.assertEqual(probabilidad(v1, p),((4, 1), '/', (-8, -16)))
    def test_transitar2(self):
        v2 = [1,2,3,4,5,6,7,4,3]
        v1 = [8,6,4,3,2,4,8,1,5]
        self.assertEqual(transitar(v1, v2),(138, 78))
    
    
if __name__ == '__main__':
    unittest.main()
