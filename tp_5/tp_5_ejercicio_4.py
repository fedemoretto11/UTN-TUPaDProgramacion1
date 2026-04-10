# Ejercicio 4
# Dada una lista con valores repetidos, crear una nueva lista sin repetidos.
# Mostrar el resultado.
print("Ejercicio 4")
datos_repetidos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
datos_sin_repetidos = []

for dato in datos_repetidos:
    if dato not in datos_sin_repetidos:
        datos_sin_repetidos.append(dato)

print("Lista sin elementos repetidos:")
for dato in datos_sin_repetidos:
    print(dato)
