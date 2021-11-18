from os import system
import random
import colorama
system("title " "Isaac Run Generator")
colorama.init()

RED = '\033[31m' 
BLUE = '\033[34m'
RESET = '\033[0m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
PURPLE = '\033[35m'
AQUAMARINE = '\033[36m'

Bienvenida = GREEN +'''
                 _____                        _____             
                |_   _|                      |  __ \            
                  | |  ___  __ _  __ _  ___  | |__) |   _ _ __  
                  | | / __|/ _` |/ _` |/ __| |  _  / | | | '_ \ 
                 _| |_\__ \ (_| | (_| | (__  | | \ \ |_| | | | |
                |_____|___/\__,_|\__,_|\___| |_|  \_\__,_|_| |_|
                                                                
                                                                
                  _____                           _             
                 / ____|                         | |            
                | |  __  ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
                | | |_ |/ _ \ '_ \ / _ \ '__/ _` | __/ _ \| '__|
                | |__| |  __/ | | |  __/ | | (_| | || (_) | |   
                 \_____|\___|_| |_|\___|_|  \__,_|\__\___/|_|   
                                                                
                                                                
''' + RESET

boss = ["Satán","Isaac","Lamb","Blue Baby","Mega Satán","Mother","True ending","Greedier"]
optional_boss = ["Boss Rush","Hush","Delirium"]
pj = ["Isaac","Maggy","Cain","Judas","Blue Baby","Eve","Samson","Azazel","Lazarus","Eden","Lost","Lilith","Keeper","Apollyon","Forgotten","Bethany","Jacob y Essau"]
tainted_pj = ["Tainted Isaac","Tainted Maggy","Tainted Cain","Tainted Judas","Tainted Blue Baby","Tainted Eve","Tainted Samson","Tainted Azazel","Tainted Lazarus","Tainted Eden","Tainted Lost","Tainted Lilith","Tainted Keeper","Tainted Apollyon","Tainted Forgotten","Tainted Bethany","Tainted Jacob y Essau"]
optinal_path = ["Angeles","Demonios"]

def random_run_gen(personaje,path,optional,puertas):
    personaje = AQUAMARINE + random.choice(personaje+tainted_pj) + RESET
    path = RED + random.choice(path) + RESET
    if not(path == RED + "Greedier" + RESET):
        optional = YELLOW + random.choice(optional) + RESET
    else:
        optional = None
    if(path == RED + "Mega Satán" + RESET):
        puertas = "Angeles"
    else:
        puertas = PURPLE + random.choice(optinal_path) + RESET
    
    if(path == RED + "True ending" + RESET or path == RED + "Mother" + RESET):
        optional = "Boss Rush"

    return personaje,path,optional,puertas



def main():    
    while(True):
        print(Bienvenida)
        personaje,path,optional,puertas = random_run_gen(pj,boss,optional_boss,optinal_path)
        adicional = input("¿Quieres una ruta adicional? [S/N]: ")
        if((adicional == "S" or adicional == "s") and not optional == None):
            print("Tenes que hacer una run con {} hasta {}".format(personaje,path))
            print("Como adicional tambien podes ir a {}".format(optional))
            if(optional == YELLOW + "Delirium" + RESET):
                print("Si no encontras el portal no pasa nada!")
            print("Tenes que seguir las puertas de los {}".format(puertas))
        else:
            print("Tenes que hacer una run con {} hasta {}".format(personaje,path))
        ask = input("¿Quieres que se genere otra run? [S/N]: ")
        if(ask == "N" or ask == "n"):
            break
        system("cls")
    input("Presiona enter para salir")
    

main()