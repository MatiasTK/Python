def calificaciones(path):
    fichero = open(path,"r",encoding="UTF-8")
    lineas = fichero.readlines()
    fichero.close()
    
    calificaciones = []
    
    clave = lineas[0][:-1].split(";")
    
    for i in lineas[1:]:
        valores = i[:-1].split(";") #Para que no imprima el \n
        alumno = {}
        for j in range(len(valores)):
            alumno[clave[j]] = valores[j]
        calificaciones.append(alumno)
    
    return calificaciones

def nota_final(calificaciones):
    for i in range(len(calificaciones)):
        parcial = ((float(calificaciones[i]["Parcial1"].replace(",",".")) + float(calificaciones[i]["Parcial2"].replace(",","."))) * 30) / 100
        try:
            practicas = (float(calificaciones[i]["Practicas"].replace(",",".")) * 40) / 100
        except:
            practicas = 0
        final = "{:.3}".format(parcial+practicas)
        calificaciones[i]["Final"] = final
    return calificaciones
        
def aprobados(calificaciones):
    aprobados = []
    desaprobados = []
    for i in range(len(calificaciones)):
        asistencia = int(calificaciones[i]["Asistencia"].replace("%",""))
        parciales = (float(calificaciones[i]["Parcial1"].replace(",",".")) + float(calificaciones[i]["Parcial2"].replace(",","."))) 
        try:
            practicas = float(calificaciones[i]["Practicas"].replace(",","."))
        except:
            practicas = 0
        no_final = (parciales + practicas) / 3
        final = float(calificaciones[i]["Final"])
        if asistencia >= 75 and no_final >= 4 and final >= 5:
            aprobados.append(calificaciones[i])
        else:
            desaprobados.append(calificaciones[i])
            
    return aprobados,desaprobados

path = "calificaciones.csv"
dic = calificaciones(path)
dic = nota_final(dic)

aprobados,desaprobados = aprobados(dic)

print(aprobados)

    
    
    
    
