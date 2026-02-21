#OPTIMIZACION NUMERICA SIMPLE
#Minimizar f(x) = (x - 3)**2

x = 0
# Tasa de aprendizaje
alpha = 0.1

# Realiza 20 iteraciones
for _ in range (20):
    # Gradiente correcto de f(x) = (x-3)²
    grad = 2 * (x - 3)
    # Actualiza x según descenso gradiente
    x = x - alpha * grad
# Imprime el valor aproximado al mínimo    
print (x)    