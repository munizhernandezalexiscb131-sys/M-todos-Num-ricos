#METODO JACOBI
import numpy as np

A = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])
b = np.array([11,12,13])
x = np.zeros(3)                            #vector inicial de aproximacion para las variables
tol = 1e-6
max_iter = 100

for k in range(max_iter):
  x_new = np.zeros(3)                      #vector donde se guardara la nueva aproximacion
  x_new[0] = (11 - x[1] + x[2]) / 10       #despejar de x a partir de la primera ecuacion
  x_new[1] = (12 - 2*x[0] + x[2]) / 10     #despejar de y a partir de la segunda ecuacion
  x_new[2] = (13 - 2*x[0] + 3*x[1]) / 10   #despejar de z a partir de la tercera ecuacion

  if np.linalg.norm(x_new - x) < tol:      #verifica si el cambio entre iteraciones es menor que
    break
  x = x_new                                #actualiza la aproximacion para la siguiente iteracion
print("solucion aproximado: ", x_new)
print("iteraciones: ", k+1)