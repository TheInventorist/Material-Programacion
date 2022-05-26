def leerArchivo(nombreArchivo):
    contenido = []
    f = open(nombreArchivo, "r")
    for line in f:
        contenido.append(line)
    f.close()
    reworkedList = []
    for item in contenido:
        reworked = item.split("\n")
        reworkedList.append(reworked[0])
    return reworkedList


def estructurarDatos(lista1, lista2):
    matriz = []
    for i in range(len(lista1)):
        matriz.append([])
        matriz[i].append(lista1[i])
        matriz[i].append(lista2[i])
    return matriz


def cargarData():
    ruts = leerArchivo("Ruts.txt")
    nombres = leerArchivo("Nombres.txt")
    estuctura = estructurarDatos(ruts, nombres)
    return estuctura


def buscaNombres(estructura, rut):
    for i in range(len(estructura)):
        if(estructura[i][0] == rut):
            return estructura[i][1]
    return 0
