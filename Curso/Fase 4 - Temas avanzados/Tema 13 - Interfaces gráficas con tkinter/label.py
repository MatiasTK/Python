from tkinter import *

root = Tk()

# Variables dinamicas
texto = StringVar()
texto.set("Un nuevo texto")

root.title("Labels!")

Label(root,text="¡Hola mundo!").pack(anchor="nw")
label = Label(root,text="¡Otra etiqueta!")
label.pack(anchor="center")
Label(root,text="¡Ultima etiqueta!").pack(anchor="se")

label.config(bg="Green",fg="blue",font=("Verdana",24)) # Fg -> Foreground -> color superior(Color letras), Font("Tipografia",tamaño letra)
label.config(textvariable=texto)

root.mainloop()