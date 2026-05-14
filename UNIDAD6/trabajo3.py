#Aplicación IA: dinámica de aprendizaje
#modelo simplificado: dw/dt= -0.5w
import numpy as np  # Importa NumPy

def f(t, w):        # Define ecuación diferencial
    return -0.5 * w # Modelo de decaimiento exponencial

t = 0      # Tiempo inicial
w = 10     # Peso inicial del modelo
h = 0.1    # Paso temporal

for i in range(20):         # Ejecuta iteraciones
    w = w + h * f(t, w)     # Actualiza peso
    t = t + h               # Incrementa tiempo

    print("t =", t, " w =", w)  # Muestra evolución
