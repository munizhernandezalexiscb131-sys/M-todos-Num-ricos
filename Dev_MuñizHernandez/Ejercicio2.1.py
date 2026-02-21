#PRESICION VS EXACTITUD
import numpy as np

# Datos experimentales
mediciones = np.array([9.8, 9.81, 9.79, 9.80])
# Valor real de referencia
valor_real = 9.81

# Calcula la media de las mediciones
media = np.mean(mediciones)
# Calcula el error absoluto
error = abs(media - valor_real)

print("Media: ", media)
print("Error absoluto: ", error)