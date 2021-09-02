dic = {}

nombre = input("Nombre: ")
edad = input("Edad: ")
direccion = input("Direccion: ")
telefono = input("Telefono: ")

dic["Nombre"] = nombre
dic["Edad"] = edad
dic["Direccion"] = direccion
dic["Telefono"] = telefono

print(dic["Nombre"],"tiene",dic["Edad"],"años, vive en",dic["Direccion"],"y su numero de telefono es",dic["Telefono"])

