from lente import Lente

# Creamos dos objetos de la clase Lente
lente1 = Lente(10000, "Marca1", "Formula1")
lente2 = Lente(15000, "Marca2", "Formula2")

# Probamos el método calcular_precio_venta
print(f"Precio de venta del lente1: {lente1.calcular_precio_venta()}")
print(f"Precio de venta del lente2: {lente2.calcular_precio_venta()}")

# Probamos el método __str__
print(f"Información del lente1: {str(lente1)}")
print(f"Información del lente2: {str(lente2)}")

# Probamos el método __eq__
if lente1 == lente2:
    print("Los lentes son iguales")
else:
    print("Los lentes son diferentes")

lente3 = Lente(100, "Marca1", "Formula1")
if lente1 == lente3:
    print("Los lentes son iguales")
else:
    print("Los lentes son diferentes")

# Probamos el método __add__
precio_total = lente1 + lente2
print(f"Precio total de venta de los dos lentes: {precio_total}")