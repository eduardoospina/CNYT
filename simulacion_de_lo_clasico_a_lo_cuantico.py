from libreria import *
import numpy as np
import matplotlib.pyplot as plt

v1 = [True,False,False,False,False,True]
v2 = [0,0,0,0,0,0]
m1 = [[False,False,False,True,False,True],[True,True,False,True,False,True],[True,True,False,True,False,True],[True,True,False,True,False,True],[False,False,False,True,False,True],[False,False,False,True,False,True]]
m2 = [[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]]
m = 6
n = 6
c1 = 10
def canicasbooleanos (m1, m2, v1, v2, c1):
    # m1 matriz real, m2 matriz ima, v1 vectpor real, v2 vector ima, c1 # clicks
    for i in range (c1):
        if i <= c1:
            v1, v2 = accionmatrizvector(v1,v2,m1,m2)
        for j in range (len(v1)):
            if v1[j] >= 1:
                v1[j] = True
            else:
                 v1[j] = False
            if v2[j] >= 1:
                v2[j] = True
            else:
                v2[j] = False
    print(v1)
    print(v2)
    return(v1, v2)
def múltiplesrendijasclásicoprobabilístico(m,n):
    return(1)
def multiplesrendijascuantiuco(m,n):
    return(2)
def grafico (v1):
    datos = len(v1)
    eje_x = np.array([eje_x for x in range(datos)])
    eje_y = np.array([round(v1[eje_x][0]*100, 2) for i in range(datos)])

    plot.bar(eje_x, eje_y, color = "f", align = "center")
    plot.title("vector probabilidad")
    plot.show()
    


#grafico(v1)  
#canicasbooleanos (m1, m2, v1, v2, c1)
