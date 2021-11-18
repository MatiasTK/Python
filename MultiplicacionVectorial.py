def multiplicacion_vectorial(A,B):
    rx = A[1]*B[2] - A[2]*B[1]
    ry = A[0]*B[2] - A[2]*B[0]
    rz = A[0]*B[1] - A[1]*B[0]
    
    R.append(rx)
    R.append(ry)
    R.append(rz)

def comprobar_vector(A,B):
    prueba = True
    if not(len(A) == 3 and len(B) == 3):
        print("Error: los vectores no tienen 3 componentes")
        prueba = False
    for i in A:
        if not((i.replace('.','',1)).isdigit()):
            print("Error: El vector A contiene caracteres que no son numeros")
            prueba = False
    for j in B:
        if not((j.replace('.','',1)).isdigit()):
            print("Error: El vector B contiene caracteres que no son numeros")
            prueba = False
    return prueba

R = []

end = False
while(not end):
    A = (input("Ingrese los valores de A separados por una coma: ").split(","))

    B = (input("Ingrese los valores de B separados por una coma: ").split(","))
    
    if(comprobar_vector(A,B)):
        A = [float(i) for i in A]
        B = [float(j) for j in B]

        multiplicacion_vectorial(A,B)
        print("El resultado de la multiplicacion vectorial es: ({} i | {} j | {} k) \n".format(R[0],R[1],R[2]))
    ans = input("Desea continuar? (Y/N): ")
    if(ans == "N" or ans == "n"):
        end = True
input("Presione enter para continuar")
