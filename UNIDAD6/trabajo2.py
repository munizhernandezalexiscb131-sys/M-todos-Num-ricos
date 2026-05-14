#VISUALIZACION DE LA SOLUCION
import numpy as np
import matplotlib.pyplot as plt
def f(x,y):   #define la ecuacion diferencial
    return x + y   #retorna pendiente
x = 0   #valor inicial de x
y = 1   #condicion inicial
h = 0.1   #tamaño del paso

x_vals = []
y_vals = []

for i in range(20):   #ejecuta 5 iteraciones
    x_vals.append(x)   #guarda valor actual de x
    y_vals.append(y)   #guarda valor actual de y
    y = y + h * f(x,y)   #aproximacion numerica tipo euler 
    x = x + h   #incrementa x

plt.plot(x_vals,y_vals)   #grafica solucion aproximada
plt.xlabel("x")   #etiqueta eje x
plt.ylabel("y")   #etiqueta eje y
plt.title("solucion aproxiamda de la EDO")   #titulo
plt.grid()   #activa cuadricula
plt.show()   #muestra grafica