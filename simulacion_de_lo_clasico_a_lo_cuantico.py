from sys import stdin

def prettyprintingcanicas(vector):
    for i in range(len(vector)):
        for j in range(1):
            print(vector[i])
def prettyprintingscuantico(vector):
    for i in range(len(vector)):
        for j in range(1):
            print(vector[i][j])
def matrizvvectorb(m1,v1):
    conta = 1
    suma = 0
    matriz_Vector = [0 for i in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(m1)):
            for k in range(len(m1[0])):
                suma = suma + m1[i][k] * v1[k]
            if suma == 0:
                matriz_Vector[i] = False
            else:
                matriz_Vector[i] = True
            suma = 0
            break                
    return matriz_Vector
def matrizvvectorr(m1,v1):
    conta = 1
    matriz = [[[0,0] for j in range(1)] for i in range(len(m1))]
    for i in range(len(m1)):
        for j in range(len(v1[0])):
            for k in range(len(m1[0])):
                matriz[i][j][0] = matriz[i][j][0] + (m1[i][k][0] * v1[k][j] - m1[i][k][1]*v1[k][j+conta])
                matriz[i][j][1] = matriz[i][j][1] + (m1[i][k][1] * v1[k][j] + m1[i][k][0]*v1[k][j+conta])
            break
    return(matriz)
def canicas(m1,v1,n):
    if len(m1) == 0 or len(v1) == 0:
        print("error.")
    elif len(m1[0]) != len(v1):
        print("error.")
    else:
        conta = 1
        while conta <= n:
            multi = matrizvvectorb(m1,v1)
            conta += 1
        prettyprintingcanicas(multi)
        return(multi)
def cuantico(m,e,n):
    if len(m) == 0 or len(e) == 0:
        print("error.")
    elif len(m[0]) != len(e):
        print("error.")
    else:
        conta = 1
        while conta <= n:
            multi = matrizvvectorr(m,e)
            conta += 1
        prettyprintingscuantico(multi)
    return(multi)
def clasico(m,e,n):
    if len(m) == 0 or len(e) == 0:
        print("error.")
    elif len(m[0]) != len(e):
        print("error.")
    else:
        conta = 1
        while conta <= n:
            multi = matrizvvectorr(m,e)
            conta += 1
        prettyprintingscuantico(multi)
    print(multi)
    return(multi)
import matplotlib.pyplot as plot
import numpy as np
def Probabilidadestado(v):
    unidades = len(v)
    x = np.array([ x for x in range(unidades)])
    y = np.array([round(v[x][0]*100,2) for x in range(unidades)])
    plot.bar( x,y , color ='b', align='center')
    plot.title('estado')
    plot.show()

