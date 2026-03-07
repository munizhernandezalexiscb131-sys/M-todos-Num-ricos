import numpy as np #biblioteca para calculos numericos
def g(x): #definicion de la funcion iterativa g(x)
   return np.cos(x)  #funcion coseno que define el punto fijo

x = 0.5 #valor inicial de la aproximacion
tolerancia = 1e-6  #error maximo permitido
max_iter = 100  #numero maximo de iteraciones

for i in range(max_iter):  #ciclo de iteracion
   x_nuevo = g(x)  #aplicacion de la formula de aproximacion

   if abs(x_nuevo - x) < tolerancia:  #criterio de paro basado
      break  #termina si la diferencia es suficiente pequeño

   x = x_nuevo  #actualizacion del valor para la siguiente iteracion

print("Raiz aproximada: ", x_nuevo)  #mostrar resultado final
print("Iteraciones realizadas: ", i+1)   #mostrar numero de iteraciones