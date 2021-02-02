import os
import sys

directorio = os.getcwd()
opcion = sys.argv


def crearFichero(nombreFich, dato):
    try:
        if os.path.isfile(nombreFich) != True:
            archivo = open(nombreFich, "w")
            archivo.write(dato)
            archivo.close()
            print(f"->o Archivo {nombreFich} Creado!")
        else:
            print(f"->w WARNING: Archivo {nombreFich} Existente!")
    except OSError:
        print(f"->x ERROR: {OSError}")


dato = "Notas:\n\n"

crearFichero(opcion[1] + ".txt", dato)
