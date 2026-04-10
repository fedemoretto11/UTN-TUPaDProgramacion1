# Ejercicio 6
# Dada una lista con 7 numeros, rotar todos los elementos una posicion hacia la derecha.
print("Ejercicio 6")
numeros_originales = [1, 2, 3, 4, 5, 6, 7]
ultimo_valor = numeros_originales[-1]

for indice in range(len(numeros_originales) - 1, 0, -1):
    numeros_originales[indice] = numeros_originales[indice - 1]

numeros_originales[0] = ultimo_valor

print("Lista rotada hacia la derecha:")
for numero in numeros_originales:
    print(numero)
