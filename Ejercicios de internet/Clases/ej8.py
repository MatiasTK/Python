class Revertir:
    def __init__(self,c = None):
        self.c = c 
        
    def resultado(self):
        l = self.c.split(" ")
        print(l[-1]," ",end="")
        for x in range(len(l) - 1):
            print(l[x]," ",end="")
        
c = Revertir(input("Ingresa una cadena: "))
c.resultado()
        