energia = 100
tiempo = 12
cerradura_abiertas = 0
alarma = False
codigo_parcial = ""

forzar_seguidos = 0
bloqueado = False

agente = input("Ingrese el nombre del agente: ")
while not agente.isalpha() or agente == "":
    print("Nombre incorrecto")
    agente = input("Ingrese el nombre del agente: ")

print(f"\nAgente {agente} ha ingresado al sistema")

while energia > 0 and tiempo > 0 and cerradura_abiertas < 3 and not bloqueado:
  print("\n--- MENU ---")
  print("1. Forzar cerradura")
  print("2. Hackear panel")
  print("3. Descanasar")

  opcion = input("Seleccione una opcion: ")
  while not opcion.isdigit() or int(opcion) < 1 or int(opcion) > 3:
    print("Opcion incorrecta")
    opcion = input("Seleccione una opcion: ")

  if opcion == "1":
    forzar_seguidos += 1
    energia -= 20
    tiempo -= 2
    if forzar_seguidos == 3:
      alarma = True
      print("Cerradura bloqueada por forzar 3 veces seguidas. Alarma activada")
    else:
      if energia < 40:
        riesgo = input("Energía baja. Elija un numero del 1 al 3: ")

        while not riesgo.isdigit():
            riesgo = input("Numero incorrecto, ingrese un numero del 1 al 3: ")

        while int(riesgo) < 1 or int(riesgo) > 3:
            riesgo = input("Numero incorrecto, ingrese un numero del 1 al 3: ")
            while not riesgo.isdigit():
                riesgo = input("Numero incorrecto, ingrese un numero del 1 al 3: ")

        if riesgo == "3":
            alarma = True
            print("Alarma activada")

    if not alarma:
      cerradura_abiertas += 1
      print(f"Cerradura abierta! Cerraduras abiertas: {cerradura_abiertas}")
    else:
      bloqueado = True
      print("Agente bloqueado por alarma activada")
  elif opcion == "2":
    forzar_seguidos = 0
    energia -= 10
    tiempo -= 3
    print("Hackeando panel...")

    for i in range(1, 5):
      codigo_parcial += "F"
      print(f"Paso {i}/4 - Código parcial: {codigo_parcial}")
    
    if len(codigo_parcial) >= 8 and cerradura_abiertas < 3:
      cerradura_abiertas += 1
      print(f"Se abrio una cerradura! Cerraduras abiertas: {cerradura_abiertas}")
  elif opcion == "3":
    forzar_seguidos = 0
    energia += 15
    if energia > 100:
      energia = 100
    tiempo -= 1
    if alarma:
      print("Descansando con la alarma activada")
      energia -= 10
    print("Descansando...")
  
  if alarma and tiempo <= 3 and cerradura_abiertas < 3:
    bloqueado = True

print("\n--- RESULTADO FINAL ---")
if cerradura_abiertas == 3:
  print(f"Felicidades, agente {agente}! Has abierto las 3 cerraduras")
elif bloqueado:
  print(f"Agente {agente} ha sido bloqueado por la alarma activada")
elif energia <= 0 or tiempo <= 0:
  print(f"Agente {agente} no ha logrado abrir las 3 por falta de tiempo o energia")

