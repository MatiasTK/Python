import math
import os

task = int(input("¿Que queres hacer?\n1)Suma de vectores\n2)Resta de vectores\n3)Producto escalar\n4)Producto vectorial\n5)Salir\n"))

while task != 5:


    a = float(input("Ingresa el valor de A: "))
    at = float(input("Ingresa el angulo de A: "))
    b = float(input("Ingresa el valor de B: "))
    bt = float(input("Ingresa el angulo de B: "))

    ax = (a * math.cos(math.radians(at)))
    ay = (a * math.sin(math.radians(at)))
    bx = (b * math.cos(math.radians(bt)))
    by = (b * math.sin(math.radians(bt)))

    if task == 1:

        rx = (ax + bx)
        ry = (ay + by)

        r = math.sqrt((rx**2) + (ry**2))

        print("La resultante es:",r)

        rt = math.degrees(math.atan(ry/rx))

        print("El angulo de la resultante es:",rt)

    elif task == 2:

        rx = (ax - bx)
        ry = (ay - by)

        r = math.sqrt((rx**2) + (ry**2))

        print("La resultante es:",r)

        rt = math.degrees(math.atan(ry/rx))

        print("El angulo de la resultante es:",rt)

    elif task == 3:
        r = (ax * bx) + (ay * by)
        print("Resultado del producto escalar:",r)

    elif task == 4:
        r = (ax*by) - (ay * bx)
        print("Resultado del producto vectorial:",r)

    input("Presiona una tecla para continuar...")
    os.system("cls")    
    
    task = int(input("¿Que queres hacer?\n1)Suma de vectores\n2)Resta de vectores\n3)Producto escalar\n4)Producto vectorial\n5)Salir\n"))

input("Presiona una tecla para continuar...")