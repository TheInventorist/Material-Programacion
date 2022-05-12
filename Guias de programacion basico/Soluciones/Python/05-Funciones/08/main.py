# -*- coding: utf-8 -*-
"""
Created on Tue May 10 16:48:09 2022

@author: vince
"""
from modulos import palbraPorPosicion

def main():
    palabra = input("Ingrese palabra: ")
    posicion = int(input("Ingrese posicion: "))
    palbraPorPosicion(palabra, posicion)




if(__name__ == "__main__"):
    main()