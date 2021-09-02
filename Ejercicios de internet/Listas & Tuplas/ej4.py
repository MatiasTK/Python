ganadores = []

cg = int(input("¿Cuantos numeros ganadores hay? "))

for i in range(cg):
    ganadores.append(int(input("Introduce un numero ganador: ")))

ganadores.sort

print("Los numeros ganadores son: ",ganadores)