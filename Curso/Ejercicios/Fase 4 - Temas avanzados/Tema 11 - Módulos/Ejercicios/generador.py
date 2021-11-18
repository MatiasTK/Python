import random
import math
def leer_numero(ini,fin,mensaje):
    print(mensaje)
    numero = int(input("Ingresa un numero: "))
    if numero >= ini and numero <= fin:
        return numero
    else:
        leer_numero(ini,fin,mensaje)
    
def generador():
    numeros = leer_numero(1,20,"¿Cuantos números quieres generar? [1-20]:")
    modo = leer_numero(1,3,"¿Cómo quieres redondear los numeros? [1] Al alza [2] A la baja [3] Normal")
    l = []
    for i in range(numeros):
        n = random.uniform(0,101)
        if modo == 1:
            r = math.ceil(n)
            print("Numero normal: {}\nNumero Redondeado(Ceil): {}".format(n,r))
            l.append(r)
        elif modo == 2:
            r = math.floor(n)
            print("Numero normal: {}\nNumero Redondeado(Floor): {}".format(n,r))
            l.append(r)
        else:
            r = round(n)
            print("Numero normal: {}\nNumero Redondeado(Round): {}".format(n,r))
            l.append(r)
    return list(set(l))
            
print(generador())

