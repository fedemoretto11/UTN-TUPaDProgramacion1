operador = input("Ingrese el nombre del operador: ")

while not operador.isalpha() or operador == "":
    print("Error: El nombre del operador debe contener solo letras.")
    operador = input("Ingrese el nombre del operador: ")

lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""
martes1 = ""
martes2 = ""
martes3 = ""

opcion_menu = ""

while opcion_menu != "5":
  print("\n--- AGENDA DE TURNOS ---")
  print("1. Reservar turno")
  print("2. Cancelar turno")
  print("3. Ver agenda del dia")
  print("4. Ver resumen general")
  print("5. Cerrar sistema")

  opcion_menu = input("Seleccione una opcion: ")

  while not opcion_menu.isdigit() or int(opcion_menu) < 1 or int(opcion_menu) > 5:
    print("Opcion invalida. Por favor seleccione una opcion del 1 al 5.")
    opcion_menu = input("Seleccione una opcion: ")

  if opcion_menu == "1":
    print("\n--- RESERVAR TURNO ---")
    dia = input("Elija día (1=Lunes, 2=Martes): ")

    while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
      print("Opcion invalida. Por favor seleccione 1 para Lunes o 2 para Martes.")
      dia = input("Elija día (1=Lunes, 2=Martes): ")
    
    paciente = input("Ingrese el nombre del paciente: ")

    while not paciente.isalpha() or paciente == "":
      print("Nombre de paciente incorrecto")
      paciente = input("Ingrese el nombre del paciente: ")

    if dia == "1":
      if paciente == lunes1 or paciente == lunes2 or paciente == lunes3 or paciente == lunes4:
        print("El paciente ya tiene un turno reservado el Lunes")
      else:
        if lunes1 == "":
          lunes1 = paciente
          print(f"Turno reservado para {paciente} el Lunes en el turno 1")
        elif lunes2 == "":
          lunes2 = paciente
          print(f"Turno reservado para {paciente} el Lunes en el turno 2")
        elif lunes3 == "":
          lunes3 = paciente
          print(f"Turno reservado para {paciente} el Lunes en el turno 3")
        elif lunes4 == "":
          lunes4 = paciente
          print(f"Turno reservado para {paciente} el Lunes en el turno 4")
        else:
          print("No hay turnos disponibles el Lunes")
    elif dia == "2":
      if paciente == martes1 or paciente == martes2 or paciente == martes3:
        print("El paciente ya tiene un turno reservado el Martes")
      else:
        if martes1 == "":
          martes1 = paciente
          print(f"Turno reservado para {paciente} el Martes en el turno 1")
        elif martes2 == "":
          martes2 = paciente
          print(f"Turno reservado para {paciente} el Martes en el turno 2")
        elif martes3 == "":
          martes3 = paciente
          print(f"Turno reservado para {paciente} el Martes en el turno 3")
        else:
          print("No hay turnos disponibles el Martes")
  elif opcion_menu == "2":
    print("\n--- CANCELAR TURNO ---")
    dia = input("Elija día (1=Lunes, 2=Martes): ")

    while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
      print("Opcion invalida. Por favor seleccione 1 para Lunes o 2 para Martes.")
      dia = input("Elija día (1=Lunes, 2=Martes): ")
    
    paciente = input("Ingrese el nombre del paciente: ")

    while not paciente.isalpha() or paciente == "":
      print("Nombre de paciente incorrecto")
      paciente = input("Ingrese el nombre del paciente: ")

    if dia == "1":
      if paciente == lunes1:
        lunes1 = ""
        print(f"Turno cancelado para {paciente} el Lunes en el turno 1")
      elif paciente == lunes2:
        lunes2 = ""
        print(f"Turno cancelado para {paciente} el Lunes en el turno 2")
      elif paciente == lunes3:
        lunes3 = ""
        print(f"Turno cancelado para {paciente} el Lunes en el turno 3")
      elif paciente == lunes4:
        lunes4 = ""
        print(f"Turno cancelado para {paciente} el Lunes en el turno 4")
      else:
        print("El paciente no tiene un turno reservado el Lunes")
    elif dia == "2":
      if paciente == martes1:
        martes1 = ""
        print(f"Turno cancelado para {paciente} el Martes en el turno 1")
      elif paciente == martes2:
        martes2 = ""
        print(f"Turno cancelado para {paciente} el Martes en el turno 2")
      elif paciente == martes3:
        martes3 = ""
        print(f"Turno cancelado para {paciente} el Martes en el turno 3")
      else:
        print("El paciente no tiene un turno reservado el Martes")
  elif opcion_menu == "3":
    print("\n--- AGENDA DEL DIA ---")
    dia = input("Elija día (1=Lunes, 2=Martes): ")

    while not dia.isdigit() or int(dia) < 1 or int(dia) > 2:
      print("Opcion invalida. Por favor seleccione 1 para Lunes o 2 para Martes.")
      dia = input("Elija día (1=Lunes, 2=Martes): ")

    if dia == "1":
      print("\nAgenda del Lunes:")
      print(f"Turno 1: {lunes1 if lunes1 != '' else 'libre'}")
      print(f"Turno 2: {lunes2 if lunes2 != '' else 'libre'}")
      print(f"Turno 3: {lunes3 if lunes3 != '' else 'libre'}")
      print(f"Turno 4: {lunes4 if lunes4 != '' else 'libre'}")
    elif dia == "2":
      print("\nAgenda del Martes:")
      print(f"Turno 1: {martes1 if martes1 != '' else 'libre'}")
      print(f"Turno 2: {martes2 if martes2 != '' else 'libre'}")
      print(f"Turno 3: {martes3 if martes3 != '' else 'libre'}")
  elif opcion_menu == "4":
    ocupados_lunes = 0
    ocupados_martes = 0

    if lunes1 != "":
      ocupados_lunes += 1
    if lunes2 != "":
      ocupados_lunes += 1
    if lunes3 != "":
      ocupados_lunes += 1
    if lunes4 != "":
      ocupados_lunes += 1
    if martes1 != "":
      ocupados_martes += 1
    if martes2 != "":
      ocupados_martes += 1
    if martes3 != "":
      ocupados_martes += 1
    
    disponibles_lunes = 4 - ocupados_lunes
    disponibles_martes = 3 - ocupados_martes

    print("\n--- RESUMEN GENERAL ---")
    print(f"Total de turnos ocupados el Lunes: {ocupados_lunes} || Total de turnos disponibles el Lunes: {disponibles_lunes}")
    print(f"Total de turnos ocupados el Martes: {ocupados_martes} || Total de turnos disponibles el Martes: {disponibles_martes}")
  elif opcion_menu == "5":
    print("Saliendo del sistema")
  
    



