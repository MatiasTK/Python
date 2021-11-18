#Modulo!
from typing import Type

def suma(num1,num2):
    try:
        num1 + num2
    except TypeError:
        return "Error: Tipo de dato no valido"
    return num1 + num2

def resta(num1,num2):
    try:
        num1 - num2
    except TypeError:
        return "Error: Tipo de dato no valido"
    return num1 - num2

def producto(num1,num2):
    try:
        if type(num1) == str or type(num2) == str:
            raise TypeError
        num1 * num2
    except TypeError:
        return "Error: Tipo de dato no valido"
    return num1 * num2

def division(num1,num2,reverse=False):
    try:
        num1 / num2
    except TypeError:
        return "Error: Tipo de dato no valido"
    except ZeroDivisionError:
        return "Error: No es posible dividir entre cero"
    if reverse == False:
        return num1 / num2
    else:
        return num2 / num1
