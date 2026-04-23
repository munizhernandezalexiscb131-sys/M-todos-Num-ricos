#APLICACION DE IA: calculo de area bajo la curva
#funcion tipo distribucion: f(x)=e**(-x**2)
import numpy as np
def f(x):  #define la funcion tipo gaussiana
    return np.exp(-x**2)   #retorna el valor e**(-x**2)
a = 0   #limite inferior de integracion
b = 1   #limite superior de integracion
n = 100   #numero de intervalos
h = (b - a) / n   #calcula el tamaño del paso
x = np.linspace(a, b, n + 1)   #genera los puntos de discretizacion del intervalo
y = f(x)   #evalua la funcion en todos los puntos
integral = (h / 2) * (y[0] + 2 * np.sum(y[1:n]) + y[n])   #aplica la formula del trapecio compuesto
print("Area bajo la curva: ", integral)   #muestra el resultado nuemrico

#la integracion numerica