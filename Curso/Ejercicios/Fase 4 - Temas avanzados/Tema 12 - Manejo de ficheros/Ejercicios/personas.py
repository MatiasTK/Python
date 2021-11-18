fichero = open("personas.txt","r",encoding="utf8") #El UTF PARA Q SE IMPRIMA BIEN
personas = fichero.readlines()
fichero.close()

lf = []
for i in range(len(personas)):
    lf.append(personas[i].split(";"))
    
for i in range(len(lf)):
    print("ID: {}, Nombre: {}, Apellido: {}, Nacimiento: {}".format(lf[i][0],lf[i][1],lf[i][2],lf[i][3]))

input("\nPresiona una tecla para continuar...")

""" #Forma del profe
from io import open

fichero = open("personas.txt","r",encoding="utf8")
lineas = fichero.readlines()
fichero.close()

personas = []

for linea in lineas:
    campos = linea.replace("\n","").split(";")
    persona = {"id":campos[0],"nombre":campos[1],"apellido":campos[2],"nacimiento":campos[3]}
    personas.append(persona)

for p in personas:
    print("(id={}) {} {} => {}".format(p["id"],p["nombre"],p["apellido"],p["nacimiento"]))
 """