import math
from sys import stdin
def sumacomplejos(a,b):
    a = (a[0]+b[0],a[1]+b[1])
    return a
   
def prettyprintingc(c):
    print(c[0],"+",c[1],"i")

def restacomplejos(a,b):
    return (a[0]-b[0],a[1]-b[1])

def multiplicarcomplejos(a,b):
    a = (a[0]*b[0]-a[1]*b[1]),(a[0]*b[0]+a[1]*b[1])
    print(a)
    return(a)

def conjugado (a):
    a = (a[0],(a[1]*-1))
    return a
def divcomplejos(a,b):
    arriba = ((a[0]*a[1]+b[0]*b[1])/((a[1]**2)+(b[1]**2)))
    abajo = (a[1]*b[0]-a[0]*b[1])/((a[1]**2)+(b[1]**2))
    fin = (arriba,abajo)
    return fin
def modulo(a):
    modul = (((a[0]**2)+(a[1]**2))**1/2)
    return modul
def conversioncap(a):
    q = math.atan(a[1]/a[0])
    p = modulo (a)
    fin = (p,q)
    return fin
"""def fase(a):
    return a[1]"""
def prettyprintingv(a):
    ini = a[0:len(a)//2]
    mita = a[len(a)//2:]
    for i in range (len(ini)):
        print(ini[i],"+",mita[i],"i")
           
def sumavectoresc(b,d):
    #b y d son vectores
    suma = []
    for i in range (len(b)):
        e = b[i] + d[i]
        suma.append(e)
    print (prettyprintingv(suma))
    return suma
def inversoaditivov(b):
    #b = vector
    inversa = []
    for i in range(len(b)):
        e = b[i]*-1
        inversa.append(e)
    print (prettyprintingv(b))
    print (prettyprintingv(inversa))
    return inversa
def escalarxvectorc(b,d,n):
    #b escalar d vector n es longitud mitad vector
    multi = []
    for i in range (n):
        e = ((b[0]*d[i])-(b[1]*d[i + n]),((b[0]*d[i+n])+(b[1]*d[i])))
        multi.append(e)
    print ((multi))
    return (multi)

def sumarmatriz(a,b,c,d,m,n):
    # a matriz real b matriz ima c matriz real d matriz ima
    sumar = []
    sumai = []
    for i in range ((m)):
        for j in range (n):
            e = a[i][j]+c[i][j]
            f = b[i][j]+d[i][j]
            sumar.append(e)
            sumai.append(f)
    print(sumar)
    print(sumai)
    return (sumar,sumai)
def inversoaditivom(a,b,m):
    # a matriz real b matriz ima, m y n coso de la matriz
    inversar = []
    inversai = []
    for i in range (m):
        menor1 = []
        menor2 = []
        for j in range (m):
            c = a[i][j]*-1
            d = b[i][j]*-1
            menor1.append(c)
            menor2.append(d)
        inversar.append(menor1)
        inversai.append(menor2)
    print (inversar)
    print (inversai)
    return (inversar,inversai)
def escalarxmatrizc(a,b,c,d,m):
    #a numero real b numero imaginario, c matriz real, d matriz imaginaria, m cosas de las matriz
    multi = []
    for i in range (m):
        menor = []
        for j in range (m):
          e = ((a*c[i][j])-(b*d[i][j]),((a*d[i][j])+(b*c[i][j])))
          menor.append(e)
        multi.append(e)
    print (multi)
    return (multi)

def transpuestamatrizvector(a,d,m):
    #a matriz real, d matriz ima, ma coso de la matriz
    transr = []
    transi = []
    for i in range(m):
        menor1 = []
        menor2 = []
        for j in range(m):
            if i == j:
                menor1.append(a[i][j])
                menor2.append(d[i][j])
            else:
                menor1.append(a[j][i])
                menor2.append(d[j][i])
        transr.append(menor1)
        transi.append(menor2)
    return(transr, transi)  

def conjugada (a,b,m):
  # a matriz real y b matriz ima, m cosa de matriz
  conjugada = []
  for i in range(m):
    menor = []
    for j in range(m):
        c = b[i][j]*-1
        menor.append(c)
    conjugada.append(menor)
  return conjugada
def adjuntamatriz(a,b,m):
    #a parte real matriz, b parte imaginaria, cosa de matriz
    conjugada1 = (conjugada(a,b,m))
    adjunta1 = []
    adjunta2 = []
    c,d = transpuestamatrizvector(a,conjugada1,m)
    adjunta1.append(c)
    adjunta2.append(d)
    print(adjunta1)
    print(adjunta2)
    return (adjunta1, adjunta2)

def productomatrices (a,b):
    #a y b matrices con tuplas
    producto = [[[0,0] for j in range (len(a))]for i in range (len(a))]
    for i in range(len(a)):
        for j in range(len(a)):
            for m in range (len(a[0])):
                producto[i][j][0] += (a[i][m][0] * b[m][j][0] - a[i][m][1] * b[m][j][1])
                producto[i][j][1] += (a[i][m][1] * b[m][j][0] - a[i][m][0] * b[m][j][1])
    print ( producto )
    return producto

def accionmatrizvector (a,b,c,d,m,n):
    #m numero columnas vector, n numero filas matriz, a y c vector real, b y d matriz y vector imag
    if ((m == n) == False):
        print ( "no se puede realizar")
    else :
        n3 = []
        n4 = []
        for i in range(m):
            n1 = []
            n2 = []
            for j in range(n):
                a1 = ((a[i]*c[i][j])-(b[i]*d[i][j]),((a[i]*d[i][j])+(b[i]*c[i][j])))
                n1.append(a1[0])
                n2.append(a1[1])
            n3.append(n1)
            n4.append(n2)
    print(n3)
    print(n4)
                
        
def productointernov (a,b,c,d):
    #a y c vector real , b y d vector ima
    n1 = []
    n2 = []
    for i in range (len(a)):
        e = ((a[i]*c[i])-(b[i]*d[i]),((a[i]*d[i])+(b[i]*c[i])))
        n1.append(c[0])
        n2.append(c[1])
    f = n1[0] + n1[1]
    g = n2[0] + n2[1]
    for i in range (2,((len(a)-1))):
        f = f + n1[i]
        g = g + n2[i]
    c = ((f,g))
    print (c)
    return c
def normav(a,b,m):
    #a vector real, b vector ima, m tamaño
    norma = []
    norma1 = []
    for i in range (len(a)):
        c = ((a[i]*a[i])-(b[i]*b[i]),((a[i]*b[i])+(b[i]*a[i])))
        norma.append(c[0])
        norma1.append(c[1])
    d = norma[0] + norma[1]
    e = norma1[0] + norma1[1]
    for i in range (2,m-1):
        d = d + norma[i]
        e = e + norma1[i]
    c = ((d,e))
    print ("(",d,"+",e,"i",")**(1/2))")
    return (c)

def distanciavectores(a,b,c,d):
    # a y c vectores reales, b y d vectores imag
    a1 = []
    a2 = []
    a5 = []
    a4 = []
    for i in range (len(a)):
        e = (a[i] - c[i])
        f = (b[i] - d[i])
        a1.append(e)
        a2.append(f)
    for i in range (len(a)):
        a5.append(((a[i]*c[i])-(b[i]*d[i]),((a[i]*d[i])+(b[i]*c[i]))))
    a4 = sumacomplejos(a5[0],a5[1])
    for i in range(2,len(a)):
        a4 = sumacomplejos(a4,a5[i])             
    print(a4)
    return a4

def esunitaria(a,b,m):
    # a parte real, b parte imaginaria, m tamaño
    c,d = adjuntamatriz(a,b,m)
    uni = []
    for i in range(len(a)):
        menor = []
        for j in range(len(a)):
            menori = []
            for m in range(len(c)):
                for n in range(len(c)):
                    x = ((a[i][m]*c[j][n])-(b[i][m]*d[j][n]),((a[i][m]*d[j][n])+(b[i][m]*c[j][n])))
                    menori.append(x)
            menor.append(menori)
        uni.append(menor)
    if m ==len(A):
        print (True)
    else:
        print(False)
    
            
    


def eshermitiana(a,b,m):
    c,d = adjuntamatriz(a,b,m)
    if a == c and b == d:
        print("es hermitania")
    else:
        print ("no es hermitania")
    print (a,b)
    print (c,d)
    
def productotensor(a,b,c,d):
    #a y c matriz real, b y d son matrices imaginarias
    if len(a) == 0 or len(c) == 0:
        print("datos incorrectos")
    else:
        tensor = []
        tensor1=[]
        for i in range(len(a)):
            menor = []
            for j in range(len(a)):
                menori = []
                for m in range(len(c)):
                    for n in range(len(c)):
                        x = ((a[i][m]*c[j][n])-(b[i][m]*d[j][n]),((a[i][m]*d[j][n])+(b[i][m]*c[j][n])))
                        menori.append(x)
                menor.append(menori)
            tensor.append(menor)
    print (tensor)
    return tensor

def simulador1():
    x = [[0,1],[1,0]]
    h = [[(1/(2**(1/2))),(1/(2**(1/2)))],[(1/(2**(1/2))),-(1/(2**(1/2)))]]
    x1 = [[0,0],[0,0],[0,0],[0,0]]
    h1 = [[0,0],[0,0],[0,0],[0,0]]
    m1 = productotensor(x,x1,h,h1)
    m2 = productotensor(h,h1,h,h1)
    print(m1)
    print(m1)
    v00 = [1,0,0,0]
    m1porm2 = productomatrices(m1,m2)
    gamma = productomatrices(m1porm2,v00)
    print (gamma)

#vectores primera mitad real segunda mitad
v1 = [6,0,5,4]
v2 = [9,3,6,3]
v3 = [3,2,4,3]
v4 = [5,6,7,5]
n = 4
n1 = (2,3)
n2 = (4,6)
m1 = [[2,3,4],[5,6,7],[1,2,3]]
m2 = [[5,9,8],[1,3,7],[4,3,2]]
m3 = [[4,3,5],[5,9,7],[8,4,2]]
m4 = [[5,3,1],[2,4,5],[2,3,4]]
m6 = [[0.0,1.0],[1.0,0.0]]
m7 = [[0.0,0.0],[0.0,0.0]]
m8 = [[(1.0/(2.0**(1.0/2.0))),(1.0/(2.0**(1.0/2.0)))],[(1.0/(2.0**(1.0/2.0))),-(1.0/(2.0**(1.0/2.0)))]]
m9 = [[0,0],[0,0],[0,0],[0,0]]
m5 = [[(6,0),(-1,0)],[(3,0),(-1,0)]]
m10 = [[(1,0),(2,0)],[(3,0),(4,0)]]
m11 = [[(0,0),(0,0)],[(0,0),(0,0)]]
m12 = [[(0,0),(0,0)],[(0,0),(0,0)]]


"""esunitaria(m1,m2,3)"""
eshermitiana(m1,m2,3)
distanciavectores(v1,v2,v3,v4)
#accionmatrizvector (v1,v2,m1,m2,3,3)
#productointernov (v1,v2,v3,v4)
#normav(v1,v2,4)
#multiplicarcomplejos(n1,n2)
#productomatrices (m5,m10)
#productotensor(m6,m7,m8,m9)
#sumavectoresc(v1,v2)
#inversoaditivov(v1)
#sumarmatriz(m1,m2,m3,m4,2,3)
#escalarxvectorc(v3,v4,2)
#inversoaditivom(m1,m2,3)
#escalarxmatrizc (3,2,m1,m2,3)
#transpuestamatrizvector(m1,m2,3)
#conjugada(m1,m2,3)
#adjuntamatriz(m1,m2,3)
