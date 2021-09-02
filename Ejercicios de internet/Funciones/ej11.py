def frecuencia_palabra(parrafo):
    dic = {}
    for palabra in parrafo:
        if palabra in dic:
            dic[palabra] = dic[palabra] + 1
        else:
            dic[palabra] = 1
    return dic

def mas_frecuente(dic):

    mayor = 0
    word = 0

    for palabra in dic:
        if dic[palabra] > mayor:
            mayor = dic[palabra]
            word = palabra
    
    return word,mayor
    



parrafo = input("Ingresa un parrafo: ")

dic = frecuencia_palabra(parrafo)

palabra,frecuencia = mas_frecuente(dic)

print(dic)

print("La palabra mas repetida es",palabra,"con",frecuencia,"repeticiones")