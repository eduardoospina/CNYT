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

def transitar(vector1, vector2):
    if len(vector1) != len(vector2):
        print("Error")
    else:
        a_1 = productointernov(vector1, vector2)
    return a_1
probabilidad([(2,2),(1,2)], 1)
transitar([1,2,3,4,5,6], [9,8,7,4,3,5])
