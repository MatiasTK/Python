dic = {}
palabras = input("Introduci una traduccion con formato palabra:traduccion,: ")
frase = input("Introduci una frase a traducir: ")

for i in palabras.split(","):
    palabra,traduccion = i.split(":")
    dic[palabra] = traduccion

for i in frase.split(" "):
    if i in dic:
        print(dic[i],"",end="")
    else:
        print(i,"",end="")
