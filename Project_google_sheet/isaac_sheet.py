import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
import colorama
import time
import sys
from os import system

system("title " "Isaac Daily Summary")

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name(resource_path("creds.json"), scope)

client = gspread.authorize(creds)

sheet = client.open("Isaac_daily").sheet1
last_updated_sheet = client.open("Isaac_daily").lastUpdateTime

data = sheet.get_all_records()

colorama.init()

RESET = '\033[0m'
RED = '\033[31m'
GREEN = '\033[32m'
MAGENTA = '\033[35m'
GOLD = '\033[33m'
YELLOW = '\033[93m'
LIGHT_BLUE = '\033[94m'
CYAN = '\033[36m'
LIGHT_RED = '\033[91m'
ORANGE = '\033[33m'
BLUE = '\033[34m'

BIENVENIDA = ''' _____                        _____        _ _         _____             
|_   _|                      |  __ \      (_) |       |  __ \            
  | |  ___  __ _  __ _  ___  | |  | | __ _ _| |_   _  | |__) |   _ _ __  
  | | / __|/ _` |/ _` |/ __| | |  | |/ _` | | | | | | |  _  / | | | '_ \ 
 _| |_\__ \ (_| | (_| | (__  | |__| | (_| | | | |_| | | | \ \ |_| | | | |
|_____|___/\__,_|\__,_|\___| |_____/ \__,_|_|_|\__, | |_|  \_\__,_|_| |_|
                                                __/ |                    
                                               |___/                     
  _____                                            
 / ____|                                           
| (___  _   _ _ __ ___  _ __ ___   __ _ _ __ _   _ 
 \___ \| | | | '_ ` _ \| '_ ` _ \ / _` | '__| | | |
 ____) | |_| | | | | | | | | | | | (_| | |  | |_| |
|_____/ \__,_|_| |_| |_|_| |_| |_|\__,_|_|   \__, |
                                              __/ |
                                             |___/ 
'''
DESPEDIDA = '''
    __  ___      __  _ 
   /  |/  /___ _/ /_(_)
  / /|_/ / __ `/ __/ / 
 / /  / / /_/ / /_/ /  
/_/  /_/\__,_/\__/_/   
                       '''

while(True):
    print(GREEN + BIENVENIDA + RESET)
    print("Ultima actualizacion:", last_updated_sheet[0:10],"\n")
    piso = input("¿En que piso estás?\nNota: los pisos deben escribirse como B1,B2,C1,C2,D1,D2,W1,W2,C/S,C/D.\nIngresa el piso: ")
    
    linea = None
    if(piso):
        for i in data:
            if i['Piso'] == piso:
                linea = i;

    if(linea == None or not piso):
        print("\nSos un salchicha no pusiste un piso valido")
    else:
        Color = RESET
        for sala in linea:
            if(linea[sala] and not sala == "Piso"):
                if(sala == "Dorada"):
                    Color = GOLD
                elif(sala == "Tienda"):
                    Color = YELLOW
                elif(sala == "Secreta"):
                    Color = LIGHT_BLUE
                elif(sala == "Curse"):
                    Color = RED
                elif(sala == "Angeles"):
                    Color = CYAN
                elif(sala == "Diablo"):
                    Color = LIGHT_RED
                elif(sala == "Challenge"):
                    Color = MAGENTA
                elif(sala == "Extra"):
                    Color = BLUE
                print(Color + sala,"->",linea[sala] + RESET)
                time.sleep(1)
    seguir = input("\n¿Deseas consultar otro piso? (S/N): ")
    system("cls")
    if(seguir == "N" or seguir == "n"):
        break
print("Gracias por usar el programa")
print("Hecho por:")
print(LIGHT_BLUE + DESPEDIDA + RESET)

input("Presiona enter para salir")
