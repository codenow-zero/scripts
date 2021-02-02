import os
import sys

nombreDir = sys.argv

cwd = os.getcwd()

os.chdir(cwd)

try:
    os.rmdir(nombreDir)
    print(f"->o Archivo {nombreDir} Eliminado!")
except OSError:
    print(f"->x ERROR: {OSError}")