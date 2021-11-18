from tkinter import *

root = Tk()

# Text es para poder escribir texto -> ya sea en el root o donde quieras
texto = Text(root)
texto.pack()
texto.config(width=30,height=10) # En este caso el widgth y height se basa en caracteres para escribir -> width caracteres de ancho que puede escribir

texto.config(font=("Consolas",12),padx=15,pady=15,selectbackground="red") #Selecbackground es el color de seleccion

root.mainloop()