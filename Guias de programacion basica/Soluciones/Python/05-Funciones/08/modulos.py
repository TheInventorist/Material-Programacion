# -*- coding: utf-8 -*-
"""
Created on Tue May 10 16:48:58 2022

@author: vince
"""
from math import ceil

def palbraPorPosicion(palabra, posicion):
    if(len(palabra) % 2 == 0):
        mitad = int(len(palabra)/2)
        if(posicion == 0):
            print(palabra[:mitad])
        else:
            print(palabra[mitad:])
    else:
        mitad = int(ceil(len(palabra)/2))
        if(posicion == 0):
            print(palabra[:mitad])
        else:
            print(palabra[mitad-1:])