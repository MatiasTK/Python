cesta = {}

aniadir = input("Introduce el articulo (articulo:precio): ")
total = 0

while not(aniadir == "Salir" or aniadir == "salir"):
    aniadir = aniadir.split(":")
    cesta[aniadir[0]] = aniadir[1]
    total += int(aniadir[1])
    aniadir = input("Introduce el articulo (articulo:precio): ")
    

print(cesta)
print("Precio total:",total)