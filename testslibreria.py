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
    def test_multiplicarcomplejos(self):
        v = (6,3)
        d = (2,1)
        self.assertEqual(multiplicarcomplejos(v,d), (9,15))
    def test_multiplicarcomplejos(self):
        v = (-2,1)
        d = (1,2)
        self.assertEqual(multiplicarcomplejos(v,d), (-4, 0))
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
    def test_distanciavectores(self):
        v1 = [6,0,5,4]
        v2 = [9,3,6,3]
        v3 = [3,2,4,3]
        v4 = [5,6,7,5]
        self.assertEqual(distanciavectores(v1,v2,v3,v4), (-70, 151))
        
    def test_esunitaria(self):
        m1 = [[2,3,4],[5,6,7],[1,2,3]]
        m2 = [[5,9,8],[1,3,7],[4,3,2]]
        self.assertEqual(esunitaria(m1,m2,3), (0))
        
    def test_eshermitiana(self):
        m1 = [[2,3,4],[5,6,7],[1,2,3]]
        m2 = [[5,9,8],[1,3,7],[4,3,2]]
        self.assertEqual(eshermitiana(m1,m2,3), (0))
        
    def test_accionmatrizvector (self):
        v1 = [6,0,5,4]
        v2 = [9,3,6,3]
        m1 = [[2,3,4],[5,6,7],[1,2,3]]
        m2 = [[5,9,8],[1,3,7],[4,3,2]]
        self.assertEqual(accionmatrizvector(v1,v2,m1,m2,3,3), ([[48, 81, 84], [15, 18, 21], [26, 27, 28]]))
        
    def test_productointernov(self):
        v1 = [6,0,5,4]
        v2 = [9,3,6,3]
        v3 = [3,2,4,3]
        v4 = [5,6,7,5]
        self.assertEqual(productointernov(v1,v2,v3,v4), (9, 6))
        
    def test_normav(self):
        v1 = [6,0,5,4]
        v2 = [9,3,6,3]
        self.assertEqual(normav(v1,v2,4), (-65, 168))
        
    def test_productomatrices(self):
        m5 = [[(6,0),(-1,0)],[(3,0),(-1,0)]]
        m10 = [[(1,0),(2,0)],[(3,0),(4,0)]]
        self.assertEqual(productomatrices(m5,m10), ([[[3, 0], [8, 0]], [[0, 0], [2, 0]]]))
        
    def test_productotensor(self):
        m6 = [[0.0,1.0],[1.0,0.0]]
        m7 = [[0.0,0.0],[0.0,0.0]]
        m8 = [[(1.0/(2.0**(1.0/2.0))),(1.0/(2.0**(1.0/2.0)))],[(1.0/(2.0**(1.0/2.0))),-(1.0/(2.0**(1.0/2.0)))]]
        m9 = [[0,0],[0,0],[0,0],[0,0]]
        self.assertEqual(productotensor(m6,m7,m8,m9), ([[[(0.0, 0.0), (0.0, 0.0), (0.7071067811865475, 0.0), (0.7071067811865475, 0.0)], [(0.0, 0.0), (-0.0, 0.0), (0.7071067811865475, 0.0), (-0.7071067811865475, 0.0)]], [[(0.7071067811865475, 0.0), (0.7071067811865475, 0.0), (0.0, 0.0), (0.0, 0.0)], [(0.7071067811865475, 0.0), (-0.7071067811865475, 0.0), (0.0, 0.0), (-0.0, 0.0)]]]))
        
    def test_sumavectoresc(self):
        v1 = [6,0,5,4]
        v2 = [9,3,6,3]
        self.assertEqual(sumavectoresc(v1,v2), ([15, 3, 11, 7]))
        
    def test_inversoaditivov(self):
        v1 = [6,0,5,4]
        self.assertEqual(inversoaditivov(v1), ([-6, 0, -5, -4]))
        
    def test_sumarmatriz(self):
        m1 = [[2,3,4],[5,6,7],[1,2,3]]
        m2 = [[5,9,8],[1,3,7],[4,3,2]]
        m3 = [[4,3,5],[5,9,7],[8,4,2]]
        m4 = [[5,3,1],[2,4,5],[2,3,4]]
        self.assertEqual(sumarmatriz(m1,m2,m3,m4,3,3), ([6, 6, 9, 10, 15, 14, 9, 6, 5],
[10, 12, 9, 3, 7, 12, 6, 6, 6]))
        
    def test_escalarxvectorc(self):
        v3 = [3,2,4,3]
        v4 = [5,6,7,5]
        self.assertEqual(escalarxvectorc(v3,v4,2), ([(1, 31), (8, 27)]))
        
    def test_inversoaditivom(self):
        m1 = [[2,3,4],[5,6,7],[1,2,3]]
        m2 = [[5,9,8],[1,3,7],[4,3,2]]
        self.assertEqual(inversoaditivom(m1,m2,3), ([[-2, -3, -4], [-5, -6, -7], [-1, -2, -3]],
[[-5, -9, -8], [-1, -3, -7], [-4, -3, -2]]))
        
    def test_escalarxmatrizc(self):
        m1 = [[2,3,4],[5,6,7],[1,2,3]]
        m2 = [[5,9,8],[1,3,7],[4,3,2]]
        self.assertEqual(escalarxmatrizc(3,2,m1,m2,3), ([(-4, 32), (7, 35), (5, 12)]))
        
    def test_transpuestamatrizvector(self):
        m1 = [[2,3,4],[5,6,7],[1,2,3]]
        m2 = [[5,9,8],[1,3,7],[4,3,2]]
        self.assertEqual(transpuestamatrizvector(m1,m2,3), ([[2, 5, 1], [3, 6, 2], [4, 7, 3]], [[5, 1, 4], [9, 3, 3], [8, 7, 2]]))
        
    def test_conjugada(self):
        m1 = [[2,3,4],[5,6,7],[1,2,3]]
        m2 = [[5,9,8],[1,3,7],[4,3,2]]
        self.assertEqual(conjugada(m1,m2,3), ([[-5, -9, -8], [-1, -3, -7], [-4, -3, -2]]))
        
    def test_adjuntamatriz(self):
        m1 = [[2,3,4],[5,6,7],[1,2,3]]
        m2 = [[5,9,8],[1,3,7],[4,3,2]]
        self.assertEqual(adjuntamatriz(m1,m2,3), ([[[2, 5, 1], [3, 6, 2], [4, 7, 3]]],
[[[-5, -1, -4], [-9, -3, -3], [-8, -7, -2]]]))
    

    
if __name__ == '__main__':
    unittest.main()
