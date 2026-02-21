#CIFRAS SIGNIFICATIVAS Y REDONDEO
#objetivo: analizar el efecto del redondeo.

# Importa la librería NumPy para cálculos numéricos
import numpy as np 

# Se define un número con muchas cifras decimales
x= 3.1415926535

# Redondea x a 2 decimales
print(round(x, 2))
# Redondea x a 4 decimales
print(round(x, 4))
# Redondea x a 6 decimales
print(round(x, 6))