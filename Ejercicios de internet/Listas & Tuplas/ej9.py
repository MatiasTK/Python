string = input("Ingresa una palabra: ")

i = 0
contador = 0
while i < len(string):
    if string[i] == "a" or string[i] == "e" or string[i] == "i" or string[i] == "o" or string[i] == "u":
        contador += 1
    i += 1

print("Cantidad vocales:",contador)