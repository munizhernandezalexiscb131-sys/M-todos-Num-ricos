#REGLA SIMPSON
import numpy as np
def f(x):  #define la funcion a integrar
    return x**2   #retorna el valor de la funcio x ** 2
a = 0   #limite inferior de integracion
b = 2   #limite superior de integracion
n = 100   #numero de subintervalos (debe ser par)
h = (b - a) / n   #calcula el tamaño del paso
x = np.linspace(a, b, n + 1)   #genera los puntos de discretizacion del intervalo
y = f(x)   #evalua la funcion en todos los puntos
suma = y[0] + y[n]   #inicializa la suma con extremos
for i in range(1,n):   #itera sobre los puntos interiores
    if i % 2 == 0:   #verifica si el indice es par
        suma += 2 * y[i]   #aplica el coeficiente 2
    else:
        suma += 4 * y[i]   #aplica el coeficiente 4
integral = (h / 3) * suma   #aplica la formula de simpson
print("Integral aproximada (Simpson): ", integral)   #muestra el resultado nuemrico
