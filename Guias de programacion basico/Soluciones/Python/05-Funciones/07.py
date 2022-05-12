# -*- coding: utf-8 -*-
"""
Created on Thu May  5 17:09:27 2022

@author: vince
"""
from math import sqrt

def distanciaEuclidiana(x1, x2, y1, y2):
    return sqrt(((x2 - x1)**2) + ((y2 - y1)**2))

def perimetro(x1, x2, y1, y2):
    return (x2 - x1)*2  + (y2 - y1)*2

def circEnRec(xc, yc, rc, x1, y1, x2, y2):
    if((xc + rc) <= x2) and ((xc - rc) >= x1) and ((yc + rc) <= y2) and ((yc - rc) >= y1):
        return True
    else:
        return False

def recEnCirc(xc, yc, rc, x1, y1, x2, y2):
    if (x2 < (xc + rc)) and (x1 > (xc - rc)) and (y2 < (yc + rc)) and (y1 > (yc - rc)):
        return True
    else:
        return False
    

def main():
    x1 = int(input("Ingrese x1: "))
    y1 = int(input("Ingrese y1: "))
    x2 = int(input("Ingrese x2: "))
    y2 = int(input("Ingrese y2: "))
    xc = int(input("Ingrese xc: "))
    yc = int(input("Ingrese yc: "))
    rc = int(input("Ingrese rc: "))
    resultado1 = round(distanciaEuclidiana(x1, x2, y1, y2), 2)
    resultado2 = perimetro(x1, x2, y1, y2)
    resultado3 = circEnRec(xc, yc, rc, x1, y1, x2, y2)
    resultado4 = recEnCirc(xc, yc, rc, x1, y1, x2, y2)
    print(f"La distancia euclidiana es: {resultado1}")
    print(f"El perimetro es: {resultado2}")
    if(resultado3):
        print("El circulo esta contenido en el rectangulo")
    else:
        print("El circulo NO esta contenido en el rectangulo")
    if(resultado4):
        print("El rectangulo esta contenido en el ciruclo")
    else:
        print("El rectangulo NO esta contenido en el circulo")

if(__name__ == "__main__"):
    main()
