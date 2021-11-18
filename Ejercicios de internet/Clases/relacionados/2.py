# https://plataforma.josedomingo.org/pledin/cursos/programacion_python3/curso/u42/

class Cuenta:
    def __init__(self,titular="",cantidad=0.0):
        self.titular = titular
        self.cantidad = cantidad
    
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
                
                
cuenta1 = Cuenta("José",100)
cuenta1.ingresar(50.3)
cuenta1.retirar(20.5)
cuenta1.mostrar()
cuenta1.retirar(150)
cuenta1.retirar(129.8)
cuenta1.mostrar()
cuenta1.retirar(10)