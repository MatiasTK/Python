frase = input("Ingresa una frase: ")
letra = input("Ingresa la letra que quieras contar: ")

contador = 0
x = 0
while x < len(frase):
    if frase[x] == letra:
        contador += 1
    x += 1

print("Veces que aparece",letra,":",contador) 