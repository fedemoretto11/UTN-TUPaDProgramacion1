#Ejercicio 1
print("Ejercicio 1")
edad_1 = int(input("Ingrese su edad: "))
if edad_1 > 18:
  print("Es mayor de edad")

print("")
print("")

#Ejercicio 2
print("Ejercicio 2")
nota_2 = int(input("Ingrese su nota: "))
if nota_2 > 6:
  print("Aprobado")
else:
  print("Desaprobado")


print("")
print("")

#Ejercicio 3
print("Ejercicio 3")
numero_3 = int(input("Ingrese un numero: "))
numero_valido_3 = numero_3 % 2 == 0
if numero_valido_3:
  print("Ha ingresado un número par")
else:
  print("Por favor, ingrese un número par")

print("")
print("")

#Ejercicio 4
print("Ejercicio 4")
edad_4 = int(input("Ingrese su edad: "))
if edad_4 < 12:
  print("Niño/a")
elif edad_4 >= 12 and edad_4 < 18:
  print("Adolescente")
elif edad_4 >= 18 and edad_4 < 30:
  print("Adulto/a joven")
else:
  print("Adulto")

print("")
print("")

#Ejercicio 5
print("Ejercicio 5")
contrasena_5 = input("Ingrese una contraseña: ")

if 8 <= len(contrasena_5) <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

print("")
print("")

#Ejercicio 6
print("Ejercicio 6")
consumo_6 = float(input("Ingrese el consumo mensual en kWh: "))

if consumo_6 < 150:
    print("Consumo bajo")
elif 150 <= consumo_6 <= 300:
    print("Consumo medio")
else:
    print("Consumo alto")

if consumo_6 > 500:
    print("Considere medidas de ahorro energético")

print("")
print("")

#Ejercicio 7
print("Ejercicio 7")
texto_7 = input("Ingrese una palabra o frase: ")
if texto_7[-1].lower() in "aeiou":
  texto_7 += "!"
print(texto_7)

print("")
print("")

#Ejercicio 8
print("Ejercicio 8")
nombre_8 = input("Ingrese su nombre: ")

print("Seleccione una opción:")
print("1 - Mostrar el nombre en MAYÚSCULAS")
print("2 - Mostrar el nombre en minúsculas")
print("3 - Mostrar el nombre con la primera letra en mayúscula")

opcion_8 = int(input("Ingrese la opción deseada (1, 2 o 3): "))

if opcion_8 == 1:
    print(nombre_8.upper())
elif opcion_8 == 2:
    print(nombre_8.lower())
elif opcion_8 == 3:
    print(nombre_8.title())
else:
    print("Opcion incorrecta")

print("")
print("")

#Ejercicio 9
print("Ejercicio 9")
magnitud_9 = float(input("Ingrese la magnitud del terremoto: "))

if magnitud_9 < 3:
    print("Muy leve (imperceptible)")
elif magnitud_9 < 4:
    print("Leve (ligeramente perceptible)")
elif magnitud_9 < 5:
    print("Moderado (sentido por personas, pero generalmente no causa daños)")
elif magnitud_9 < 6:
    print("Fuerte (puede causar daños en estructuras débiles)")
elif magnitud_9 < 7:
    print("Muy Fuerte (puede causar daños significativos)")
else:
    print("Extremo (puede causar graves daños a gran escala)")

print("")
print("")

#Ejercicio 10
print("Ejercicio 10")
hemisferio_10 = input("Ingrese el hemisferio (N/S): ").upper()
mes_10 = int(input("Ingrese el mes (1 a 12): "))
dia_10 = int(input("Ingrese el día: "))

if (mes_10 == 12 and dia_10 >= 21) or (mes_10 <= 3 and (mes_10 != 3 or dia_10 <= 20)):
    periodo_10 = "invierno_norte"
elif (mes_10 == 3 and dia_10 >= 21) or (mes_10 <= 6 and (mes_10 != 6 or dia_10 <= 20)):
    periodo_10 = "primavera_norte"
elif (mes_10 == 6 and dia_10 >= 21) or (mes_10 <= 9 and (mes_10 != 9 or dia_10 <= 20)):
    periodo_10 = "verano_norte"
else:
    periodo_10 = "otono_norte"

if hemisferio_10 == "N":
    if periodo_10 == "invierno_norte":
        print("Invierno")
    elif periodo_10 == "primavera_norte":
        print("Primavera")
    elif periodo_10 == "verano_norte":
        print("Verano")
    else:
        print("Otoño")
else:
    if periodo_10 == "invierno_norte":
        print("Verano")
    elif periodo_10 == "primavera_norte":
        print("Otoño")
    elif periodo_10 == "verano_norte":
        print("Invierno")
    else:
        print("Primavera")
print("")
print("")

