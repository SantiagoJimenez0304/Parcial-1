class Cotizacion:
    def __init__(self, cliente_id, ventana_id, cantidad, descuento_id, total):
        self.cliente_id = cliente_id
        self.ventana_id = ventana_id
        self.cantidad = cantidad
        self.descuento_id = descuento_id
        self.total = total

    def obtenerCliente(self):
        return self.cliente_id

    def obtenerVentana(self):
        return self.ventana_id

    def obtenerCantidad(self):
        return self.cantidad

    def obtenerDescuento(self):
        return self.descuento_id

    def obtenerTotal(self):
        return self.total
