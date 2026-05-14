#RESOLVER UNA EDO SIMPLE
#EDO: dy/dx= x + y
#condicion inicial: y(0)= 1
import numpy as np
def f(x,y):   #define la ecuacion diferencial
    return x + y   #retorna el valor de dy/dx
x = 0   #valor inicial de x
y = 1   #condicion inicial
h = 0.1   #tamaño del paso

for i in range(5):   #ejecuta 5 iteraciones
    y = y + h * f(x,y)   #aproximacion numerica tipo euler 
    x = x + h   #avanza al siguiente punto
    print("x= ",x," y= ",y)
    