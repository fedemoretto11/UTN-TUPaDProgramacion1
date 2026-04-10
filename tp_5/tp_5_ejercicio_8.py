# Ejercicio 8
# Crear una matriz con las notas de 5 estudiantes en 3 materias.
# Mostrar el promedio de cada estudiante.
# Mostrar el promedio de cada materia.
print("Ejercicio 8")
notas_por_estudiante = [
    [7, 8, 6],
    [9, 10, 5],
    [8, 7, 6],
    [6, 9, 8],
    [5, 7, 9],
]

for indice_estudiante in range(len(notas_por_estudiante)):
    promedio_estudiante = sum(notas_por_estudiante[indice_estudiante]) / len(
        notas_por_estudiante[indice_estudiante]
    )
    print("Promedio del estudiante", indice_estudiante + 1, ":", promedio_estudiante)

print("")
print("Promedios de cada materia:")
for indice_materia in range(len(notas_por_estudiante[0])):
    suma_materia = 0
    for indice_estudiante in range(len(notas_por_estudiante)):
        suma_materia += notas_por_estudiante[indice_estudiante][indice_materia]
    promedio_materia = suma_materia / len(notas_por_estudiante)
    print("Materia", indice_materia + 1, ":", promedio_materia)
