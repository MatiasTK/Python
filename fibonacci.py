from matplotlib import pyplot as plt 
lista = []

num1 = 0
num2 = 1
print(num1)
print(num2)
lista.append(num1)
lista.append(num2)
for x in range(0,100):
  r = num1 + num2
  num1 = num2
  num2 = r
  lista.append(r)


plt.plot(lista,lista)
plt.show()