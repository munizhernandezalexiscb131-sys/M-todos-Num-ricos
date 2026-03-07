#VERIFICAR CAMBIO DE SIGNO
#25/02/20206
import numpy as np

def f(x):  #definicion de la funcion matematica
    return x**3 - x - 2 #expresion algebraica de la funcion

a = 1   #limite inferior del intervalo
b = 2   #limite superior del intervalo

fa = f(a)   #evaluacion de la funcion en el extremo izquierdo
fb = f(b)    #evaluacion de la funcion en el extremo derecho

print("f(a):", fa)   #mostrar valor a
print("f(b):", fb)   #mostrar valor b

if fa * fb < 0:    #verificar condicion del teorema del valor intermedio
    print("existe al menos una raiz en el intervalo")   #confirmacion
else:
    print("no se garantiza raiz en el intervalo")     #no hay cambio de signo