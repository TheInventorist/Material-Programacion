# -*- coding: utf-8 -*-
"""
Created on Thu May  5 10:47:08 2022

@author: vince
"""

def dobleFactorial(n):
    if(n <= 0):
        return 1
    else:
        if(n % 2 == 0):
            inicio = 2
        else:
            inicio = 1
        f = 1
        for i in range(inicio, n + 1, 2):
            f = f * i
        return f
            
numero = int(input("Ingrese n!! : "))

resultado = dobleFactorial(numero)

print(f"El doble factorial de {numero}!! es: {resultado}")