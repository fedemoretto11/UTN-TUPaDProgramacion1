# Ejercicio 9
# Representar un tablero de Ta-Te-Ti como una lista de listas de 3x3.
# Inicializarlo con guiones para las casillas vacias.
# Permitir que dos jugadores ingresen posiciones para colocar X u O.
# Mostrar el tablero despues de cada jugada valida.
print("Ejercicio 9")
tablero = [["-" for _ in range(3)] for _ in range(3)]
simbolos_jugadores = ["X", "O"]
jugadas_validas = 0

print("Tablero inicial:")
for fila_tablero in tablero:
    print(" ".join(fila_tablero))

while jugadas_validas < 9:
    jugador_actual = simbolos_jugadores[jugadas_validas % 2]
    print("Turno del jugador", jugador_actual)

    try:
        fila_elegida = int(input("Ingrese la fila (0, 1 o 2): "))
        columna_elegida = int(input("Ingrese la columna (0, 1 o 2): "))
    except ValueError:
        print("Debe ingresar solo numeros enteros.")
        continue

    if fila_elegida not in [0, 1, 2] or columna_elegida not in [0, 1, 2]:
        print("La fila y la columna deben estar entre 0 y 2.")
        continue

    if tablero[fila_elegida][columna_elegida] != "-":
        print("La casilla ya esta ocupada. Intente otra vez.")
        continue

    tablero[fila_elegida][columna_elegida] = jugador_actual
    jugadas_validas += 1

    print("Tablero despues de la jugada:")
    for fila_tablero in tablero:
        print(" ".join(fila_tablero))
