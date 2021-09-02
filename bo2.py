import random

print("\033[36m","\nBienvenido al generador del boludo que tiene que abrir la puerta\nAhora en Python! :D")
print("\033[0m")

sorteo = 'S'

while sorteo == 'S' or sorteo == 's':
    aleatorio = random.randrange(0,4)

    if aleatorio == 0:
        print("Tiene que abrir la puerta el","\033[31m","BLANCO")
        print("\033[0m")
    elif aleatorio == 1:
        print("Tiene que abrir la puerta el","\033[33m","AMARILLO")
        print("\033[0m")
    elif aleatorio == 2:
        print("Tiene que abrir la puerta el","\033[32m","VERDE")
        print("\033[0m")
    elif aleatorio == 3:
        print("Tiene que abrir la puerta el","\033[34m","AZUL")
        print("\033[0m")

    sorteo = input("¿Queres hacer otro sorteo? (S/N)\n")
else:
    print("Gracias por participar!")