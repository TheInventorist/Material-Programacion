# -*- coding: utf-8 -*-
"""
Created on Tue May 17 10:44:47 2022

@author: vince
"""
def constructorMatriz(n):
    lista = []
    for i in range(n):
        lista.append([])
    return lista


def main():
    n = int(input("Ingrese cantidad nombres: "))
    
    matriz = constructorMatriz(n)
        
    for i in range(n):
        nombre = input(f"Ingrese nombre {i+1}: ")
        matriz[i].append(nombre)

    print(matriz)

if(__name__ == "__main__"):
    main()