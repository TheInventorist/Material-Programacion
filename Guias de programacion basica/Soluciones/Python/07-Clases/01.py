# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 16:07:39 2022

@author: vince
"""
class Pokemon:
    def __init__(self, nombre, tipo, vida, ataque, velocidad):
        self.nombre = nombre
        self.tipo = tipo
        self.vida = vida
        self.ataque = ataque
        self.velocidad = velocidad
        
    def __str__(self):
        return f"Pokemon: {self.nombre} / {self.tipo} / {self.vida} / {self.ataque} / {self.velocidad}"
    
    def atacar(self):
        return self.ataque * 0.2
    
    def recibirAtaque(self, ataqueRecibido):
        self.vida -= ataqueRecibido
        return self.vida


def main():
    print("Data Pokemon: nombre, tipo, vida, ataque, velocidad")
    stringPk1 = input("Ingrese data pokemon1: ")
    stringPk2 = input("Ingrese data pokemon2: ")
    print("")
    datapk1 = stringPk1.split(" ")
    datapk2 = stringPk2.split(" ")
    pk1 = Pokemon(datapk1[0], datapk1[1], int(datapk1[2]), int(datapk1[3]), int(datapk1[4]))
    pk2 = Pokemon(datapk2[0], datapk2[1], int(datapk2[2]), int(datapk2[3]), int(datapk2[4]))
    print(pk1)
    print(pk2)
    print("")
    turno = 0
    if(pk1.velocidad > pk2.velocidad):
        turno = 1
    else:
        turno = 2
        
    while(pk1.vida > 0 and pk2.vida > 0):
        if(turno == 1):
            turno = 2
            pokeAtaque = round(pk1.atacar(), 1)
            pokeVidaAtacado = round(pk2.recibirAtaque(pk1.atacar()), 1)
            vida1 = round(pk1.vida, 1)
            vida2 = round(pk2.vida, 1)
            print(f"{pk1.nombre}[{vida1}] ataca a {pk2.nombre}[{vida2}] / {pk2.nombre} pierde {pokeAtaque} hp [{pokeVidaAtacado}]")
        else:
            turno = 1
            pokeAtaque = round(pk2.atacar(), 1)
            pokeVidaAtacado = round(pk1.recibirAtaque(pk2.atacar()), 1)
            vida1 = round(pk1.vida, 1)
            vida2 = round(pk2.vida, 1)
            print(f"{pk2.nombre}[{vida2}] ataca a {pk1.nombre}[{vida1}] / {pk1.nombre} pierde {pokeAtaque} hp [{pokeVidaAtacado}]")
            
    print("")
    if(pk1.vida > 0):
        vida1 = round(pk1.vida, 1)
        print(f"{pk1.nombre} gana el combate contra {pk2.nombre}, quedando con {vida1} hp")
    else:
        vida2 = round(pk2.vida, 1)
        print(f"{pk2.nombre} gana el combate contra {pk1.nombre}, quedando con {vida2} hp")
        
if __name__ == "__main__":
    main()