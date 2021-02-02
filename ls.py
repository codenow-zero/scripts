import os

cwd = os.getcwd()


listdir = os.listdir(cwd)

os.system('cls' if os.name == 'nt' else 'clear')
print("\n")
for file in listdir:

    if(os.path.isdir(file)):
        print(" --> DIR: " + file)
    else:
        print(" --> FILE: " + file)