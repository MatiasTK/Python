n = int(input("Elegi un numero para mostrar su tabla: "))

file = open("tabla-{}.txt".format(str(n)),"w")

for i in range(11):
    file.write("{} * {} => {}".format(n,i,n*i))
    if i != 10:
        file.write("\n")
    
file.close()
