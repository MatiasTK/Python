import gspread
from oauth2client.service_account import ServiceAccountCredentials
import getpass
from os import system
import base64

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("Login_SQL").sheet1

data = sheet.get_all_records()

while(True):
    print("\nBienvenido al sistema")
    print("1. Ingresar")
    print("2. Registrarse")
    print("3. Salir")
    opcion = input("Ingrese una opcion: ")
    accedio = False
    ya_registro = False
    
    if(opcion == "1"):
        usuario = input("Ingrese su usuario: ")
        contrasenia = getpass.getpass("Ingrese su contraseña: ")
        contrasenia_encoded = base64.b64encode(contrasenia.encode("utf-8"))
        for linea in data:
            if(linea["Usuario"] == usuario or linea["Mail"] == usuario):
                if(str(linea["Contrasenia"]) == str(contrasenia_encoded)):
                    print("Bienvenido", linea["Nombre"])
                    accedio = True
                    break
        if(accedio == False):
            print("Usuario o contraseña incorrectos")
    elif(opcion == "2"):
        nombre = input("Ingrese su nombre: ")
        mail = input("Ingrese su mail: ")
        usuario = input("Ingrese su usuario: ")
        contrasenia = getpass.getpass("Ingrese su contraseña: ")
        encoded = base64.b64encode(contrasenia.encode("utf-8"))
        for linea in data:
            if(linea["Usuario"] == usuario or linea["Mail"] == mail):
                print("El usuario o el mail ya existen")
                break
        else:
            sheet.insert_row([nombre,usuario,str(encoded),mail], 2)
            print("Usuario registrado")
            input("Presione enter para continuar")
            data = sheet.get_all_records()
            system("cls")
    elif(opcion == "3"):
        break
    if(accedio == True):
        break
print("Gracias por utilizar el programa")
input("Presione enter para salir")