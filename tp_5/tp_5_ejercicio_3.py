# Ejercicio 3
# Generar una lista con 15 numeros enteros al azar entre 1 y 100.
# Crear una lista con los pares y otra con los impares.
# Mostrar cuantos numeros tiene cada lista.
import random

print("Ejercicio 3")
numeros_azar = []
for _ in range(15):
    numero_generado = random.randint(1, 100)
    numeros_azar.append(numero_generado)

numeros_pares = []
numeros_impares = []

for numero in numeros_azar:
    if numero % 2 == 0:
        numeros_pares.append(numero)
    else:
        numeros_impares.append(numero)

print("Cantidad de numeros pares:", len(numeros_pares))
print("Cantidad de numeros impares:", len(numeros_impares))
