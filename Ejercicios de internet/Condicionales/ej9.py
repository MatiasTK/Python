edad = int(input("Ingresa tu edad:"))

if edad < 4:
    print("Felicitaciones!,podes entrar gratis :)")
elif edad > 4 and edad < 18:
    print("Tenes que pagar $5")
elif edad >= 18:
    print("Tenes que pagar $10")

