def rotateImage(a):
   return list(zip(*a[::-1]))
    
a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

print(rotateImage(a))
            
# Algo como -> l = [[a[2][0],a[1][0],a[0][0]], [a[2][1],a[1][1],a[0][1]]]

print("-------------------------\nExplicacion: a[::-1] te pone la inversa de a, quedaria algo como: ")

b = a[::-1]

for x in range(len(b)):
    print(b[x])


print("El * en la B significa que va a modificar la lista original y no va a hacer una copia, zip() toma el primer argumento de cada lista y lo hace una tupla o lista")

b = list(zip(*b))

for x in range(len(b)):
    print(b[x])
