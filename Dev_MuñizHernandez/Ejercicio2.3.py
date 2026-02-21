#OPTIMIZACION NUMÉRICA CON SciPy
#Minimizar: f(x) = (x - 2)**2

# Importa función de minimización
from scipy.optimize import minimize

# Define la función objetivo
f = lambda x: (x - 2)**2
# Minimiza empezando desde x=0
resultado = minimize(f, x0=0)

# Imprime el valor donde la función es mínima
print(resultado.x)
