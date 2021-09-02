contrasenia = "contraseña"

input("Ingresa el usuario: ")
intento = input("Ingresa la contraseña: ")

while not(intento == contrasenia):
    print("Contraseña incorrecta")
    intento = input("Ingresa la contraseña: ")