import pickle

""" class Personaje:
    personajes = {}
    def __init__(self):
        pass
    
class Gestor(Personaje):
    try:
        fichero = open("personajes.pckl","rb")
        contenedor = pickle.load(fichero)
        fichero.close()
        print(contenedor)
    except:
        fichero = open("personajes.pckl","wb")
        fichero.close()
    def __init__(self) -> None:
        pass
    def crear(self):
        nombre = input("Ingresa la clase: ")
        for i in self.personajes:
            if i == nombre:
                print("Ya existe ese personaje")
                return
        else:
            dic = {}
            dic["vida"] = int(input("Ingresa la vida: "))
            dic["ataque"] = int(input("ingresa el ataque: ")) 
            dic["defensa"] = int(input("Ingresa la defensa: "))
            dic["alcance"] = int(input("Ingresa el alcance: "))
            self.personajes[nombre] = dic
    def mostrar(self):
        for i,c in enumerate(self.personajes):
            print("==================================")
            print("Nombre: {} || Estadisticas: {}".format(c, self.personajes[c]))
            print("==================================")
    def borrar(self):
        choice = input("¿A quien queres borrar?\n")
        for i in self.personajes:
            if i == choice:
                del(self.personajes[i])
                return
        else:
            print("No se pudo encontrar ese personaje")
    def __del__(self):
        fichero = open("personajes.pckl","wb+")
        pickle.dump(self.personajes,fichero)
        fichero.close()
        
            
        
 
while(True):
    task = int(input("¿Que queres hacer?\n1)Crear personaje\n2)Mostrar personajes\n3)Borrar personaje\n4)Salir\nEleccion: "))
    if task == 1:
        Gestor().crear()
    elif task == 2:
        Gestor().mostrar() 
    elif task == 3:
        Gestor().borrar()
    else:
        break
        
         """
   
   
# Si bien el codigo de arriba funciona creo que no es lo pedido, forma del profe:

class Personaje:
    def __init__(self,nombre,vida,ataque,defensa,alcance):
        self.nombre = nombre
        self.vida = vida
        self.ataque = ataque
        self.defensa = defensa
        self.alcance = alcance
    def __str__(self):
        return "{} => {} vida, {} ataque, {} defensa, {} alcance".format(self.nombre,self.vida,self.ataque,self.defensa,self.alcance)

class Gestor:
    personajes = []
    
    def __init__(self):
        self.cargar()
    
    def agregar(self,p):
        for ptemp in self.personajes:
            if ptemp.nombre == p.nombre:
                return
        
        self.personajes.append(p)
        self.guardar()
    
    def mostrar(self):
        if len(self.personajes) == 0:
            print("El gestor esta vacio")
            return
        for p in self.personajes:
            print(p)
    
    def borrar(self,p):
        for ptemp in self.personajes:
            if ptemp.nombre == p:
                self.personajes.remove(ptemp)
                self.guardar()
                print("\nPersonaje {} Borrado".format(p))
                return 
    
    def cargar(self):
        fichero = open("personajes.pckl","ab+")
        fichero.seek(0)
        try:
            self.personajes = pickle.load(fichero)
        except:
            # print("El fichero esta vacio")
            pass
        finally:
            fichero.close()
            print("Se han cargado {} personajes".format(len(self.personajes)))
    
    def guardar(self):
        fichero = open("personajes.pckl","wb")
        pickle.dump(self.personajes,fichero)
        fichero.close()
        
g = Gestor()
#g.mostrar()

#g.agregar(Personaje("Caballero",4,2,4,2))
#g.agregar(Personaje("Guerrero",2,4,2,4))
#g.agregar(Personaje("Arquero",2,4,1,8))
#g.mostrar()

g.borrar("Arquero")
g.borrar("Caballero")
g.mostrar()