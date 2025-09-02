from funcion import (
	cal_subtotal,
	cal_cantidad,
	cal_iva,
	cal_total,
	iva_producto
)
from diccionario import productos
from tuplas import get_article

iva = 0.19


nombre = input("Ingrese su nombre: ")


tuplas = get_article(productos)


print("Productos disponibles:")
for i, (prod, precio) in enumerate(tuplas, 1):
	print(f"{i}. {prod} - ${precio}")

seleccion = input("Ingrese los números de los productos que desea (separados por coma): ")
indices = [int(x.strip()) for x in seleccion.split(",")]

productos = []
precios = []
for idx in indices:
	prod, precio = tuplas[idx - 1]
	productos.append(prod)
	precios.append(precio)


print("*****")
print("Super Mercado")
print("Cra 17b 43 7c")
print("NIT: 1234567891234")
print("*****")
print(f"Factura para: {nombre}")
print("Producto  | Precio")
for prod, precio in zip(productos, precios):
	print(f"{prod}  |  {precio}")

print("*****")

subtotal = cal_subtotal(precios)
iva_total = cal_iva(subtotal, iva)
total = cal_total(subtotal, iva_total)

print("Subtotal:", subtotal)
print("IVA:", iva_total)
print("Total:", total)
print("*****")

ivas_prod = iva_producto(precios, iva)
for prod, iva_p in zip(productos, ivas_prod):
	print(f"IVA de {prod}: {iva_p}")