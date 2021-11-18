from tkinter import * 

root = Tk()
root.title("Entrys!")

# Grid es cuadricula nos permite alinear mejor las cosas
# Sticky para alinear el texto
# Padding -> Margen

label = Label(root,text="Nombre muy largo")
label.grid(row=0,column=0,sticky="e",padx=5,pady=5) #Sticky formato brujula

entry = Entry(root) 
entry.grid(row=0,column=1,padx=5,pady=5)
entry.config(justify="right",state="disabled") #Es de donde empieza a aparecer el texto en el entry, state desactiva algo EN ESTE CASO el entry lo deja sin poder escribir

label2 = Label(root,text="Contraseña")
label2.grid(row=1,column=0,sticky="e",padx=5,pady=5)

entry2 = Entry(root) 
entry2.grid(row=1,column=1,padx=5,pady=5)
entry2.config(justify="center",show="*") #El show es para que se muestre eso para que no se vea


root.mainloop()