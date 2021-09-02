import os

task = 0

debo = 0
pagado = 0

facturas = {}

while not task == 4:
    task = int(input("¿Que Desea hacer?\n1)Añadir factura\n2)Pagar Factura\n3)Mostrar facturas pendientes\n4)Terminar\n"))
    os.system("cls")

    if task == 1:
        numero = int(input("Introduci el numero de factura: "))
        coste = int(input("Introduci el coste de la factura: "))
        facturas[numero] = coste 
        debo += coste
    elif task == 2:
        numero = int(input("Introduci el numero de factura: "))
        pagado += facturas[numero]
        debo -= facturas[numero]
        del facturas[numero]
    elif task == 3:
        for x in facturas:
            print("Factura Nro:",x,"Coste:",facturas[x],"\n")
        input("Presiona enter para continuar...")
    elif task == 4:
        break
    os.system("cls")
    print("Precio total de facturas inpagas:",debo,"\nPrecio total de facturas pagadas:",pagado)
    input("Presiona enter para continuar...")
    os.system("cls")


    