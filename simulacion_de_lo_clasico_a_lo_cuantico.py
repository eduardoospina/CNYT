from libreria import *
import numpy as np
import matplotlib.pyplot as plt

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
def múltiplesrendijasclásicoprobabilístico(rendijas, blancos, m):
    matriz = [[[0,0] for j in range (rendijas + blancos +1)]for i in range (rendijas + blancos +1)]
    contador = blancos//2
    for i in range (rendijas):
        matriz[i+1] = 1/rendijas
    for i in range ((rendijas + blancos +1)):
        for j in range ( rendijas + blancos +1):
            if j >= (rendijas + 1):
                matriz[j][j] = 1
            if contador > 0 and (rendijas + 1)<(rendijas + blancos +1):
                matriz[(rendijas + blancos )][1]= 1/(blancos//2)
            if j ==1:
                for i in range ((rendijas + blancos +1)):
                    for j in range ( rendijas + blancos +1):
                        if j >= (rendijas + 1):
                            matriz[j][j] = 1
                        if contador > 0 and (rendijas + 1)<(rendijas + blancos +1):
                            matriz[(rendijas + blancos )][1]= 1/(4)
    print (matriz)
    return(m)
def multiplesrendijascuantico(rendijas, blancos,m):
    matriz = [[[0,0] for j in range (rendijas + blancos +1)]for i in range (rendijas + blancos +1)]
    contador = blancos//2
    for i in range (rendijas):
        matriz[i+1] = 1/rendijas
    for i in range ((rendijas + blancos +1)):
        for j in range ( rendijas + blancos +1):
            if j >= (rendijas + 1):
                matriz[j][j] = 1
            if contador > 0 and (rendijas + 1)<(rendijas + blancos +1):
                matriz[(rendijas + blancos )][1]= 1/(blancos//2)
            if j ==1:
                for i in range ((rendijas + blancos +1)):
                    for j in range ( rendijas + blancos +1):
                        if j >= (rendijas + 1):
                            matriz[j][j] = 1
                        if contador > 0 and (rendijas + 1)<(rendijas + blancos +1):
                            matriz[(rendijas + blancos )][1]= 1/(4)
    print (matriz)
    return(m)
    return(2)
def grafico (v1):
    datos = len(v1)
    eje_x = np.array([eje_x for x in range(datos)])
    eje_y = np.array([round(v1[eje_x][0]*100, 2) for i in range(datos)])

    plot.bar(eje_x, eje_y, color = "f", align = "center")
    plot.title("vector probabilidad")
    plot.show()
    


#multiplesrendijascuantico(2,4,"((1+i)/2)")
#múltiplesrendijasclásicoprobabilístico(2,4,1/2)
#grafico(v1)  
#canicasbooleanos (m1, m2, v1, v2, c1)
