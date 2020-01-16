import math

def sumacomplejos(a,b):
    return (a[0]+b[0],a[1]+b[1])
    
def prettyprintingc(c):
    print(c[0],"+",c[1],"i")

def restacomplejos(a,b):
    return (a[0]-b[0],a[1]-b[1])

def multicomplejos(a,b):
    return((a[0]*b[0]-a[1]*b[1]),(a[0]*b[0]+a[1]*b[1]))

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
def fase(a): 
    return a[1]








