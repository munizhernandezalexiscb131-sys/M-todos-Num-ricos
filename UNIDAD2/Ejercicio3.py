a = 1   #limite inicial inferior
b = 2   #limite inicial superior
n = 22   #numero de iteraciones

error_teorico = (b - a) / (2**n)   #formula del error maximo de biseccion

print("error maximo despues de ", n," iteraciones: ", error_teorico)   #mostrar error