import unittest
from simulacion_de_lo_clasico_a_lo_cuantico import *


class simulaciondeloclasicoalocuantico(unittest.TestCase):
   
    def test_1( self  ):
        v1 = [True,False,False,False,False,True]
        v2 = [0,0,0,0,0,0]
        m1 = [[False,False,False,True,False,True],[True,True,False,True,False,True],[True,True,False,True,False,True],[True,True,False,True,False,True],[False,False,False,True,False,True],[False,False,False,True,False,True]]
        m2 = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
        
        self.assertEqual(experimentBooleanMatrix( m1, m2, v1, v2, 1 ),
                         [True, True, True, True, True, True],[False, False, False, False, False, False] )

        self.assertEqual(experimentBooleanMatrix( m1, m2, v1, v2, 3 ),
                         [True, True, True, True, True, True],[False, False, False, False, False, False] )

        self.assertEqual(experimentBooleanMatrix( m1, m2, v1, v2, 5 ),
                         [True, True, True, True, True, True],[False, False, False, False, False, False] )

    def testMultipleSlitExperiment( self ):
        
        self.assertEqual( probabilisticSystem(  matrix[:], vectIni[:], 2 ),  [[0.0, 0.0], [0.0, 0.0], [0.0, 0.0], [0.16666666666666666, 0.0],
                                                    [0.16666666666666666, 0.0], [0.3333333333333333, 0.0],
                                                    [0.16666666666666666, 0.0], [0.16666666666666666, 0.0]] )
       
    def testMultipleSlitQuantumExperiment( self ):
        
        self.assertEqual( multipleSlitQuantumExperiment(  matrix[:], vectIni[:], 1 ), [[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                                                                             [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                                                                             [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0],
                                                                             [0.1666666666666667, 0.3333333333333334, 0.0, 1.0, 0.0, 0.0, 0.0, 0.0],
                                                                             [0.1666666666666667, 0.3333333333333334, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0],
                                                                             [0.0, 0.3333333333333334, 0.3333333333333334, 0.0, 0.0, 1.0, 0.0, 0.0],
                                                                             [0.1666666666666667, 0.0, 0.3333333333333334, 0.0, 0.0, 0.0, 1.0, 0.0],
                                                                             [0.1666666666666667, 0.0, 0.3333333333333334, 0.0, 0.0, 0.0, 0.0, 1.0]])

    def testGraphProbabilitiesVector( self ):
         graphProbabilitiesVector( [ [0,0] ,[0,0]  ,[0,0] ,
                                     [1/3,0],[1/6,0], [1/6,0],
                                     [1/6,0],[1/3,0] ]  )
       
       
if __name__ == '__main__':
    unittest.main()
