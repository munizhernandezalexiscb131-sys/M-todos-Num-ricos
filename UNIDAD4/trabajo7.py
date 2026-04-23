import numpy as np
def f(x,y):
    return x + y

a, b = 0, 1 #define los limites en el eje x
c, d = 0, 1 #define los limites en el eje y

n = 50 #numero de divisiones en x
m = 50 #numero de divisiones en y

dx = (b - a)/n #calcula el tamaño del paso en x
dy = (d - c)/m #calcula el tamaño del paso en y

integral = 0 #inicializa el acumulador de la integral

for i in range(n):
    for j in range(m):
        x = a + i*dx
        y = c + j*dy