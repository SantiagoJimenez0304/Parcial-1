class Ventana:
    def __init__(self, estilo, ancho, alto):
        self.estilo = estilo
        self.ancho = ancho
        self.alto = alto

    def obtenerEstilo(self):
        return self.estilo

    def obtenerAncho(self):
        return self.ancho

    def obtenerAlto(self):
        return self.alto
