print("Bienvenido a la calculadora de intereses!")
dinero = int(input("Cantidad de dinero a invertir: "))
interes = int(input("Interes anual: "))
anios = int(input("Cantidad de años que desea invertir: "))

capital = ((dinero * (interes + 100)) / 100) * anios
print("Capital obtenido:",capital)