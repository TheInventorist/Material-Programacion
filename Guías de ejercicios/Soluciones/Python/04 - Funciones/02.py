# -*- coding: utf-8 -*-
"""
Created on Thu May  5 10:25:15 2022

@author: vince
"""
from math import pi

def perimetro(r):
    return pi * r * 2

def area(r):
    return pi * (r ** 2)

radio = float(input("Ingrese radio: "))

resultadoPerimetro = round(perimetro(radio), 3)
resultadoArea = round(area(radio), 3)

print(f"El perimetro de {radio} es: {resultadoPerimetro}")
print(f"El area de {radio} es: {resultadoArea}")
    