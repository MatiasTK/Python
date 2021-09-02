def firstDuplicate(a):
    conjunto = set()
    for x in a:
        if x in conjunto:
            return x
        else:
            conjunto.add(x)
    return -1
    

a = [2, 1, 3, 5, 3, 2]
print(firstDuplicate(a))