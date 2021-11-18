import sys
""" # CREO QUE SE PUEDE MEJORAR XD

try:
    fichero = open("contador.txt","r")
    texto = fichero.read()
    contador = int(texto)
    if len(texto) == 0:
        raise TypeError
    elif len(sys.argv) == 2:
        fichero.close()
        fichero = open("contador.txt","w")
        if sys.argv[1] == "inc":
            contador += 1
            fichero.write(str(contador))
            fichero.close()
        elif sys.argv[1] == "dec":
            contador -= 1
            fichero.write(str(contador))
            fichero.close()
        else:
            fichero.close()
            print(contador)
    else:
        fichero.close()
        print(contador)
except:
    print("Error: Fichero corrupto. Volve a ejecutar")
    fichero = open("contador.txt","w")
    fichero.write("0")
    fichero.close() """

# Forma del profe

fichero = open("contador.txt","a+")
fichero.seek(0)
contenido = fichero.readline()

if len(contenido) == 0:
    contenido = "0"
    fichero.write(contenido)

fichero.close()

try:
    contador = int(contenido)
    
    if len(sys.argv) == 2:
        if sys.argv[1] == "inc":
            contador += 1
        elif sys.argv[1] == "dec":
            contador -= 1
        print(contador)
    
    fichero = open("contador.txt","w")
    fichero.write(str(contador))
    fichero.close()
except:
    print("Error: Fichero corrupto")