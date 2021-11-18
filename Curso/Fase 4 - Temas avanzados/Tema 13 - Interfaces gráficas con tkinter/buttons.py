from tkinter import *

def crear_label():
    Label(root,text="Label creada dinamicamente").pack()
    
def sumar():
    r.set(float(n1.get()) + float(n2.get()))
    borrar()
    
def resta():
    r.set(float(n1.get()) - float(n2.get()))
    borrar()
    
def producto():
    r.set(float(n1.get()) * float(n2.get()))
    borrar()

def division():
    r.set((float(n1.get())) / float(n2.get()))
    borrar()
    
def borrar():
    n1.set("")
    n2.set("")


root = Tk()
root.title("Calculadora")
root.config(bd=15)

n1 = StringVar()
n2 = StringVar()
r = StringVar()

#Button(root,text="Clickeame",command=crear_label).pack()
Label(root,text="Numero 1").pack()
Entry(root,justify="center",textvariable=n1).pack() # Primer numero
Label(root,text="Numero 2").pack()
Entry(root,justify="center",textvariable=n2).pack() # Segundo numero
Label(root,text="Resultado").pack()
Entry(root,justify="center",textvariable=r,state="disabled").pack() # Resultado
Label(root,text="").pack()
Button(root,text="Sumar",command=sumar).pack(side="left",padx=5,pady=5)
Button(root,text="Resta",command=resta).pack(side="left",padx=5,pady=5)
Button(root,text="Producto",command=producto).pack(side="left",padx=5,pady=5)
Button(root,text="Division",command=division).pack(side="left",padx=5,pady=5)


root.mainloop()