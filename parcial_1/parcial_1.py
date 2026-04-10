# inicializacion de variables
lista_herramientas = []
lista_existencias = []
opcion_menu = ""

while opcion_menu != "8":
  print("\n--- Menu de la Ferreteria Local ---\n")
  print("1. Carga inicial de las herramientas")
  print("2. Carga de existencias")
  print("3. Visualizacion de inventario")
  print("4. Consulta de Stock (existencias)")
  print("5. Reporte de Agotados")
  print("6. Alta de Nuevo Producto")
  print("7. Actualización de Stock (Venta/Ingreso)")
  print("8. Salir")
  print("\n-----------------------------------")
  print("")
  print("")

  opcion_menu = input("Ingrese su opcion: ")
  while not opcion_menu.isdigit() or int(opcion_menu) < 1 or int(opcion_menu) > 8:
    print("Opcion invalida. Por favor ingrese un número del 1 al 8.")
    opcion_menu = input("Ingrese su opción: ")

  if opcion_menu == "1":
    print("\n--- Carga inicial de las herramientas ---")
    cantidad_herramientas = input("Ingrese la cantidad de herramientas a cargar: ")

    while not cantidad_herramientas.isdigit() or int(cantidad_herramientas) <= 0:
      print("Cantidad invalida. Por favor ingrese un numero entero positivo.")
      cantidad_herramientas = input("Ingrese la cantidad de herramientas a cargar: ")
    
    cantidad_herramientas = int(cantidad_herramientas)

    for i in range(cantidad_herramientas):
      herramienta = input(f"Ingrese el nombre de la herramienta {i+1}: ")

      while not herramienta.isalpha() or herramienta == "":
        print("Nombre de herramienta incorrecto. Por favor ingrese un nombre valido.")
        herramienta = input(f"Ingrese el nombre de la herramienta {i+1}: ")

      lista_herramientas.append(herramienta)
      lista_existencias.append(0)
    print("Carga inicial de herramientas completada.")
  elif opcion_menu == "2":
    print("\n--- Carga de existencias ---")
    if len(lista_herramientas) == 0:
      print("No hay herramientas cargadas. Por favor realice la carga inicial primero.")
    else:
      for i in range(len(lista_herramientas)):
        print(f"{i+1}. {lista_herramientas[i]} - Existencias actuales: {lista_existencias[i]}")
    
        cantidad_cargar = input(f"Ingrese la cantidad de existencias a cargar para {lista_herramientas[i]}: ")

        while not cantidad_cargar.isdigit() or int(cantidad_cargar) <= 0:
          print("Cantidad invalida. Por favor ingrese un numero entero positivo.")
          cantidad_cargar = input(f"Ingrese la cantidad de existencias a cargar para {lista_herramientas[i]}: ")
        
        lista_existencias[i] += int(cantidad_cargar)
        print(f"Existencias actualizadas para {lista_herramientas[i]}. Nueva cantidad: {lista_existencias[i]}")
  elif opcion_menu == "3":
    print("\n--- Visualizacion de inventario ---")
    if len(lista_herramientas) == 0:
      print("No hay herramientas cargadas. Por favor realice la carga inicial primero.")
    else:
      print("Inventario actual:")
      for i in range(len(lista_herramientas)):
        print(f"{i+1}. {lista_herramientas[i]} - Existencias: {lista_existencias[i]}")
  elif opcion_menu == "4":
    print("\n--- Consulta de Stock (existencias) ---")
    if len(lista_herramientas) == 0:
      print("No hay herramientas cargadas. Por favor realice la carga inicial primero.")
    else:
      nombre_herramienta = input("Ingrese el nombre de la herramienta para consultar su stock: ")
      if nombre_herramienta in lista_herramientas:
        index = lista_herramientas.index(nombre_herramienta)
        print(f"Stock disponible para {lista_herramientas[index]}: {lista_existencias[index]}")
      else:
        print("Herramienta no encontrada.")
  elif opcion_menu == "5":
    print("\n--- Reporte de Agotados ---")
    if len(lista_herramientas) == 0:
      print("No hay herramientas cargadas. Por favor realice la carga inicial primero.")
    else:
      agotados = False
      for i in range(len(lista_herramientas)):
        if lista_existencias[i] == 0:
          print(f"{lista_herramientas[i]} - Agotado")
          agotados = True
      if not agotados:
        print("No hay herramientas agotadas.")
  elif opcion_menu == "6":
    print("\n--- Alta de Nuevo Producto ---")
    nuevo_producto = input("Ingrese el nombre del nuevo producto: ")

    while not nuevo_producto.isalpha() or nuevo_producto == "":
      print("Nombre de producto incorrecto. Por favor ingrese un nombre valido.")
      nuevo_producto = input("Ingrese el nombre del nuevo producto: ")

    if nuevo_producto in lista_herramientas:
      print("El producto ya existe en el inventario.")
    else:
      lista_herramientas.append(nuevo_producto)
      print("Ingrese la cantidad inicial de existencias para el nuevo producto:")
      cantidad_inicial = input()
      while not cantidad_inicial.isdigit() or int(cantidad_inicial) < 0:
        print("Cantidad invalida. Por favor ingrese un numero entero no negativo.")
        cantidad_inicial = input()
      lista_existencias.append(int(cantidad_inicial))
      print(f"Nuevo producto '{nuevo_producto}' agregado al inventario con existencias iniciales de {cantidad_inicial}.")
  elif opcion_menu == "7":
    print("\n--- Actualización de Stock (Venta/Ingreso) ---")
    if len(lista_herramientas) == 0:
      print("No hay herramientas cargadas. Por favor realice la carga inicial primero.")
    else:
      nombre_producto = input("Ingrese el nombre del producto para actualizar su stock: ")
      if nombre_producto in lista_herramientas:
        index = lista_herramientas.index(nombre_producto)
        print(f"Stock actual para {lista_herramientas[index]}: {lista_existencias[index]}")
        tipo_actualizacion = input("¿Desea realizar una venta o un ingreso? (venta/ingreso): ")

        while tipo_actualizacion.lower() not in ["venta", "ingreso"]:
          print("Opción inválida. Por favor ingrese 'venta' o 'ingreso'.")
          tipo_actualizacion = input("¿Desea realizar una venta o un ingreso? (venta/ingreso): ")

        cantidad_actualizar = input("Ingrese la cantidad a actualizar: ")

        while not cantidad_actualizar.isdigit() or int(cantidad_actualizar) <= 0:
          print("Cantidad invalida. Por favor ingrese un numero entero positivo.")
          cantidad_actualizar = input("Ingrese la cantidad a actualizar: ")

        cantidad_actualizar = int(cantidad_actualizar)

        if tipo_actualizacion.lower() == "venta":
          if cantidad_actualizar > lista_existencias[index]:
            print("No hay suficiente stock para realizar la venta.")
          else:
            lista_existencias[index] -= cantidad_actualizar
            print(f"Venta realizada. Nuevo stock para {lista_herramientas[index]}: {lista_existencias[index]}")
        else:
          lista_existencias[index] += cantidad_actualizar
          print(f"Ingreso realizado. Nuevo stock para {lista_herramientas[index]}: {lista_existencias[index]}")
      else:
        print("Producto no encontrado.")