class Clase:
    def get_string(self,cadena):
        self.c = cadena
    def print_string(self):
        print((self.c).upper())
        
s = Clase()
s.get_string(input("Ingresa una cadena: "))
s.print_string()
