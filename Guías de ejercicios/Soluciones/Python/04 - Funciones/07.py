# -*- coding: utf-8 -*-
"""
Created on Thu May  5 17:09:27 2022

@author: vince
"""
from math import sqrt

def distanciaEuclidiana(x1, x2, y1, y2):
    return sqrt(((x2 - x1)**2) + ((y2 - y1)**2))

x1 = int(input("Ingrese x1: "))
y1 = int(input("Ingrese y1: "))
x2 = int(input("Ingrese x2: "))
y2 = int(input("Ingrese y2: "))

resultado = round(distanciaEuclidiana(x1, x2, y1, y2), 2)

print(f"La distancia euclidiana es: {resultado}")

