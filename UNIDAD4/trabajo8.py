#METODO DEL TRAPECIO EN 2D
import numpy as np
def f(x,y): #define funcion bidimensional
    return x**2 + y**2 #funcion cuadratica

a, b = 0, 1 #define los limites en el eje x
c, d = 0, 1 #define los limites en el eje y

n = 50 #numero de puntos en x
m = 50 #numero de puntos en y

x = np.linspace(a, b, n) #genera puntos en x
y = np.linspace(a, b, m) #genera puntos en y

dx = (b - a)/ (n - 1) #calcula el tamaño del paso en x
dy = (d - c)/ (m - 1) #calcula el tamaño del paso en y

integral = 0 #inicializa el acumulador de la integral

for i in range(n): #itera en x
    for j in range(m): #itera en y
        peso = 1 #inicializa el peso
        if i==0 or i==n-1: #verifica si está en borde en x
            peso *= 0.5 #ajusta peso en borde
        if j==0 or j==m-1: #verifica si esta en borde en y
            peso *= 0.5 #ajusta peso en borde
        integral += peso*f(x[i],y[j]) #acumula valor ponderado

integral *= dx*dy #multiplica por el area del elemento
print("integral (trapecio 2D): ",integral)