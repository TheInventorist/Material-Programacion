# -*- coding: utf-8 -*-
"""
Created on Wed May  4 17:23:16 2022

@author: vince
"""

from random import randrange

numeroAleatorio = randrange(100)
intentos = 0
adivinado = False

while not(adivinado):
    numeroSeleccionado = int(input("Ingrese numero: "))
    intentos += 1
    if(numeroSeleccionado == numeroAleatorio):
        adivinado = True
    elif(numeroAleatorio > numeroSeleccionado):
        print("El numero es mayor")
    else:
        print("El numero es menor")

print(f"Correcto, el numero es: {numeroAleatorio}, lo logro en {intentos} intentos")
    