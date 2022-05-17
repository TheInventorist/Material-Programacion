# -*- coding: utf-8 -*-
"""
Created on Thu May  5 11:23:17 2022

@author: vince
"""
from math import pi

def probabilidadCaptura(St, T, n):
    F = 1.19909
    resultado = 1
    for i in range(n + 1):
        operacion = (1 - ((4 * (St - (F**T))**2 ) / ((pi**2) * ((2*i) - 1)**2)))
        resultado = resultado * operacion
    return resultado

St = float(input("Ingrese salud total maxima: "))
T = float(input("Ingrese grado timidez-agresividad: "))
n = int(input("Ingrese n: "))

probabilidad = round(probabilidadCaptura(St, T, n), 2)

print(f"La probabilidad de captura es : {probabilidad}")

