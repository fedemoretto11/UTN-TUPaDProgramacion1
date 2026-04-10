# Ejercicio 10
# Una tienda registra las ventas de 4 productos durante 7 dias en una matriz de 4x7.
# Mostrar el total vendido por cada producto.
# Mostrar el dia con mayores ventas totales.
# Indicar cual fue el producto mas vendido en la semana.
print("Ejercicio 10")
ventas_semanales = [
    [10, 15, 20, 25, 30, 35, 40],
    [5, 10, 15, 20, 25, 30, 35],
    [8, 12, 18, 22, 28, 32, 38],
    [3, 6, 9, 12, 15, 18, 21],
]

for indice_producto in range(len(ventas_semanales)):
    total_producto = sum(ventas_semanales[indice_producto])
    print("Total vendido del producto", indice_producto + 1, ":", total_producto)

ventas_por_dia = []
for indice_dia in range(len(ventas_semanales[0])):
    total_dia = 0
    for indice_producto in range(len(ventas_semanales)):
        total_dia += ventas_semanales[indice_producto][indice_dia]
    ventas_por_dia.append(total_dia)

dia_con_mas_ventas = ventas_por_dia.index(max(ventas_por_dia)) + 1
print("Dia con mayores ventas totales:", dia_con_mas_ventas)

totales_por_producto = []
for fila_ventas in ventas_semanales:
    totales_por_producto.append(sum(fila_ventas))

producto_mas_vendido = totales_por_producto.index(max(totales_por_producto)) + 1
print("Producto mas vendido en la semana:", producto_mas_vendido)
