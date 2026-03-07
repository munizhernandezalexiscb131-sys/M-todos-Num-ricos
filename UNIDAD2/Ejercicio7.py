#interpolacion con numpy
import numpy as np

x_datos = np.array([0, 1, 2])  #arreglo con valor conocidos en x
y_datos = np.array([1, 3, 2])  #arreglo con valor conocidos en y

coeficientes = np.polyfit(x_datos, y_datos, 2)  #ajuste de polinomio grado 2
polinomio = np.poly1d(coeficientes)  #construccion del polinomio

x_eval = 1.5  #punto donde se evaluara el polinomio
y_eval = polinomio(x_eval)  #evaluacion del polinomio

print("Coeficientes del polinomio: ", coeficientes)  #Mostrar coeficientes
print("Valor interpolado: ", y_eval)  #mostrar valor interpolado