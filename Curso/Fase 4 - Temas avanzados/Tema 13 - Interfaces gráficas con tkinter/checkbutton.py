from tkinter import *

def seleccionar():
    cadena = ""
    if(leche.get() == True):
        cadena += "Con leche"
    else:
        cadena += "Sin leche"
    
    if(azucar.get() == True):
        cadena += " y con azucar"
    else:
        cadena += " y sin azucar"
    
    monitor.config(text=cadena)

root = Tk()
root.title("Cafeteria")
root.config(bd=15)

leche = BooleanVar()
azucar = BooleanVar()

imagen = PhotoImage(file="imagen.gif")
Label(root,image=imagen).pack(side="left")

frame = Frame(root)
frame.pack(side="left")

Label(frame,text="¿Como quieres el cafe?").pack(anchor="w")
Checkbutton(frame,text="Con leche",variable=leche,onvalue=True,offvalue=False,command=seleccionar).pack(anchor="w")
Checkbutton(frame,text="Con azucar",variable=azucar,onvalue=True,offvalue=False,command=seleccionar).pack(anchor="w")

monitor = Label(frame)
monitor.pack(anchor="center")

root.mainloop()