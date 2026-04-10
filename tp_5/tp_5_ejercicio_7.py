# Ejercicio 7
# Crear una matriz de 7x2 con las temperaturas minimas y maximas de una semana.
# Calcular el promedio de las minimas y el de las maximas.
# Mostrar en que dia se registro la mayor amplitud termica.
print("Ejercicio 7")
temperaturas_semana = [
    [15, 25],
    [17, 28],
    [14, 22],
    [16, 27],
    [13, 24],
    [18, 30],
    [12, 20],
]

suma_minimas = 0
suma_maximas = 0

for temperatura_dia in temperaturas_semana:
    suma_minimas += temperatura_dia[0]
    suma_maximas += temperatura_dia[1]

promedio_minimas = suma_minimas / len(temperaturas_semana)
promedio_maximas = suma_maximas / len(temperaturas_semana)

print("Promedio de temperaturas minimas:", promedio_minimas)
print("Promedio de temperaturas maximas:", promedio_maximas)

mayor_amplitud = 0
dia_mayor_amplitud = 0

for indice_dia in range(len(temperaturas_semana)):
    amplitud_termica = temperaturas_semana[indice_dia][1] - temperaturas_semana[indice_dia][0]
    if amplitud_termica > mayor_amplitud:
        mayor_amplitud = amplitud_termica
        dia_mayor_amplitud = indice_dia + 1

print("Dia con mayor amplitud termica:", dia_mayor_amplitud)
