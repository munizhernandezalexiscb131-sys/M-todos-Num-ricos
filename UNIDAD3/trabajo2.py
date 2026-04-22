#EVALUACION DEL ERROR
import numpy as np
x = 1.822  #valor aproximado de la variable x obtenido numericamente
y = 0.822  #valor aproximado de la variable y obtenido numericamente

f1= x**2 + y**2 - 4  #evalua la primera ecuacion usando la solucion aproximado
f2 = x - y - 1   #evalua la segunda ecuacion usando la solucion aproximado
print("error ecuacion 1: ",f1)  #muestra el error residual de la
print("error ecuacion 2: ",f2)  #muestra el error residual de la