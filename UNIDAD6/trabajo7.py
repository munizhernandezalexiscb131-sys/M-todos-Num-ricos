#Visualización gráfica

import numpy as np              
import matplotlib.pyplot as plt 

def f(x, y):        # Define EDO
    return x + y    # Función diferencial

x = 0      # Valor inicial
y = 1      # Condición inicial
h = 0.1    # Tamaño del paso

x_vals = [] # Lista para almacenar valores de x
y_vals = [] # Lista para almacenar valores de y

for i in range(20):         # Ejecuta iteraciones
    x_vals.append(x)        # Guarda x
    y_vals.append(y)        # Guarda y

    y = y + h * f(x, y)     # Euler
    x = x + h               # Incrementa x

plt.plot(x_vals, y_vals)    # Grafica solución numérica
plt.xlabel("x")             # Etiqueta eje x
plt.ylabel("y")             # Etiqueta eje y
plt.title("Método de Euler") # Título
plt.grid()                  # Activa cuadrícula
plt.show()                  # Muestra gráfica
