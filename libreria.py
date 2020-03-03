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
    q = math.atan2((a[1]/a[0]),1)
    p = modulo (a)
    fin = (p,q)
    return fin
def fase(a):
    b = (a[0]**2) + (a[1]**2)
    c = round(math.sqrt(b),2)
    d = a[1]/a[0]
    e = round(math.atan(d),2)
    f = (c, e)
    print (f[1])
    return f[1]

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
    print (suma)
    return suma
def inversoaditivov(b):
    #b = vector
    inversa = []
    for i in range(len(b)):
        e = b[i]*-1
        inversa.append(e)
    print (prettyprintingv(b))
    print (prettyprintingv(inversa))
    print (inversa)
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
    print(transr,transi)
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
  print (conjugada)
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

def accionmatrizvector (a,b,c,d):
    #m numero columnas vector, n numero filas matriz, a y c vector real, b y d matriz y vector imag
    if ((len(a) == len(c)) == False):
        print ( "no se puede realizar")
    else :
        n3 = []
        n6 = []
        n4 = 0
        n5 = 0
        for i in range(0,len(c)):
            n1 = []
            n2 = []
            for j in range(0,len(a)):
                a1 = ((a[j]*c[i][j])-(b[j]*d[i][j]),((a[j]*d[i][j])+(b[j]*c[i][j])))
                n1.append(a1[0])
                n2.append(a1[1])
                n4 += (n1[j])
                n5 += (n2[j])
            n3.append(n4)
            n6.append(n5)
            n4 = 0
            n5 = 0
    return (n3,n6)      
        
def productointernov (v1, v2):
    #v1, v2 vector primera parte real segunda imaginaria
    n_n = [0, 0]
    n1 = []
    for i in range (len(v1)//2):
        v1[i+(len(v1)//2)] = v1[ i + (len(v1)//2)] * -1 
    for i in range (len(v1)//2):
        e = (v1[i]*v2[i]-v1[i + (len(v1)//2)]*v2[i + (len(v1)//2)]),(v1[i + (len(v1)//2)]*v2[i]+v1[i]*v2[i + (len(v1)//2)])
        n1.append(e)
    for i in range (len(n1)):
        n_n = sumacomplejos(n_n, n1[i])
    print(n_n)
    return n_n
def normav(v1):
    #a vector real, b vector ima, m tamaño
    n1 = productointernov(v1,v1)
    print ((n1,"i",")**(1/2))"))
    return (n1)

def distanciavectores(v1,v2):
    # v1, v2 vectores
    v3=[]
    for i in range (len(v1)):
        v3.append(v1[i]-v2[i])
    v4 = productointernov(v3, v3)
    print ((v4,"i",")**(1/2))"))
    return v4

def esunitaria(a,b):
    # a parte real, b parte imaginaria, m tamaño
    c,d = adjuntamatriz(a,b,m)
    uni = []
    for i in range(len(a)):
        menor = []
        for j in range(len(a)):
            menori = []
            for m in range(len(c)):
                for n in range(len(c)):
                    x = 1
                    menori.append(x)
            menor.append(menori)
        uni.append(menor)
    if m ==len(a):
        print (True)
        c = 1
    else:
        print(False)
        c= 0
    return c
            
    


def eshermitiana(a,b,m):
    c,d = adjuntamatriz(a,b,m)
    if a == c and b == d:
        print ("es hermitania")
        c = 1
    else:
        print("no es hermitania")
        c = 0
    print (a,b)
    print (c,d)
    return c
    
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
v1 = [3,0,5,4,0]
v2 = [1,2,3,6,0]
v3 = [3,2,4,3]
v4 = [5,6,7,5]
n = 4
n1 = (2,3)
n2 = (4,6)
m1 = [[2,3,4,3,3],[5,6,7,4,5],[1,2,3,6,7],[1,2,3,3,4],[1,2,3,7,8]]
m2 = [[2,1,1,0,0],[1,1,-1,0,0],[1,1,1,0,0],[1,2,3,0,0],[1,2,3,0,0]]
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

#productointernov (v1,v2)
#normav(v1)
#distanciavectores(v1,v2)
accionmatrizvector (v1,v2,m1,m2)
"""fase((1,1))
esunitaria(m1,m2,3)
eshermitiana(m1,m2,3)
distanciavectores(v1,v2,v3,v4)



multiplicarcomplejos(n1,n2)
productomatrices (m5,m10)
productotensor(m6,m7,m8,m9)
sumavectoresc(v1,v2)
inversoaditivov(v1)
sumarmatriz(m1,m2,m3,m4,3,3)s
escalarxvectorc(v3,v4,2)
inversoaditivom(m1,m2,3)
escalarxmatrizc (3,2,m1,m2,3)
transpuestamatrizvector(m1,m2,3)
conjugada(m1,m2,3)
adjuntamatriz(m1,m2,3)"""
