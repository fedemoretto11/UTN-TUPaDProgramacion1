usuario_correcto = "alumno"
contrasena_correcta = "python123"

intentos = 0
tiene_acceso = False

while (intentos < 3 and not tiene_acceso):
  print(f"Intento numero {intentos + 1} / 3")
  usuario = input("Ingrese el usuario: ")
  contrasena = input("Ingrese la contraseña: ")

  if (usuario == usuario_correcto and contrasena == contrasena_correcta):
    tiene_acceso = True
    print("\nAcceso concedido")
  else:
    print("\nUsuario o contraseña incorrectos")
    intentos += 1




if (not tiene_acceso):
  print("Cuenta bloqueada")
else:
  opcion = ""

  while opcion != "4":
    print("\n1) Ver estado de inscripcion")
    print("2) Cambiar clave")
    print("3) Mostrar mensaje motivacional")
    print("4) Salir")

    opcion = input("Seleccione una opción: ")

    while (not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 4):
      print("Opcion invalida. Seleccione una opción del 1 al 4.")
      opcion = input("Seleccione una opcion: ")

    if opcion == "1":
      print("\nEstado de inscripción: Inscrito")
    elif opcion == "2":
      nueva_contrasena = input("\nIngrese la nueva contrasena: ")
      while len(nueva_contrasena) < 6:
        print("La contrasena debe tener al menos 6 caracteres.")
        nueva_contrasena = input("Ingrese la nueva contraseña: ")
      contrasena_correcta = nueva_contrasena
      print("Contraseña actualizada exitosamente.")
    elif opcion == "3":
      print("\nDale que estas haciendo un gran trabajo, mas programar mejor vas a ser, crack")
    elif opcion == "4":
      print("\nSaliendo del programa...")
