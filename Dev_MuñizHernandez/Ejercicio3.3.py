#VISUALIZACIÓN DEL ERRROR
#Objetivo: analizar comportamiento numérico
import numpy as np
# Librería para gráficos
import matplotlib.pyplot as plt

# Valores de x
x = np.linspace(-1, 5, 100)
# Función de costo
y = (x - 2)**2

# Grafica la función
plt.plot(x, y)
# Etiqueta eje X
plt.xlabel("X")
# Etiqueta eje Y
plt.ylabel("f(X)")
# Título
plt.title("Función de costo")
# Muestra la gráfica
plt.show()