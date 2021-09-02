import os
task = 0

notas = []
completadas = []
pendientes = []



print("To-Do List :)")
while not task == 7:
    for x in range(0,len(notas)):
        paso = False
        for y in range(0,len(completadas)):
            if x == y: 
                print("\033[92m")
                print("\n",x+1,"-",notas[x])
                print("\033[00m")
            paso = True
        for y in range(0,len(pendientes)):
            if x == y:
                print("\033[93m")
                print("\n",x+1,"-",notas[x])
                print("\033[00m")
            paso = True
        if 
        print("\n",x+1,"-",notas[x])
    task = int(input("\n1)Nueva nota\n2)Eliminar Nota\n3)Marcar como completado\n4)Marcar como pendiente\n5)Mostrar completadas\n6)Mostrar pendientes\n7)Salir\n"))
    if task == 1:
        os.system("cls")
        notas.append(input("Texto a ingresar: "))
    elif task == 2:
        notas.remove(notas[int(input("Numero de nota: "))-1])
        os.system("cls")
    elif task == 3:
        numero = int(input("Numero de nota: "))
        completadas.append(notas[numero-1])
        os.system("cls")
    elif task == 4:
        numero = int(input("Numero de nota: "))
        pendientes.append(notas[numero-1])
        os.system("cls")
    elif task == 5:
        os.system("cls")
        while not(task == 3 or task == 4):
            for x in range(0,len(completadas)):
                print("\033[92m")
                print(x+1,"-",completadas[x])
                print("\033[00m")
            task = int(input("\n1)Nueva completada\n2)Eliminar completada\n3)Menu anterior\n4)Salir\n"))
            if task == 1:
                os.system("cls")
                completadas.append(input("Texto a ingresar: "))
            elif task == 2:
                completadas.remove(completadas[int(input("Numero de nota: "))-1])
                os.system("cls")
        else:
            if task == 4:
                task = 7
        os.system("cls")
    elif task == 6:
        os.system("cls")
        while not(task == 3 or task == 4):
            for x in range(0,len(pendientes)):
                print("\033[93m")
                print(x+1,"-",pendientes[x])
                print("\033[00m")
            task = int(input("\n1)Nueva pendiente\n2)Eliminar pendiente\n3)Menu anterior\n4)Salir\n"))
            if task == 1:
                os.system("cls")
                pendientes.append(input("Texto a ingresar: "))
            elif task == 2:
                pendientes.remove(pendientes[int(input("Numero de nota: "))-1])
                os.system("cls")
        else:
            if task == 4:
                task = 7
                

input("Presiona enter para continuar...")