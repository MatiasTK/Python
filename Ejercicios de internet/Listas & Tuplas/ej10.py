precios = [50,75,46,22,70,65,8]

menor = precios[0]
mayor = precios[0]

i = 0
while i < len(precios):
    if precios[i] < menor:
        menor = precios[i]
    if precios[i] > mayor:
        mayor = precios[i]
    i += 1

print("Menor:",menor,"Mayor:",mayor)