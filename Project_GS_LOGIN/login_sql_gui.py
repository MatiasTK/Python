import gspread
from oauth2client.service_account import ServiceAccountCredentials
from tkinter import *

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("Login_SQL").sheet1

data = sheet.get_all_records()


root = Tk()
root.title("Sistema")

frame = Frame(root)
frame.pack()

def main():
    Button(frame, text="Login", command=Ingresar).pack(side="left",padx=5,pady=5)

def sql(name,passw):
    for i in data:
        if i["Nombre"] == name and i["Contraseña"] == passw:
            print("Bienvenido")
            break
        else:
            print("Usuario o contraseña incorrectos")

def Ingresar():
    frame.destroy()
    frame_ingresar = Frame(root)
    frame_ingresar.pack()
    
    nombre = Label(frame_ingresar, text="Nombre: ")
    nombre.grid(row=0,column=0,padx=5,pady=5)
    entry_n = Entry(frame_ingresar)
    entry_n.grid(row=0,column=1,padx=5,pady=5)
    entry_n.config(width=30)
    name = entry_n.bind("<KeyRelease>")
    
    contrasenia = Label(frame_ingresar, text="Contraseña: ")
    contrasenia.grid(row=1,column=0,padx=5,pady=5)
    entry_c = Entry(frame_ingresar)
    entry_c.grid(row=1,column=1,padx=5,pady=5)
    entry_c.config(width=30)
    passw = entry_c.bind("<KeyRelease>")
    
    Button(frame_ingresar, text="Ingresar", command=sql(name,passw)).grid(row=2,column=1,padx=5,pady=5)


while True:
    main()
    break

root.mainloop()
