#DIFERENCIA CENTRAL
import numpy as np
def f(x):
    return x**3                       #retorna el valor de la funcion x**3
x = 2                                 #punto donde se calculará la derivada
h = 0.001                             #tamaño del paso numerico
derivada = (f(x + h) - f(x - h)) / (2 * h)      #aplica la formula de diferencia central
real = 3 * x ** 2                     #calcula la derivada analitica real
error = abs(real - derivada)          #calcula el error absoluto
print("derivada central: ",derivada)  #muestra el valor aproximado
print("derivada real: ", real)        #muestra el valor exacto
print("error: ", error)               #diferencia entre ambos