#Comparación Euler vs RK4

import numpy as np  # Biblioteca numérica

def f(x, y):        # Define ecuación diferencial
    return x + y    # Retorna dy/dx

def exacta(x):              # Define solución analítica
    return 2 * np.exp(x) - x - 1  # Solución exacta

h = 0.1      # Tamaño del paso
x = 0        # Valor inicial

y_euler = 1  # Condición inicial para Euler
y_rk4 = 1    # Condición inicial para RK4

for i in range(10):                      # ejecuta iteraciones

    # metodo de Euler
    y_euler = y_euler + h * f(x, y_euler) # euler

    # metodo RK4
    k1 = f(x, y_rk4)                      # primera pendiente
    k2 = f(x + h/2, y_rk4 + h*k1/2)       # segunda pendiente
    k3 = f(x + h/2, y_rk4 + h*k2/2)       # tercera pendiente
    k4 = f(x + h, y_rk4 + h*k3)           # cuarta pendiente

    y_rk4 = y_rk4 + (h/6) * (k1 + 2*k2 + 2*k3 + k4) #actualizacion RK4

    x = x + h                             # incrementa x

real = exacta(x)                          # calcula solucion exacta

error_euler = abs(real - y_euler)         # error Euler
error_rk4 = abs(real - y_rk4)             # error RK4

print("Exacta:", real)
print("Euler:", y_euler)
print("RK4:", y_rk4)
print("Error Euler:", error_euler)
print("Error RK4:", error_rk4)