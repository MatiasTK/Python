# https://plataforma.josedomingo.org/pledin/cursos/programacion_python3/curso/u42/

class Cuenta:
    def __init__(self,titular="",cantidad=0.0,edad=0):
        self.titular = titular
        self.cantidad = cantidad
        self.edad = edad
    
    def titular_set(self,titular):
        if(type(titular) == str):
            self.titular = titular
        else:
            print("El titular es un caracter invalido")
    def titular_get(self):
        return self.titular
    
    def ingresar(self,cantidad):
        if(type(cantidad) == float or type(cantidad) == int):
            self.cantidad += cantidad
        else:
            print("La cantidad es un caracter invalido")
    
    def retirar(self,cantidad):
        if(type(cantidad) == float or type(cantidad) == int):
            if(self.cantidad <= 0):
                print("No se puede retirar, fondos vacios")
            elif(self.cantidad < cantidad):
                print("No se puede retirar, fondos insuficientes")
            else:
                self.cantidad -= cantidad
        else:
            print("La cantidad es un caracter invalido")

    def mostrar(self):
        print("Titular:",self.titular,"Fondos: {} $".format(self.cantidad))

class CuentaJoven(Cuenta):
    def __init__(self,titular="",cantidad=0.0,edad=0,bonificacion=0):
        super().__init__(titular,cantidad,edad)
        self.bonificacion = bonificacion
        
    def bonificacion_set(self,bonificacion):
        if(type(bonificacion) == int):
            self.bonificacion = bonificacion
        else:
            print("La bonificacion es un caracter invalido")
    def bonificacion_get(self):
        return self.bonificacion
    
    def es_titular_valido(self):
        if(self.edad >= 18 and self.edad < 25):
            return True
        else:
            return False
    
    def mostrar(self):
        return super().mostrar() + "Bonificacion: {} $".format(self.bonificacion)
    
    def retirar(self, cantidad):
        if(self.es_titular_valido()):
            return super().retirar(cantidad)
        else:
            print("No se puede retirar, titular no valido")
    
    
