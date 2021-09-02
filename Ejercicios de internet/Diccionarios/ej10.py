task = 0

clientes = []
base_datos = {}

nif = 0

while not task == 6:
    task = int(input("¿Que desea hacer?\n1)Añadir cliente\n2)Preguntar por NIF y eliminar\n3)Preguntar por NIF y mostrar datos\n4)Mostrar datos de clientes con NIF y nombre\n5)Mostrar clientes preferentes con NIF y nombre\n6)Terminar programa\n"))
    
    if task == 1:
        cliente = input("Datos clientes en formato csv(nombre, dirección, teléfono, correo, preferente): ")
        clientes = cliente.split(",")
        base_datos[nif] = clientes
        nif += 1
    elif task == 2:
        nif_r = int(input("NIF del cliente a remover: "))
        del base_datos[nif_r]
    elif task == 3:
        nif_s = int(input("NIF del cliente para mostrar datos:"))
        print(base_datos[nif_s])
    elif task == 4:
        print(base_datos)
    elif task == 5:
        for x in range(0,len(base_datos)):
            if base_datos[x][-1] == "S" or base_datos[x][-1] == "s" or base_datos[x][-1] == "Si" or base_datos[x][-1] == "si" :
                print(base_datos[x])
    elif task == 6:
        break
            



