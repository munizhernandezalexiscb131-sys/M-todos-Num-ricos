#ERROR DE TRUNCAMIENTO
#aproximación de x usando serie de taylor

# Librería matemática estándar
import math

# Valor donde se evaluará la función
x = 1

# Aproximación de e^x usando solo los primeros términos
aprox = 1 + x + (x ** 2) / 2
# Valor real usando la función exponencial
real = math.exp(x)
# Calcula el error absoluto
error = abs(real - aprox)

print("Aproximación: ", aprox)
print("Real: ", real)
print("Error: ", error)