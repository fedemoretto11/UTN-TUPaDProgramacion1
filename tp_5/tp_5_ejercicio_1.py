# Ejercicio 1
# Crear una lista con las notas de 10 estudiantes.
# Mostrar la lista completa.
# Calcular y mostrar el promedio.
# Indicar la nota mas alta y la mas baja.
print("Ejercicio 1")
notas_estudiantes = [7, 8, 6, 9, 10, 5, 8, 7, 6, 9]

print("Lista completa de notas:")
for nota in notas_estudiantes:
    print(nota)

suma_notas = 0
for nota in notas_estudiantes:
    suma_notas += nota

promedio_notas = suma_notas / len(notas_estudiantes)
print("Promedio:", promedio_notas)

nota_mas_alta = notas_estudiantes[0]
nota_mas_baja = notas_estudiantes[0]

for nota in notas_estudiantes:
    if nota > nota_mas_alta:
        nota_mas_alta = nota
    if nota < nota_mas_baja:
        nota_mas_baja = nota

print("Nota mas alta:", nota_mas_alta)
print("Nota mas baja:", nota_mas_baja)
