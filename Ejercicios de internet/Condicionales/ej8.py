puntuacion = float(input("Puntuacion: "))
paga = 2400 * puntuacion

if puntuacion == 0.0:
    print("Tu nivel de rendimiento es Inaceptable",end="")
elif puntuacion == 0.4:
    print("Tu nivel de rendimiento es Aceptable", end="")
elif puntuacion >= 0.6:
    print("Tu nivel de rendimiento es Meritorio",end="")
else:
    print("Puntuacion incorrecta")

print(",tu paga sera:",paga)