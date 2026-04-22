#RESOLUCION CON SCIPY
import numpy as np
from scipy.optimize import fsolve #importa el metodo fsolve para resolver sistemas no lineales
def sistema(vars):                #define la funcion que representa el sistema de ecuaciones
  x, y = vars                     #separa las variables del vector de entrada
  f1 = x**2 + y**2 - 4            #primera ecuacion del sistema
  f2 = x - y - 1                  #segunda ecuacion del sistema
  return [f1, f2]                 #devuelve el sistema evaluado
sol = fsolve(sistema, [1, 1])     #busca la solucion usando como aproximacion inicial (1,1)
print("solucion aproximada",sol)  #imprime la solucion encontrada