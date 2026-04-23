import numpy as np
def f(x,y): #define funcion bidimensional
    return np.exp(-(x**2 + y**2)) #

a, b = -1, 1 #define los limites en el eje x
c, d = -1, 1 #define los limites en el eje y

n = 100 #numero de puntos en x
m = 100 #numero de puntos en y

dx = (b - a)/ n #calcula el tamaño del paso en x
dy = (d - c)/ m #calcula el tamaño del paso en y

integral = 0 #inicializa el acumulador de la integral

for i in range(n): #itera en x
    for j in range(m): #itera en y
        x = a + i*dx #calcula punto en x
        y = c + j*dy #calcula punto en y
        integral += f(x[i],y[j]) #acumula valor ponderado