import math
import os

def area(choice):
    if choice == 1:
        if int(input("¿Que queres hacer?\n1)Area\n2)Perimetro\n")) == 1:
            base = float(input("Ingresa la base del triangulo: "))
            altura = float(input("Ingresa la altura del triangulo: "))
            print("-------------------------------------")
            print("Area del triangulo:",(base*altura)/2)
            print("Formula: (Base * Altura)/2")
            print("-------------------------------------")
        else:
            l1 = float(input("Ingresa el primer lado del triangulo: "))
            l2 = float(input("Ingresa el segundo lado del triangulo: "))
            l3 = float(input("Ingresa el primer lado del triangulo: "))
            print("-------------------------------------")
            print("Perimetro del triangulo:",(l1+l2+l3))
            print("Formula: Lado 1 + Lado 2 + Lado 3")
            print("-------------------------------------")
    elif choice == 2:
        if int(input("¿Que queres hacer?\n1)Area\n2)Perimetro\n")) == 1:
            lado = float(input("Ingresa un lado del cuadrado: "))
            print("-------------------------------------")
            print("Area del cuadrado:",lado**2)
            print("Formula: Lado^2")
            print("-------------------------------------")
        else:
            l1 = float(input("Ingresa el primer lado del cuadrado: "))
            l2 = float(input("Ingresa el segundo lado del cuadrado: "))
            l3 = float(input("Ingresa el primer lado del cuadrado: "))
            l4 = float(input("Ingresa el cuarto lado del cuadrado: "))
            print("-------------------------------------")
            print("Perimetro del cuadrado:",(l1+l2+l3+l4))
            print("Formula: Lado1 + Lado2 + Lado3 + Lado4")
            print("-------------------------------------")
    elif choice == 3:
        if int(input("¿Que queres hacer?\n1)Area\n2)Longitud\n")) == 1:
            radio = float(input("Ingresa el radio del circulo: "))
            print("-------------------------------------")
            print("Area del circulo:",(math.pi * (radio**2))) 
            print("Formula: Pi * (Radio^2)")
            print("-------------------------------------")
        else:
            radio = float(input("Ingresa el radio del circulo: "))
            print("-------------------------------------")
            print("Longitud del circulo:",(math.pi * 2 * radio)) 
            print("Formula: 2 * Pi * Radio")
            print("-------------------------------------")
    elif choice == 4:
        if int(input("¿Que queres hacer?\n1)Area\n2)Longitud\n")) == 1:
            base = float(input("Ingresa la base del rectangulo: "))
            altura = float(input("Ingresa la altura del rectangulo: "))
            print("-------------------------------------")
            print("Area del rectangulo:",base * altura) 
            print("Formula: base * altura")
            print("-------------------------------------")
        else:
            l1 = float(input("Ingresa el primer lado del rectangulo: "))
            l2 = float(input("Ingresa el segundo lado del rectangulo: "))
            l3 = float(input("Ingresa el primer lado del rectangulo: "))
            l4 = float(input("Ingresa el cuarto lado del rectangulo: "))
            print("-------------------------------------")
            print("Perimetro del rectangulo:",(l1 + l2 + l3 + l4)) 
            print("Formula: Lado1 + Lado2 + Lado3 + Lado4")
            print("-------------------------------------")
    elif choice == 5:
        if int(input("¿Que queres hacer?\n1)Area\n2)Volumen\n")) == 1:
            radio = float(input("Ingresa el radio del cilindro: "))
            altura = float(input("Ingresa la altura del cilindro: "))
            print("-------------------------------------")
            print("Area del cilindro:",(2 * math.pi * radio * (radio + altura))) 
            print("Formula: 2 * Pi * Radio * (Radio + Altura)")
            print("-------------------------------------")
        else:
            radio = float(input("Ingresa el radio del cilindro: "))
            altura = float(input("Ingresa la altura del cilindro: "))
            print("-------------------------------------")
            print("Volumen del cilindro:",((radio**2) * math.pi * altura)) 
            print("Formula: Radio^2 * Pi * Altura")
            print("-------------------------------------")
    elif choice == 6:
        if int(input("¿Que queres hacer?\n1)Volumen\n2)Area\n")) == 1:
            radio = float(input("Ingresa el radio del cono: "))
            altura = float(input("Ingresa la altura del cono: "))
            print("-------------------------------------")
            print("Volumen del cono:",(math.pi * (radio**2) * altura)/3)
            print("Formula: (Pi * Radio^2 * Altura)/3")
            print("-------------------------------------")
        else:
            print("-------------------------------------")
            print("No lo implemente, no estoy muy seguro como se calcula pero te tiro una formula que encontre:")
            print("Pi * Radio * (Radio + Angulo)")
            print("-------------------------------------")
    elif choice == 7:
        if int(input("¿Que queres hacer?\n1)Area\n2)Volumen\n")) == 1:
            radio = float(input("Ingresa el radio de la esfera: "))
            print("-------------------------------------")
            print("Area de la esfera:",(4 * math.pi * (radio**2)))
            print("Formula: 4 * Pi * Radio^2")
            print("-------------------------------------")
        else:
            radio = float(input("Ingresa el radio de la esfera: "))
            print("-------------------------------------")
            print("Volumen de la esfera:",((4/3)* math.pi * (radio**3))) 
            print("Formula: 4/3 * Pi * Radio^3")
            print("-------------------------------------")
    else:
        print("-------------------------------------")
        print("Ingresaste un numero incorrecto")
        print("-------------------------------------")

choice = 0
print("Bienvenido a la calculadora de areas!")
while not choice > 0 and choice < 7:
    choice = int(input("Elegi una opcion:\n1)Triangulo\n2)Cuadrado\n3)Circulo\n4)Rectangulo\n5)Cilindro\n6)Cono\n7)Esfera\n")) 

area(choice)

repeat = "S"
while repeat == "S" or repeat == "s":
    repeat = input("¿Queres hacer otra cuenta? S/N\n")
    if repeat == 's' or repeat == 'S':
        os.system("cls")
        choice = int(input("Elegi una opcion:\n1)Triangulo\n2)Cuadrado\n3)Circulo\n4)Rectangulo\n5)Cilindro\n6)Cono\n7)Esfera\n"))
        area(choice) 

print("Gracias por utilizarme!")
input("Presiona cualquier tecla para continuar...")


