#Parte A
print("PARTE A")
import numpy as np
mediciones = np.array([2.51, 2.49, 2.50, 2.52, 2.48])
real = 2.5

media = np.mean(mediciones)
E_absoluto = abs(real - media)
E_relativo = E_absoluto / real
E_porcentual = ((media - real)/real)*100

mediar = round(media, 3)
E_absolutor = round(E_absoluto, 3)
E_relativor = round(E_relativo, 3)
E_porcentualr = round(E_porcentual, 3)
DE = np.std(mediciones)
DEr = round(DE, 3)

print(f"Desviacion estandar (presicion): {DEr}")
print(f"El valor de aproximado es: {mediar} (es exacto)")
print(f"El Error Absoluto es: {E_absolutor}")
print(f"El Error Relativo es: {E_relativor}")
print(f"El Error Porcentual es: {E_porcentualr} (no hay sesgo)")
print("x = ",media," ± ",DEr)

#Parte B
print("")
print("PARTE B")
m = 1.2
g = 9.81
h = media
E = m * g * h

print("Energia potencial: ",E)

deltaE = (E/h) * DE

print(f"Propagacion del error: {round(deltaE,3)}")