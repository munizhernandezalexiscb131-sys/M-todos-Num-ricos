#Aplicación IA: dinamica de pesos
#modelo: dw/dt= -0.5w
import numpy as np

def f(t, w):        # define ecuación diferencial
    return -0.5 * w # modelo de decaimiento

t = 0      # tiempo inicial
w = 10     # peso inicial
h = 0.1    # paso temporal

for i in range(20):                 # ejecuta RK4
    k1 = f(t, w)                    # primera pendiente
    k2 = f(t + h/2, w + h*k1/2)     # segunda pendiente
    k3 = f(t + h/2, w + h*k2/2)     # tercera pendiente
    k4 = f(t + h, w + h*k3)         # cuarta pendiente

    w = w + (h/6) * (k1 + 2*k2 + 2*k3 + k4) # actualización
    t = t + h                       # incrementa tiempo

    print("t =", t, " w =", w)      # muestra evolucion