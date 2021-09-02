n = int(input("Numero: "))
cont = 1

for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print("")