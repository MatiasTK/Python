#Creo abecedario
abecedario = "abcdefghijklmnñopqrstuvwxyz"
abc = list(abecedario)

i = 0
while i < len(abc):
    if i % 3 == 0 and i != 0:
        abc.remove(abc[i])
    i += 1

print(abc)
