#ÁLGEBRA LINEAL CON NumPy
#Resolver: Ax = b
import numpy as np

# Define la matriz de coeficientes
A = np.array([[3, 2],[1, 2]])
# Define el vector independiente
b = np.array([5, 5])
# Resuelve el sistema lineal
x = np.linalg.solve(A, b)

# Resultado
print(x)