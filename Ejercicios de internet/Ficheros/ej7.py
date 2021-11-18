def dictionary(path):
    file = open(path,"r",encoding="UTF-8")
    lines = file.readlines()
    file.close()
    keys = lines[0]
    keys = keys[:-1].split(";")
    
    dic = {}
    
    for i in keys:
        dic[i] = []
        
    for i in lines[1:]:
        i = i[:-1].split(";")
        for j in range(len(dic)):
            dic[keys[j]].append(i[j])
    
    return dic

def operations(dic):
    r = 0
    for i in dic["Mínimo"]:
        r += float(i.replace(",","."))
    minimo = r / len(dic["Mínimo"])
    r = 0
    for i in dic["Máximo"]:
        r += float(i.replace(",","."))
    maximo = r / len(dic["Máximo"])
    media = (maximo + minimo) / 2
    print("La media es: {:.2}".format(media))
    
    

path = "cotizacion.csv"
dic = dictionary(path)
final = operations(dic)
