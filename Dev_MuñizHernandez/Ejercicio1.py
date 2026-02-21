#EJERCICIO: aproximacion numerica de una raiz

import numpy as np

#1000 datos de 0 a 2
x = np.linspace(0, 2, 1000)

f = x ** 2 - 2

#np.argmin = para encontrar el valor minimo en un array
x_aprox = x[np.argmin(np.abs(f))]
# Imprime la aproximación de la raíz
print (x_aprox)