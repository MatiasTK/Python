import math

class Circulo:
    def __init__(self,radio = 0):
        self.r = radio
        print("Se agrego el radio {} correctamente".format(self.r))
    def area(self):
        a = math.pi * (self.r)**2
        print("El area es:",a)
    def perimetro(self):
        p = 2 * math.pi * self.r
        print("El perimetro es:",p)

radio = int(input("Ingresa el radio del circulo:"))

r = Circulo(radio)
r.area()
r.perimetro()

input("Presiona una tecla para continuar...")
            

        
        