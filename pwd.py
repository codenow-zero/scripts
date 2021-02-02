import os
import sys

cwd = os.getcwd()

archivos = sys.argv

if(len(archivos) > 1):

    if(archivos[1] == "-l"):
        listdir = os.listdir(cwd)
        print("\n")
        for file in listdir:

            if(os.path.isdir(file)):
                print(" --> DIR: " + file)
            else:
                print(" --> FILE: " + file)

            #print("\n --> " + file)
    else:
        print("->x ERROR: Comando no Valido!")
else:
    print("\n -> "+cwd)
    
