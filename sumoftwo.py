
def sumOfTwo(a,b,v):
    hash = {}
    hash = set()
    
    for i in a:
        buscado = v - i
        hash.add(buscado)
    
    for j in b:
        if(j in hash):
            return True
    
    return False

def sumOfTwo2(a,b,v):
    for i in range(len(a)):
        for j in range(len(b)):
            if(a[i] + b[j] == v):
                return True
    return False

a = [1, 2, 3, 4, 5]
b = [6, 7, 8, 9, 10]
v = 0
print(sumOfTwo(a,b,v))
