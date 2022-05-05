# -*- coding: utf-8 -*-
"""
Created on Thu May  5 15:52:56 2022

@author: vince
"""

def convertidorDeMinutos(minutos):
    return minutos // 60, minutos % 60

minutos = int(input("Ingrese minutos: "))

hrs, mins = convertidorDeMinutos(minutos)


print(f"{hrs} horas y {mins} minutos")