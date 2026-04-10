# Ejercicio 13
# Dada la siguiente lista de puntajes de un videojuego:
# puntajes = [450, 1200, 875, 990, 300, 1500, 640]
# Mostrar el puntaje mas alto y el mas bajo.
# Mostrar la lista ordenada de mayor a menor (ranking).
# Indicar en que posicion del ranking se encuentra el puntaje 990.
print("Ejercicio 13")
puntajes = [450, 1200, 875, 990, 300, 1500, 640]
ranking = sorted(puntajes, reverse=True)

print("Puntaje mas alto:", max(puntajes))
print("Puntaje mas bajo:", min(puntajes))
print("Ranking de mayor a menor:", ranking)

if 990 in ranking:
    print("El puntaje 990 esta en la posicion:", ranking.index(990) + 1)
else:
    print("El puntaje 990 no se encuentra en el ranking.")
