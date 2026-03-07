#IMPLEMENTAR BISECCION MANUAL
import numpy as np
def f(x):  #definicion de la funcion a analizar
    return x**3 - x - 2 #expresion algebraica de la funcion

a = 1   #extremo izquierdo inicial
b = 2   #extremo derecho inicial
tolerancia = 1e-6   #error maxima permitido
max_iter = 23   #numero maximo de iteraciones permitidas

for i in range(max_iter):   #ciclo de iteraciones
    c = (a + b) / 2   #calculo del punto medio
    fc = f(c)   #evaluacion de la funcion en el punto medio

    if abs(fc) < tolerancia:   #criterio de paro por valor cercano a cero
        break   #termina el ciclo

    if f(a) * fc < 0:   #verifica si la raiz esta en el subintervalo
        b = c   #actualiza extremo derecho
    else:
        a = c   #actualiza el extremo izquierdo

print("raiz aproximada: ",c)   #muestra la raiz
print("iteraciones realizadas: ", i+1)   #numero de iteraciones