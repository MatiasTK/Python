import sys
#argv[0] es como en C -> Es el nombre del script
if len(sys.argv) == 3:
    texto = sys.argv[1]
    repeticiones = int(sys.argv[2])

    for r in range(repeticiones):
        print(texto)
else: 
    print("Error,introduce los argumentos correctamente")
    print("Usage: escribir_lineas.py 'String' number")
