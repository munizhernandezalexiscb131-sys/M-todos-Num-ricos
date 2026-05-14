#Aplicación IA: descenso dinámico
#modelo: dw/dt= -0.3w
import numpy as np 

def f(t, w):        # Define ecuación diferencial
    return -0.3 * w # Modelo de decaimiento del peso

t = 0      # Tiempo inicial
w = 5      # Peso inicial del modelo
h = 0.2    # Paso temporal
n = 20     # Número de iteraciones

for i in range(n):          # Ejecuta Euler
    w = w + h * f(t, w)     # Actualiza peso
    t = t + h               # Incrementa tiempo

    print("t =", t, " w =", w)  # Muestra evolución
