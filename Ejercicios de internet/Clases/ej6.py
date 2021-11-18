class Suma:
    def __init__(self,lista = []):
        self.l = lista
        
    def encontrar(self):
        nl = []
        
        x = 0
        y = x + 1
        z = y + 1
        while x < len(self.l) - 1:
            if self.l[x] + self.l[y] + self.l[z] == 0:
                nl.append([x,y,z])
            else:
                if z < len(self.l) - 1 :
                    z += 1
                elif y < len(self.l) - 1 :
                    y += 1
            x += 1

l = [-25, -10, -7, -3, 2, 4, 8, 10]                        
entrada = Suma(l)
entrada.encontrar()
                        
                        
# No se como se hace exactamente, hay una forma en internet pero es usando una biblioteca 