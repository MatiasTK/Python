# https://plataforma.josedomingo.org/pledin/cursos/programacion_python3/curso/u42/

class Persona:
    def __init__(self, nombre="", edad=0,DNI=0):
        self.nombre = nombre
        self.edad = edad
        self.dni = DNI
        
    def nombre_set(self, nombre):
        if(type(nombre) == str):
            self.nombre = nombre
        else:
            print("Error: No se recibio un nombre valido")
    def nombre_get(self):
        return self.nombre

    def edad_set(self, edad):
        if(type(edad) == int):
            self.edad = edad
        else:
            print("Error: No se recibio una edad valida")
    def edad_get(self):
        return self.edad
    
    def dni_set(self, dni):
        if(type(dni) == int):
            self.dni = dni
        else:
            print("Error: No se recibio un DNI valido")
    def dni_get(self):
        return self.dni
    
    def mostrar(self):
        print("Nombre: {}, Edad: {}, DNI: {} \n".format(self.nombre, self.edad, self.dni))
        
    def esMayorDeEdad(self):
        if(self.edad >= 18):
            return True
        else:
            return False
        

Mati = Persona()
Mati.nombre_set("Matias Vallejos")
Mati.edad_set(18)
Mati.dni_set(43057720)

Mati.mostrar()

if(Mati.esMayorDeEdad()):
    print("Es mayor de edad")
else:
    print("No es mayor de edad")