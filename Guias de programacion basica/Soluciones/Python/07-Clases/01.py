# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 10:49:11 2022

@author: vince
"""

class Pokemon:
    def __init__(self, nombre, tipo, vida, ataque, velocidad):
        self.nombre = nombre
        self.tipo = tipo
        self.vida = vida
        self.ataque = ataque
        self.velocidad = velocidad
    
    def atacar(self): # getter
        return self.ataque * 0.2
    
    def recibirAtaque(self, ataquePokemon):
        self.vida -= ataquePokemon
        return self.vida
    
    def __str__(self):
        return f"Pokemon: {self.nombre} / {self.tipo} / {self.vida} / {self.ataque} / {self.velocidad}"


def main():
    print("Data Pokemon: nombre, tipo, vida, ataque, velocidad")
    stringData1 = input("Ingrese data Pokemon 1: ")
    stringData2 = input("Ingrese data Pokemon 2: ")
    listaData1 = stringData1.split(" ")
    listaData2 = stringData2.split(" ")
    pk1 = Pokemon(listaData1[0], listaData1[1], int(listaData1[2]), int(listaData1[3]), int(listaData1[4]))
    pk2 = Pokemon(listaData2[0], listaData2[1], int(listaData2[2]), int(listaData2[3]), int(listaData2[4]))
    
    turno = 0
    if(pk1.velocidad > pk2.velocidad):
        turno = 1
    else:
        turno = 2
    
    while(pk1.vida > 0 and pk2.vida > 0):
        if(turno == 1):
            turno = 2
            print(f"{pk1.nombre}[{pk1.vida}] ataca a {pk2.nombre}[{pk2.vida}] / {pk2.nombre} pierde {pk1.atacar()} hp [{pk2.recibirAtaque(pk1.atacar())}] ")
        else:
            turno = 1
            print(f"{pk2.nombre}[{pk2.vida}] ataca a {pk1.nombre}[{pk1.vida}] / {pk1.nombre} pierde {pk2.atacar()} hp [{pk1.recibirAtaque(pk2.atacar())}] ")
    
    if(pk1.vida > 0):
        print(f"{pk1.nombre} gana el combate contra {pk2.nombre}, quedando con {pk1.vida} hp")
    else:
        print(f"{pk2.nombre} gana el combate contra {pk1.nombre}, quedando con {pk2.vida} hp")


if(__name__ == "__main__"):
    main()