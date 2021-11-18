""" 1. Crear la clase Persona con los métodos “set_nombre”, “set_edad”, “get_nombre”, “get_edad” y
“print_persona”. Luego crear dos objetos del tipo Persona e imprimirlos.
2. Agregarle a la clase anterior un constructor que reciba nombre y edad.
3. Agregarle a la clase anterior un método “es_mayor_de_edad” que devuelva True o False.
4. Agregarle un método “es_mayor_que” el cual recibe un objeto persona y compara su edad con la
del objeto actual.
5. Agregarle un método estático “get_mayor” que reciba dos objetos Persona y devuelva el de edad
mayor.
6. Agregar un método estático “dump_csv” que reciba el nombre de un archivo, una lista de
personas y genere un archivo CSV separado por comas con los datos de cada persona.
7. Agregar un método estático “load_csv” que reciba el nombre de un archivo y devuelva una lista
de objetos Persona.
8. En linux embebido, es posible manejar el estado de GPIOs escribiendo un caracter “0” o “1” en
un archivo. Realizar un módulo “gpio” con una clase llamada “Gpio” que reciba en su constructor
un número. Agregarle el método “set_state” que reciba un bool. Este método escribirá un caracter
“0” o “1” en un archivo en el path “/tmp/gpio_n.data” siendo “n” el número recibido en el
constructor. Crear un programa para importar el módulo y probarlo.
9. Agregar a la clase anterior el método “get_state” que devuelva un bool según el contenido del
archivo. """

import csv

class Persona:
    
    def __init__(self,nombre="",edad=0):
        self.nombre = nombre
        self.edad = edad
    
    def set_nombre(self,nombre):
        self.nombre = nombre
        
    def get_nombre(self):
        return self.nombre
    
    def set_edad(self,edad):
        self.edad = edad
    
    def get_edad(self):
        return self.edad
    
    def print_persona(self):
        print("Hola! soy",self.nombre,"y tengo",self.edad,"años")
    
    def es_mayor_de_edad(self):
        if(self.edad >= 18):
            return True
        else:
            return False
    
    def get_mayor(self,persona):
        if(self.edad > persona.get_edad()):
            return self
        else:
            return persona
        
    def dump_csv(self,path,personas):
        fp = open(path,"w",encoding="utf-8")
        for i in personas:
            fp.write(i.get_nombre()+";"+str(i.get_edad())+"\n")
        fp.close()
            
    def load_csv(self,path):
        fp = open(path,"r",encoding="utf-8")
        personas = []
        lineas = fp.readlines()
        for linea in lineas:
            lp = linea.split(";")
            p = Persona(lp[0],int(lp[1]))
            personas.append(p)
        fp.close()
        return personas    

Juan = Persona()
Juan.set_nombre("Juan")
Juan.set_edad(17)
if(Juan.es_mayor_de_edad()):
    print("Juan es mayor de edad")
Juan.print_persona()

Mati = Persona()
Mati.set_nombre("Matias")
Mati.set_edad(21)
Mati.print_persona()
if(Mati.es_mayor_de_edad()):
    print("Matias es mayor de edad")


print("El mayor es:",Juan.get_mayor(Mati).get_nombre())

L = []

L.append(Juan)
L.append(Mati)

Mati.dump_csv("personas.csv",L)

L_load = Mati.load_csv("personas.csv")

for i in L_load:
    i.print_persona()

input("Presiona una tecla para continuar...")

