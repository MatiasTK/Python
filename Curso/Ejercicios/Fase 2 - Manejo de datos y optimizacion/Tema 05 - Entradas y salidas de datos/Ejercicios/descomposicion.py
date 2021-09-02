# CASI PERO NO!
"""
import sys
entero = int(sys.argv[1])

if entero > 0 and len(sys.argv) == 2:
    string = str(entero)

    x = -1

    while True:    
        for y in range(0,len(string[0:x])):
            print("0",end="")
        print(string[x])
        if(string[x] == string[0]):
            break
        x -= 1
        
else:
    print("Mal ejecutado")
    print("Uso: descomposicion.py (Numero mayor a 0)")
"""

#El correcto

import sys

if len(sys.argv) == 2:
        numero = int(sys.argv[1])
        if numero > 0 and numero < 9999:
            longitud = len(str(numero))
            string = str(numero)

            for i in range(longitud): #lo recorre hasta el ultimo numero que es el len de un string -> no puedo hacer len de un numero
              #  print(("{:04d}").format(int(string[i])))  - >lo corto a 4 digitos y imprimo el string[i] que puede ser 3 pero como es un numero lo convierto eso a int (Sino va a tirar error el 04d usa int no string)
              # print(("{:04d}").format(int(string[longitud-1-i]))) Con esta forma la puedo recorrer al reves 
                print(("{:04d}").format(int(string[longitud-1-i]) * 10 ** i)) # de esta forma logro que se multiplique por la posicion asi tengo los numeros correctos
        else:
            print("Mal ejecutado")
            print("Utilizacion: descomposicion.py (Numero mayor a 0)") 
else:
    print("Mal ejecutado")
    print("Utilizacion: descomposicion.py (Numero mayor a 0)")

#Testeado con el numero 3647, explicacion =
""" 
Primer iteracion
String[longitud-1-i] -> 5 - 1 - 0 -> string[4] -> 7 || 7 * 10 ^ i -> 7 * 10 ^ 0 -> 7 * 1 -> Imprime 0007
Segunda iteracion
String[longitud-1-i] -> 5 - 1 - 1 -> string[3] -> 4 || 4 * 10 * i -> 4 * 10 ^ 1 -> 40 -> imrpime 0040 ( Si no hago esto ultimo imprimiria 0004)"""