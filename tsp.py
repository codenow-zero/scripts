import os
import sys

directorio = os.getcwd()
opciones = sys.argv

def cambioDir(dirs):
    try:
        os.chdir(dirs)
    except OSError:
        print(f"->x ERROR: .settings {OSError}")


def crearDirectorio(nombreDir):
    try:
        if os.path.isdir(nombreDir) != True:
            os.mkdir(nombreDir)
            print(f"->o Directorio {nombreDir} Creado!")
        else:
            print(f"->w WARNING: Directorio {nombreDir} Existente!")
    except OSError:
        print(f"->x ERROR: {OSError}")


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


if len(opciones) < 2:
    print('->x ERROR: Falta Nombre del proyecto!')
elif(len(opciones) == 2) and (opciones[1] == "-h" or opciones[1] == "-help"):
    print(
        """
    Comandos disponibles:

        ts nombreProyecto           CREA DIRECTORIO Y ARCHIVO index.ts


        ***PROXIMAMENTE OPCIONES
        """
    )
elif(opciones[1] == "-v" or opciones[1] == "--version"):
    print(
        """Version:
        Version Script: v1.0.0 alpha
        """
    )
else:
    crearDirectorio(opciones[1])
    cambioDir(opciones[1])
    crearFichero('index.ts', 'console.log("Script Automatizado creado por https://twitter.com/alexupps");')