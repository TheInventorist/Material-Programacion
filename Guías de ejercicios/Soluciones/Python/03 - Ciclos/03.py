# -*- coding: utf-8 -*-
"""
Created on Tue May 10 09:39:03 2022

@author: vince
"""
n1 = int(input("Ingrese chocolates niño 1: "))
n2 = int(input("Ingrese chocolates niño 2: "))
n3 = int(input("Ingrese chocolates niño 3: "))

jugando = True
campanas = 0

while(jugando):
    campanas += 1
    n1aux = n1
    n2aux = n2
    n3aux = n3
    n2 = int(n2aux/2) + int(n1aux/2)
    n3 = int(n3aux/2) + int(n2aux/2)
    n1 = int(n1aux/2) + int(n3aux/2)
    if n1 % 2 != 0:
        n1 += 1
    if n2 % 2 != 0:
        n2 += 1
    if n3 % 2 != 0:
        n3 += 1
    if(n1 == n2 == n3):
        jugando = False

print(f"niño1: {n1}\nniño2: {n2}\nniño3: {n3}\nCampanas: {campanas}")
        
        
    
    
    
    