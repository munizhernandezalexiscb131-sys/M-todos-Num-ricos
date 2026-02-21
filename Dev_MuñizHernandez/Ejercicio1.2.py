#ERROR DE REDONDEO EN PYTHON
#observar error de punto flotante

# Suma de números decimales en punto flotante
a = 0.1 + 0.2
# Valor esperado matemáticamente
b = 0.3

# Muestra el resultado real almacenado en memoria
print(a)
# Compara si son exactamente iguales
print(a == b)
# Calcula el error absoluto entre ambos valores
print(abs(a - b))