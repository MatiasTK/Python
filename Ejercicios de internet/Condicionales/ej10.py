vegano = input("Queres una pizza vegana? (S/N): ")
ingredientes = ["mozzarella","tomate"]

if vegano == 'S' or vegano == 's' or vegano == 'Si' or vegano == 'si':
    respuesta = input("Ingredientes disponibles:\n1)Pimiento\n2)Tofu\n")
    if respuesta == 1:
        ingredientes.append("pimiento")
    else:
        ingredientes.append("tofu")
    print("La pizza elegida es vegana y contiene:",",".join(ingredientes))
else:
    respuesta = input("Ingredientes disponibles:\n1)Peperoni\n2)Jamon y Salmon\n")
    if respuesta == 1:
        ingredientes.append("peperoni")
    else:
        ingredientes.append("jamon y salmon")
    print("La pizza elegida no es vegana y contiene:",",".join(ingredientes))
