#APLICACION IA: APROXIMACION DE GRADIENTE
#funcion de perdida : L(w) = w**2 + 3w + 1
import numpy as np
def loss(w):                                 #define funcion de perdida
    return w**2 + 3*w + 1                    #define el polinomio
w = 1.5                                      #valor del parametro del modelo
h = 0.0001                                   #paso pequeño
grad = (loss(w + h) - loss(w - h)) / (2*h)   #aproximacion del gradiente
real = 2*w + 3                               #gradiente real

print("gradiente numerico: ", grad)          #muestra gradiente aproximado
print("gradiente real: ", real)              #muestra gradiente exacta