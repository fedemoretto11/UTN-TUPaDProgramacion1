# Ejercicio 5
# Crear una lista con los nombres de 8 estudiantes presentes en clase.
# Preguntar si se quiere agregar un estudiante o eliminar uno existente.
# Mostrar la lista final actualizada.
print("Ejercicio 5")
estudiantes_presentes = [
    "Federico",
    "Maria",
    "Martin",
    "Rodolfo",
    "Pedro",
    "Lucas",
    "Francisco",
    "Maria del Carmen",
]

accion_usuario = input("Escriba agregar o eliminar: ")

if accion_usuario == "agregar":
    nombre_nuevo = input("Ingrese el nombre del nuevo estudiante: ")
    estudiantes_presentes.append(nombre_nuevo)
    print("Estudiante agregado.")
elif accion_usuario == "eliminar":
    nombre_a_eliminar = input("Ingrese el nombre del estudiante que desea eliminar: ")
    if nombre_a_eliminar in estudiantes_presentes:
        estudiantes_presentes.remove(nombre_a_eliminar)
        print("Estudiante eliminado.")
    else:
        print("El estudiante no esta en la lista.")
else:
    print("La opcion ingresada no es valida.")

print("Lista final de estudiantes:")
for estudiante in estudiantes_presentes:
    print(estudiante)
