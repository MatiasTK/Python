nombre = input("Nombre del producto: ")
precio = float(input("Precio del producto: "))
unidades = int(input("Unidades del producto: "))

print("{nombre}: {precio:6.2f}$ x {unidades:3d} = {total:8.2f}".format(nombre = nombre,precio = precio,unidades = unidades,total = unidades * precio))