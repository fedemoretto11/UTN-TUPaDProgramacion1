# Ejercicio 12
# Pedir al usuario que ingrese 8 numeros enteros y almacenarlos en una lista.
# Mostrar la lista original.
# Mostrar la lista ordenada de menor a mayor.
# Mostrar la lista ordenada de mayor a menor.
# Investigar el uso de sorted() y del parametro reverse.
print("Ejercicio 12")
numeros_ingresados = []

while len(numeros_ingresados) < 8:
    try:
        numero = int(input(f"Ingrese el numero entero {len(numeros_ingresados) + 1}: "))
        numeros_ingresados.append(numero)
    except ValueError:
        print("Debe ingresar un numero entero valido.")

print("Lista original:", numeros_ingresados)
print("Lista ordenada de menor a mayor:", sorted(numeros_ingresados))
print("Lista ordenada de mayor a menor:", sorted(numeros_ingresados, reverse=True))
