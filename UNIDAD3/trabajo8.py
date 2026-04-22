x0 = 1  #primer punto en x
y0 = 2  #valor correspondiente en y
x1 = 3  #segundo punto en x
y1 = 6  #valor correspondiente en y
x = 2  #punto donde se desea interpolar
P = y0 + ((y1-y0)/(x1-x0))*(x-x0)  #formula
print("valor interpolado: ", P) #mostrar resulyado

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 3, 100)
y = y0 + ((y1-y0)/(x1-x0))*(x-x0)

plt.axhline(0)
plt.plot(x, y)
plt.title("Funcion f(x) = y0 + ((y1-y0)/(x1-x0))*(x-x0)")
plt.show()