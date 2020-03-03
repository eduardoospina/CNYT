import unittest
from simulacion_de_lo_clasico_a_lo_cuantico import *


class simulaciondeloclasicoalocuantico(unittest.TestCase):
   
    def test_1( self  ):
        v1 = [True,False,False,False,False,True]
        v2 = [0,0,0,0,0,0]
        m1 = [[False,False,False,True,False,True],[True,True,False,True,False,True],[True,True,False,True,False,True],[True,True,False,True,False,True],[False,False,False,True,False,True],[False,False,False,True,False,True]]
        m2 = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
        
        self.assertEqual(canicasbooleanos( m1, m2, v1, v2, 1 ),
                         [True, True, True, True, True, True],[False, False, False, False, False, False] )

        self.assertEqual(canicasbooleanos( m1, m2, v1, v2, 3 ),
                         [True, True, True, True, True, True],[False, False, False, False, False, False] )

        self.assertEqual(canicasbooleanos( m1, m2, v1, v2, 5 ),
                         [True, True, True, True, True, True],[False, False, False, False, False, False] )

    def test_2( self ):
        
        self.assertEqual( múltiplesrendijasclásicoprobabilístico( 2, 4, 1/2 ),  1/2 )
       
    def test_3( self ):
        
        self.assertEqual( multiplesrendijascuantico(2,4,"((1+i)/2)") , "((1+i)/2)")

    def testGrafico( self ):
         grafico( [ [0,0] ,[0,0]  ,[0,0] ,
                    [1/3,0],[1/6,0], [1/6,0],
                    [1/6,0],[1/3,0] ]  )
       
       
if __name__ == '__main__':
    unittest.main()
