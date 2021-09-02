entero = int(input("Ingresa un entero: "))

for i in range(1,entero + 1,2):
    for j in range(i,0,-2):
        print(j,end=" ")
    print("")