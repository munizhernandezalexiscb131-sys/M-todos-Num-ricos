#Método RK2
#resolver: dy/dx= x + y; y(0) = 1
import numpy as np

def f(x, y):        # Define la ecuación diferencial
    return x + y    # Retorna el valor de dy/dx

x = 0      # Valor inicial de x
y = 1      # Condición inicial y(0)=1
h = 0.1    # Tamaño del paso
n = 10     # Número de iteraciones

for i in range(n):              # Ejecuta el método RK2
    k1 = f(x, y)                # Calcula primera pendiente
    k2 = f(x + h/2, y + h*k1/2) # Calcula pendiente intermedia

    y = y + h * k2              # Actualiza valor de y
    x = x + h                   # Incrementa x

    print("x =", x, " y =", y)  # Muestra aproximación

