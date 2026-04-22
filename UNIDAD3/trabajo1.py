#REGRESION LINEAL
import numpy as np
X = np.array([[1,1],   #matriz de datos donde la primera columna es el termino independiente
              [1,2],   #segunda observacion del conjunto de datos
              [1,3],   #tercera observacion
              [1,4]])  #cuarta observacion
y = np.array([6,5,7,10])  #vector de valores observados
XT = X.T  #calcula la transpuesta de la matriz de datos
beta = np.linalg.inv(XT.dot(X)).dot(XT).dot(y)  #calcula los coeficientes de la regresion
print("coeficientes del modelo: ", beta)