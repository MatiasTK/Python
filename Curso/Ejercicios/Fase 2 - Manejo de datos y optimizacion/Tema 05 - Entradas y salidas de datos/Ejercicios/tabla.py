import sys
if len(sys.argv) == 3:
    if (int(sys.argv[1]) and int(sys.argv[2])) > 0 and (int(sys.argv[1]) and int(sys.argv[2])) < 10:
        filas = int(sys.argv[1])
        columnas = int(sys.argv[2])
        for fila in range(filas):
            print("")
            for columna in range(columnas):
                print("*",end="")
    else:
        print("Mal ejecutado.")
        print("Uso: tabla.py (Numero entre 1 y 9) (numero entre 1 y 9)")
else:
    print("Mal ejecutado.")
    print("Uso: tabla.py (Numero entre 1 y 9) (numero entre 1 y 9)")