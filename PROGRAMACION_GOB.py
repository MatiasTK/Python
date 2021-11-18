def funcion_par(lista):
    contador = 0
    for i in range(len(lista)):
        if(lista[i] == 8):
            if(lista[i+1] % 2 == 0):
                print(lista[i+1], "Es par\n")    
                contador += 1
            if(lista[i-1] % 2 == 0):
                print(lista[i-1], "Es par\n")
                contador += 1
    print("Cantidad numeros pares:",contador,"\n")
                
def divisible(n):
    if(n % 7 == 0 and not n % 3 == 0):
        print(n,"ES el numero correcto\n")
    else:
        print(n,"No es el numero correcto\n")
            
# Ej 5
lista = [3,4,3,1,5,8,1,2,5,4,0,8,9,4,3,9,7,8,4,3,5,4,0,3,8,9,5,4,3,9,3,8,0,9,3,5,1]
funcion_par(lista)
# Ej 8
n1 = 21
n2 = 777
n3 = 651
n4 = 100
n5 = 980
divisible(n1)
divisible(n2)
divisible(n3)
divisible(n4)
divisible(n5)

#Final
input("Presiona una tecla para continuar...")
