# -*- coding: utf-8 -*-
"""
Created on Tue May 10 10:19:39 2022

@author: vince
"""
from modulos import verificadorAnual, verificadorPromocion, verificadorMejorDescuento

def main():
    codigo = input("Ingrese codigo: ")
    anio = codigo[:4]
    ranking = codigo[7:10]
    descuentoPorAnio = verificadorAnual(int(anio))
    descuentoPorPromocion = verificadorPromocion(int(ranking))
    descuentoFinal = verificadorMejorDescuento(descuentoPorAnio, descuentoPorPromocion)
    print(f"El mejor descuento es: {descuentoFinal}")



if(__name__ == "__main__"):
    main()