class Cliente:
    def __init__(self, nombre, id, direccion):
        self.nombre = nombre
        self.id = id
        self.direccion = direccion

    def obtenerNombre(self):
        return self.nombre

    def obtenerDireccion(self):
        return self.direccion

    def obtener_id(self):
        return self.id
