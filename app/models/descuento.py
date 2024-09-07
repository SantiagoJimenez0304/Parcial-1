class Descuento:
    def __init__(self, porcentaje, cantidad_minima):
        self.porcentaje = porcentaje
        self.cantidad_minima = cantidad_minima

    def obtenerPorcentaje(self):
        return self.porcentaje

    def asignarCantidadMinima(self, cantidad_minima):
        self.cantidad_minima = cantidad_minima
