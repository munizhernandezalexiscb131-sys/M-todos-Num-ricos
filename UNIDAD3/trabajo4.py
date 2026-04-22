#VISUALIZACION GRÁFICA DEL SISTEMA
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 400)  #genera 400 valores igualmente espaciados entre -3 y 3 para el eje x
y1 = np.sqrt(4 - x**2)       #calcula la parte superior del circulo usando la ecuacion x**2 + y**2 -4
y2 = -np.sqrt(4 - x**2)      #calcula la parte inferior del circulo
y_line = x - 1               #calcula los valores de y de la recta definida por la ecuacion x - y - 1 = 0

plt.plot(x,y1)              #grafica la mitad superior del circulo
plt.plot(x,y2)              #grafica la mitad inferior del circulo
plt.plot(x,y_line)          #grafica la recta del sistema

plt.xlabel('x')             #etiqueta del eje horizontal
plt.ylabel('y')             #etiqueta del eje vertical
plt.title('Sistema de ecuaciones no lineales') #titulo del grafico
plt.grid(True)              #agrega una grilla al grafico
plt.show()                  #muestra el grafico