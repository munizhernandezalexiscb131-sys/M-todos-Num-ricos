#Error numerico
#libreria para matematicas
import math

# Valor real de raíz de 2
real = math.sqrt(2)
# Valor aproximado
aprox = 1.4134134134134133

error_absoluto = abs(real - aprox)
error_relativo = error_absoluto / real

# Muestra ambos errores
print(error_absoluto, error_relativo)