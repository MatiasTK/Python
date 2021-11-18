from tkinter import *

root = Tk()  #creamos la raiz

root.title("Hola mundo!")
root.resizable(1,1) #El 0,0 es para que no pueda ser redimensionable la ventana -> el 1,1 es por defecto -> el 0,1 es agrandar vertical pero no horizontal
root.iconbitmap("hola.ico") #Tiene que ser en formato ico

frame = Frame(root,width=480,height=320)
#frame.pack(side="bottom",anchor="w") #Se enpaqueta el frame -> side es el lado donde va a estar el frame -> anchor es la orientacion derecha,izquierda.., e es de east
frame.pack(fill="both",expand=1) # la rellena horizontamlmente en x o vertial en y, Expand 
# frame.config(width=480,height=320)
frame.config(cursor="pirate") #Forma del cursor
frame.config(bg="lightblue") #Color de fondo
frame.config(bd=25) 
frame.config(relief="sunken") #Tipo de borde


root.config(cursor="arrow") #Forma del cursor
root.config(bg="blue") #Color de fondo
root.config(bd=15) 
root.config(relief="ridge") #Tipo de borde

root.mainloop() #loop principal -> Es como cuando hacia menus en while -> Es el ultimo paso