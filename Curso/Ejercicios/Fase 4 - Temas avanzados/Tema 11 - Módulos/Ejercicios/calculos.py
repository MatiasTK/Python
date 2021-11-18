from operaciones import *

a,b,c,d = (10,5,0,"Hola")

print("{} + {} = {}".format(a,b,suma(a,b)))
print("{} - {} = {}".format(b,d,resta(b,d)))
print("{} * {} = {}".format(b,b,producto(b,b)))
print("{} / {} = {}".format(a,c,division(a,c)))

print("==========================\nTesting\n==========================")

print("{} + {} = {}".format(a,d,suma(a,d)))
print("{} + {} = {}".format(a,c,suma(a,c)))
print("{} - {} = {}".format(a,d,resta(a,d)))
print("{} - {} = {}".format(a,c,resta(a,c)))
print("{} * {} = {}".format(b,c,producto(b,c)))
print("{} * {} = {}".format(b,d,producto(b,d)))
print("{} / {} = {}".format(a,b,division(a,b)))
print("{} / {} = {} (Reverse enabled)".format(a,b,division(a,b,reverse=True)))
print("{} / {} = {}".format(a,d,division(a,d)))




