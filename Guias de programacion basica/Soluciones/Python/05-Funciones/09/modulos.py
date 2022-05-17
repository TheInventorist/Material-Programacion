# -*- coding: utf-8 -*-
"""
Created on Tue May 10 10:18:48 2022

@author: vincent bla bla
"""
from datetime import date


def verificadorAnual(anio):
    anioActual = date.today().year
    diferencia = anioActual - anio
    if(diferencia >= 4):
        return 25
    elif(diferencia == 3):
        return 15
    elif(diferencia == 2):
        return 5
    else:
        return 0
    
def verificadorPromocion(ranking):
    if(ranking <= 10):
        return 50
    elif(11 <= ranking <= 20):
        return 30
    elif(21 <= ranking <= 30):
        return 10
    else:
        return 0
    
def verificadorMejorDescuento(descuento1, descuento2):
    if(descuento1 > descuento2):
        return descuento1
    else:
        return descuento2
    

