# -*- coding: utf-8 -*-
"""
Created on Wed May  4 16:24:07 2022

@author: vince
"""

estatura = float(input("Estatura: "))
peso = int(input("Peso: "))
edad = int(input("Edad: "))

imc = round(peso / (estatura**2), 2)

if(imc < 22 and edad < 45):
    riesgo = "bajo"
elif(imc >= 22 and edad < 45) or (imc < 22 and edad >= 45):
    riesgo = "medio"
elif(imc >= 22 and edad >= 45):
    riesgo = "alto"

print(f"Su riesgo es {riesgo} y su IMC es {imc}")