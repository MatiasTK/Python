""" Modulos: se pueden usar funciones o clases de otro archivo python Ej:
import saludos
saludos.saludar()
from saludos import saludar
saludar()"""

#SI NO ESTA EN EL DIRECTORIO
import sys
sys.path.insert(1,"C:\\Users\\Mati\\Desktop\\Programacion\\Python\\Curso\\Fase 4 - Temas avanzados\\Tema 11 - Módulos\\Lección 01 - Modulos")
print(sys.path)

from saludos import Saludo

Saludo()

#Es mas facil con paquetes -> Siguiente clase