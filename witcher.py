from colorama import Fore

respuesta = "s"
print("Bienvenido a la calculadora de regateos del The Witcher 3!")
while respuesta == "s" or respuesta.upper() == 's' or respuesta.upper() == 'S':
    inicial = float(input("Precio inicial: "))
    final = float(input("Precio final: "))

    mitad = (final - inicial) / 2 + inicial
    cuarenta = ((final - inicial) * 40) / 100 + inicial
    treinta = ((final - inicial) * 30) / 100 + inicial
    sesenta = ((final - inicial) * 60) / 100 + inicial

    print("El 30% es",Fore.BLUE,treinta,Fore.WHITE)
    print("El 40% es",Fore.GREEN,cuarenta,Fore.WHITE)
    print("El 50% es",Fore.YELLOW,mitad,Fore.WHITE)
    print("El 60% es",Fore.RED,sesenta,Fore.WHITE)

    print("¿Queres hacer otra cuenta? (S/N)")
    respuesta = input()
    
    if respuesta == 'N' or respuesta == 'n':
        print("Gracias por utilizar la calculadora de regateos!\nVer 3.0, ahora en Python!\n")
