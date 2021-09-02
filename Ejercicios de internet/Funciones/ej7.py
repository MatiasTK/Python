def cuadrados(lista):
    lista_cuadrados = []
    for x in lista:
        lista_cuadrados.append(x**2)
    return lista_cuadrados

lista = [1,2,3,4,5]

print(cuadrados(lista))
