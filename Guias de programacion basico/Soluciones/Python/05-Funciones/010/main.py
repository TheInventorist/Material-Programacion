# -*- coding: utf-8 -*-
"""
Created on Tue May 10 11:39:05 2022

@author: vince
"""
from modulos import consumoDiario

def main():
    GB = int(input("Cantidad de GB del usuario: "))
    planEnMb = GB * 1024
    print(f"La cantidad de Gb en Mb del usuarios es: {planEnMb}")
    consumoDiario(planEnMb)



if(__name__ == "__main__"):
    main()

