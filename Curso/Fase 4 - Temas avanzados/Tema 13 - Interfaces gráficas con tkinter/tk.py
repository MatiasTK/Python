from tkinter import *

root = Tk()  #creamos la raiz

root.title("Hola mundo!")
root.resizable(1,1) #El 0,0 es para que no pueda ser redimensionable la ventana -> el 1,1 es por defecto -> el 0,1 es agrandar vertical pero no horizontal
root.iconbitmap("hola.ico") #Tiene que ser en formato ico


root.mainloop() #loop principal -> Es como cuando hacia menus en while -> Es el ultimo paso