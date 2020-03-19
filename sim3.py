from libreria import *

def probabilidad(vector, posicion):
    lista1 =[]
    lista2= []
    a_1 = vector[posicion]
    b_1 = modulo(a_1)
    for i in range(len(vector)//2):
        lista1.append (vector[i][0])
        lista2.append (vector[i][1])
    lista1 += lista2
    a_2 = normav(lista1)
    print ((a_1 ,"/",a_2 ,))
    return (a_1,"/",a_2)

def hermitiana(matriz1, matriz2, m, vector1, vector2):
    if matriz1 != matriz2:
        esperado1 = matriz1
        resp = vector1
        return resp
    else:
        print("no es hermitieana")
        return("no es hermitieana")
