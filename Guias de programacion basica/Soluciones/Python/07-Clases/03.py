# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 11:39:43 2022

@author: vince
"""

class Cuenta:
    def __init__(self, nombreCliente, numeroCuenta, tipoInteres, saldo):
        self.nombreCliente = nombreCliente
        self.numeroCuenta = numeroCuenta
        self.tipoInteres = tipoInteres
        self.saldo = saldo
    
    def ingreso(self, cantidadIngresada):
        if(cantidadIngresada >= 0):
            self.saldo += cantidadIngresada
            return True
        else:
            return False
    
    def reintegro(self, retiro):
        if(retiro > 0):    
            if(self.saldo > retiro):
                self.saldo -= retiro
                return True
            else:
                return False
        else:
            return False
        
    def transferencia(self, cuentaDestino, importe):
        if(self.reintegro(importe)):
            cuentaDestino.ingreso(importe)
            return True
        else:
            return False
        
def main():
    cuenta1 = Cuenta("Renato", "123", 2, 1000)
    cuenta2 = Cuenta("Paula", "321", 4, 2000)
    print("------------")
    print(f"Ingreso de 2000 a cuenta 1 ({cuenta1.nombreCliente}): {cuenta1.ingreso(2000)}")
    print(f"Nuevo saldo: {cuenta1.saldo}")
    print("------------")
    print(f"Ingreso de 4000 a cuenta 2 ({cuenta2.nombreCliente}): {cuenta2.ingreso(4000)}")
    print(f"Nuevo saldo: {cuenta2.saldo}")
    print("------------")
    print(f"{cuenta1.nombreCliente} le transfiere a {cuenta2.nombreCliente} 2000")
    print(f"Saldo de {cuenta1.nombreCliente}: {cuenta1.saldo}")
    print(f"Saldo de {cuenta2.nombreCliente}: {cuenta2.saldo}")
    cuenta1.transferencia(cuenta2, 2000)
    print(f"Nuevo saldo de {cuenta1.nombreCliente}: {cuenta1.saldo}")
    print(f"Nuevo saldo de {cuenta2.nombreCliente}: {cuenta2.saldo}")

if __name__ == "__main__":
    main()
            
            