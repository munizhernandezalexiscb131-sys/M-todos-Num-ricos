#Comparación con solución exacta
#solucion analitica es: y= 2e**x - x - 1
import numpy as np 

def f(x, y):        # Define EDO
    return x + y    # Define dy/dx

def exacta(x):              # Define solución analítica
    return 2 * np.exp(x) - x - 1  # Fórmula exacta

x = 0      # Valor inicial
y = 1      # Condición inicial
h = 0.1    # Tamaño del paso

for i in range(10):         # Ejecuta iteraciones
    y = y + h * f(x, y)     # Euler
    x = x + h               # Incrementa x

    real = exacta(x)        # Calcula solución exacta
    error = abs(real - y)   # Calcula error absoluto

    print("x =", x,
          "Euler =", y,
          "Exacta =", real,
          "Error =", error)
