class Aluminio:
    def __init__(self, tipo_acabado, costo_cm_lineal):
        self.tipo_acabado = tipo_acabado
        self.costo_cm_lineal = costo_cm_lineal

    def obtenerTipoAcabado(self):
        return self.tipo_acabado

    def obtenerCostoCmLineal(self):
        return self.costo_cm_lineal
