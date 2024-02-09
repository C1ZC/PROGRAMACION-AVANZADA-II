class Lente:
    def __init__(self, precio_costo, marca, formula_recomendada):
        self.precio_costo = precio_costo
        self.marca = marca
        self.formula_recomendada = formula_recomendada
    
    def calcular_precio_venta(self):
        # Calculamos el precio de venta sumando un margen de ganancia al precio de costo
        margen_ganancia = 0.3 # 30% de margen de ganancia
        precio_venta = self.precio_costo * (1 + margen_ganancia)
        
        return precio_venta
    
    def __str__(self):
        # Devolvemos una cadena con la información del lente
        return f"Lente de la marca {self.marca}, fórmula recomendada {self.formula_recomendada}, precio de costo {self.precio_costo}"
    
    def __eq__(self, other):
        # Comparamos dos lentes por su precio de costo, marca y fórmula recomendada
        if isinstance(other, Lente):
            return (self.precio_costo == other.precio_costo and
                    self.marca == other.marca and
                    self.formula_recomendada == other.formula_recomendada)
        return False
    
    def __add__(self, other):
        # Sumamos el precio de dos lentes para obtener el precio total de venta
        if isinstance(other, Lente):
            precio_total = self.calcular_precio_venta() + other.calcular_precio_venta()
            return precio_total
        raise TypeError("No se puede sumar un lente con un objeto de otro tipo")
