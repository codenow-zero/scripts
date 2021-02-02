import os

listdir = os.listdir("C:\\Users\\MSI\\AppData\\Local\\Programs\\Python\\Python39\\Scripts")

os.system('cls' if os.name == 'nt' else 'clear')
print("\n")
for file in listdir:

    if(os.path.isdir(file)):
        print(" --> DIR: " + file)
    else:
        if file.endswith(".py"):
            print(" --> FILE: " + file)
        