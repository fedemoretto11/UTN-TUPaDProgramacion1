nombre_cliente = input("Ingrese el nombre del cliente: ")
while (not nombre_cliente.isalpha()):
  nombre_cliente = input("Ingrese un nombre valido: ")

cantidad_productos_comprar = input("Ingrese la cantidad de productos a comprar: ")
while (not cantidad_productos_comprar.isdigit() or int(cantidad_productos_comprar) < 0):
  cantidad_productos_comprar = input("Ingrese la cantidad correcta: ")

cantidad_productos_comprar = int(cantidad_productos_comprar)

total_sin_descuento = 0
total_con_descuento = 0

for i in range(cantidad_productos_comprar):
  print(f"\n--- Producto n° {i + 1} ---")

  precio_producto = input("Ingrese el precio del producto: ")
  while (not precio_producto.isdigit()):
    precio_producto = input("Ingrese un precio valido: ")

  precio_producto = int(precio_producto)
  
  total_sin_descuento += precio_producto

  tiene_descuento = input("Tiene descuento? (S/N): ").lower()
  while (tiene_descuento != "s" and tiene_descuento != "n"):
    tiene_descuento = input("TIngrese S o N: ").lower()
  
  if (tiene_descuento == "s"):
    precio_con_descuento = precio_producto * 0.9

  else:
    precio_con_descuento = precio_producto

  total_con_descuento += precio_con_descuento

ahorro = total_sin_descuento - total_con_descuento
promedio = total_con_descuento / cantidad_productos_comprar

print("\n----- RESUMEN DE LA COMPRA -----")
print(f"Cliente: {nombre_cliente}")
print(f"Total sin descuentos: ${total_sin_descuento:.2f}")
print(f"Total con descuentos: ${total_con_descuento:.2f}")
print(f"Ahorro total: ${ahorro:.2f}")
print(f"Promedio por producto: ${promedio:.2f}")