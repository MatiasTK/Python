frutas = {}
frutas["Platano"] = 1.35
frutas["Manzana"] = 0.80
frutas["Pera"] = 0.85
frutas["Naranja"] = 0.70

fb = input("Fruta que desea comprar: ")
kg = int(input("Kg que desea comprar: "))

if fb in frutas:
    print("El precio de",kg,"kg de",fb,"son $",frutas[fb] * kg)
else:
    print("No tenemos esa fruta")