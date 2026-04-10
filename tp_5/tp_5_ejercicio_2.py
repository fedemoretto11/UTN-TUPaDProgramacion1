# Ejercicio 2
# Pedir al usuario que cargue 5 productos en una lista.
# Mostrar la lista ordenada alfabeticamente.
# Preguntar que producto desea eliminar y actualizar la lista.
print("Ejercicio 2")
lista_productos = []

for indice in range(5):
    nombre_producto = input(f"Ingrese el producto {indice + 1}: ")
    lista_productos.append(nombre_producto)

productos_ordenados = sorted(lista_productos)
print("Productos ordenados alfabeticamente:")
for producto in productos_ordenados:
    print(producto)

producto_a_eliminar = input("Ingrese el producto que desea eliminar: ")
if producto_a_eliminar in lista_productos:
    lista_productos.remove(producto_a_eliminar)
    print("Producto eliminado.")
else:
    print("El producto no esta en la lista.")

print("Lista actualizada de productos:")
for producto in lista_productos:
    print(producto)
