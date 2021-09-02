print("Calculadora de indice de masa corporal")
peso = float(input("Introduce tu peso (en kg): "))
altura = float(input("Introduce tu altura (en m): "))

resultado = round(peso / altura)

print("Indice masa corporal: {0:.2f}".format(resultado))