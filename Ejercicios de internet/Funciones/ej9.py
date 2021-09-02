def maximo_comun_divisor(num1,num2):
    resto = 0
    while num2 > 0:
        resto = num2
        num2 = num1 % num2
        num1 = resto
    return num1
    
def minimo_comun_multiplo(num1,num2,mcd):
    return (num1*num2)/mcd


num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))

mcd = maximo_comun_divisor(num1,num2)
mcm = minimo_comun_multiplo(num1,num2,mcd)

print("El maximo comun divisor es:",mcd)
print("El minimo comun multiplo es:",mcm)