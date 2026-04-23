#ejercicio 1 - tema 2
#REGLA DEL TRAPECIO
import numpy as np
def f(x):  #define la funcion a integrar
    return x**2   #retorna el valor de la funcio x ** 2
a = 0   #limite inferior de integracion
b = 2   #limite superior de integracion
n = 100   #numero de subintervalos
h = (b - a) / n   #calcula el tamaño del paso
x = np.linspace(a, b, n + 1)   #genera los puntos de discretizacion del intervalo
y = f(x)   #evalua la funcion en todos los puntos
integral = (h / 2) * (2 * np.sum(y[1:n]) + y[n])   #aplica la formula del trapecio compuesto
print("Integral aproximada (Trapecio): ", integral)   #muestra el resultado nuemrico