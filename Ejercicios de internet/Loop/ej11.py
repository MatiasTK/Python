frase = input("Ingresa una frase: ")
tope = len(frase) - 1 
while tope >= 0:
    print(frase[tope],"-",end="")
    tope -= 1
