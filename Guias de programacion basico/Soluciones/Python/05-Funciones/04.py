# -*- coding: utf-8 -*-
"""
Created on Thu May  5 16:05:44 2022

@author: vince
"""
def factorial(n):
    f = 1
    for i in range(1, n + 1):
        f = f * i
    return f

numero = int(input("Ingrese n: "))
resultado = factorial(numero)
print(f"{numero}! : {resultado}")












































