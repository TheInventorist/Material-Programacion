# -*- coding: utf-8 -*-
"""
Created on Thu May  5 09:52:04 2022

@author: vince
"""

def cgu(masa1, masa2, distancia):
    G = 6.67428e-11
    return G * ((masa1 * masa2) / (distancia**2))


masa1 = float(input("Ingrese masa 1: "))
masa2 = float(input("Ingrese masa 2: "))
r = float(input("Ingrese distancia: "))

fuerzaDeAtraccion = cgu(masa1, masa2, r)

print(f"La fuerza de atraccion es de : {fuerzaDeAtraccion: .2E}")

