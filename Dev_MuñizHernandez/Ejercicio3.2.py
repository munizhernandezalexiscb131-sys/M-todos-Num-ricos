#PROPAGACION DEL ERROR
#Función: y = x**2

x= 2
dx = 0.01
# Evalúa la función
y = x**2
# Aproximación del error usando derivada
dy = abs(2 * x) * dx

print("y: ", y)
print("Error aproximado de y: ", dy)