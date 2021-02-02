import os
import sys

cwd = os.getcwd()

proyecto = sys.argv

os.chdir(cwd)

def crearFichero(nombreFich):
    try:
        if(os.path.isfile(nombreFich) != True):
            archivo = open(nombreFich, 'w')
            archivo.write("")
            archivo.close()
            print(f"->o Archivo {nombreFich} Creado!")
        else:
            print(f"->w WARNING: Archivo {nombreFich} Existente!")
    except OSError:
        print(f"->x ERROR: {OSError}")


crearFichero(proyecto[1])