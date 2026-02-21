#SESGO NUMERICO EN DATOS
#Simular sesgo en un conjunto de datos
import numpy as np

# Genera 1000 datos normales
datos_reales = np.random.normal(0, 1, 1000)
# Define un sesgo constante
sesgo = 0.5
# Muestra los datos originales
print(datos_reales)

# Aplica el sesgo sumando constante
datos_sesgados = datos_reales + sesgo

print(datos_sesgados)
print("Media Real: ", np.mean(datos_reales))
print("Media Sesgada: ", np.mean(datos_sesgados))

