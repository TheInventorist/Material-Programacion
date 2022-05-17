# -*- coding: utf-8 -*-
"""
Created on Tue May 10 11:38:54 2022

@author: vince
"""

def consumoDiario(planMB):
    enServicio = True
    dia = 1
    consumoTotal = 0
    estadoActual = 0
    while(enServicio):
        consumoDiario = int(input(f"Consumo dia {dia} en mb: "))
        consumoTotal += consumoDiario
        estadoActual = verificadorPlan(planMB, consumoTotal, estadoActual)
        dia += 1
        if consumoTotal >= planMB or consumoDiario == 0:
            enServicio = False
    cargo = estadoActual * 150
    print(f"Se consumieron {consumoTotal}mb y un cargo de {cargo}$")


def verificadorPlan(planMB, consumo, estado):
    if(planMB*0.8 > consumo >= planMB*0.5):
        if(estado != 1):
            print("50% consumo del plan")
            return 1
        else:
            return estado
    elif(planMB > consumo >= planMB*0.8):
        if(estado != 2):
            print("80% consumo del plan")
            return 2
        else:
            return estado
    elif(consumo >= planMB):
        if(estado != 3):
            print("100% consumo del plan")
            return 3
        else:
            return estado
    else:
        return estado
    
    
    
    