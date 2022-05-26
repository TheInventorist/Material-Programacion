from modules import cargarData, buscaNombres

def main():
    estuctura = cargarData()
    rut = input("Ingrese rut: ")
    nombre = buscaNombres(estuctura, rut)
    print(f"el nombre de {rut} es: {nombre}")


if(__name__ == "__main__"):
    main()