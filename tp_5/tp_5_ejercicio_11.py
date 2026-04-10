# Ejercicio 11
# Crear una lista con los nombres de 10 estudiantes.
# Solicitar al usuario que ingrese un nombre a buscar.
# Indicar si el nombre se encuentra en la lista.
# Mostrar la posicion en la que aparece.
# Si no se encuentra, informar que no esta en la lista.
print("Ejercicio 11")
estudiantes = [
    "Ana",
    "Bruno",
    "Carla",
    "Diego",
    "Elena",
    "Federico",
    "Gabriela",
    "Hector",
    "Ines",
    "Julian",
]

nombre_buscado = input("Ingrese un nombre a buscar: ").strip()
posicion_encontrada = -1

for indice in range(len(estudiantes)):
    if estudiantes[indice].lower() == nombre_buscado.lower():
        posicion_encontrada = indice
        break

if posicion_encontrada != -1:
    print("El nombre se encuentra en la lista.")
    print("Posicion:", posicion_encontrada + 1)
else:
    print("El nombre no esta en la lista.")
