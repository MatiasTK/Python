divisas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥',"Peso":"ARS"}
buscada = input("Nombre de la divisa a buscar: ")
for i in divisas:
    if i == buscada:
        print(divisas[i])
        break
else:
    print("La divisa no esta")

