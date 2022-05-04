# -*- coding: utf-8 -*-
"""
Created on Wed May  4 16:32:05 2022

@author: vince
"""

distancia = float(input("Distancia: "))
angulo = float(input("Angulo: "))

lugar = ""

if(distancia <= 7):
    lugar = "PILETA"
elif(20 >= distancia > 7):
    if(90 > angulo >= 40):
        lugar = "PUBLICO"
    else:
        lugar = "CEMENTO"
elif(35 >= distancia > 20):
    if(90 >= angulo > 45):
        lugar = "PUBLICO"
    elif(45 >= angulo > 0):
        lugar = "AREA VERDE"
    elif(135 >= angulo > 90):
        lugar = "AREA VERDE"
    elif(225 >= angulo > 180):
        lugar = "AREA VERDE"
    elif(315 >= angulo > 270):
        lugar = "AREA VERDE"
    else:
        lugar = "CEMENTO"
elif(47 >= distancia > 35):
    if(90 >= angulo > 45):
        lugar = "PUBLICO"
    else:
        lugar = "CEMENTO"
else:
    lugar = "FUERA DE LA PLAZA"
    

print(f"{lugar}")










