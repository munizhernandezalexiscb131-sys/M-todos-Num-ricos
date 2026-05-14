#Método RK4
import numpy as np  

def f(x, y):        # Define ecuación diferencial
    return x + y    # Función dy/dx

x = 0      # Valor inicial
y = 1      # Condición inicial
h = 0.1    # Tamaño del paso
n = 10     # Número de iteraciones

for i in range(n):                  # Ejecuta RK4
    k1 = f(x, y)                    # Primera pendiente
    k2 = f(x + h/2, y + h*k1/2)     # Segunda pendiente
    k3 = f(x + h/2, y + h*k2/2)     # Tercera pendiente
    k4 = f(x + h, y + h*k3)         # Cuarta pendiente

    y = y + (h/6) * (k1 + 2*k2 + 2*k3 + k4)  # Fórmula RK4
    x = x + h                       # Incrementa x

    print("x =", x, " y =", y)      # Muestra solución
