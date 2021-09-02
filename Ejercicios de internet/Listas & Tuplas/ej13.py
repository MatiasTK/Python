lista = [int(x) for x in input("Introduci numeros separados por ',': ").split(",")]

media = sum(lista) / len(lista)
desviacion = []
x = 0
while x < len(lista):
    calc = lista[x] - media
    desviacion.append(calc)
    x += 1

print("Media:",media)
print("Desviacion:",desviacion)

