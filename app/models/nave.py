class Nave:
    def __init__(self, ventana_id, tipo, ancho, alto, vidrio_id, aluminio_id):
        self.ventana_id = ventana_id
        self.tipo = tipo
        self.ancho = ancho
        self.alto = alto
        self.vidrio_id = vidrio_id
        self.aluminio_id = aluminio_id

    def obtenerVentanaId(self):
        return self.ventana_id

    def obtenerAncho(self):
        return self.ancho

    def obtenerAlto(self):
        return self.alto

    def obtenerAluminioId(self):
        return self.aluminio_id
