class Vidrio:
    def __init__(self, tipo, esmerilado, costo_cm2):
        self.tipo = tipo
        self.esmerilado = esmerilado
        self.costo_cm2 = costo_cm2

    def asignarTipo(self, tipo):
        self.tipo = tipo

    def asignarCostocm2(self, costo_cm2):
        self.costo_cm2 = costo_cm2
