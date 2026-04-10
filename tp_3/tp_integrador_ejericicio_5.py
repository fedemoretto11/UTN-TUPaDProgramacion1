print("--- BIENVENIDO A LA ARENA ---")

# Paso 1: nombre del gladiador
nombre = input("Nombre del Gladiador: ")
while nombre == "" or not nombre.isalpha():
    print("Nombre incorrecto, ingrese denuevo")
    nombre = input("Nombre del Gladiador: ")

vida_jugador = 100
vida_enemigo = 100
pociones = 3
danio_ataque_pesado = 15
danio_enemigo = 12
turno_gladiador = True

print(f"\nInicio")
print(f"\n{nombre} vs Enemigo")

while vida_jugador > 0 and vida_enemigo > 0:
    if turno_gladiador:
      print(f"\n{nombre} (HP: {vida_jugador}) vs Enemigo (HP: {vida_enemigo}) | Pociones: {pociones}")
      print("Elige accion:")
      print("1. Ataque Pesado")
      print("2. Rafaga Veloz")
      print("3. Curar")

      opcion = input("Opcion: ")
      while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
          print("Opcion incorrecta, ingrese denuevo")
          opcion = input("Opcion: ")
      
      if opcion == "1":
        danio_final = danio_ataque_pesado
        if vida_enemigo < 20:
          danio_final = danio_ataque_pesado * 1.5
          print("Golpe critico")
        vida_enemigo -= danio_final
        print(f"{nombre} ataca con Ataque Pesado causando {danio_final} de daño")
      elif opcion == "2":
        print("Rafaga Veloz de golpes")
        for i in range(3):
          vida_enemigo -= 5
          print(f"Golpe {i+1} causa 5 de daño")
      elif opcion == "3":
        if pociones > 0:
          vida_jugador += 30
          pociones -= 1
          if vida_jugador > 100:
            vida_jugador = 100
          print(f"{nombre} se cura usando una pocion. Vida actual: {vida_jugador}")
        else:
          print("No tienes pociones disponibles")
      turno_gladiador = False
    else:
      if vida_enemigo > 0:
        vida_jugador -= danio_enemigo
        print(f"El enemigo ataca causando {danio_enemigo} de daño")
      turno_gladiador = True
        
print("\n--- FIN DEL COMBATE ---")
if vida_jugador > 0:
    print(f"Ganaste! {nombre} ha ganado la batalla.")
else:
    print("Perdiste! Has caido en combate.")