class Estado:
    def __init__(self, ubicaciones):
        self.ubicaciones = ubicaciones

class Accion:
    def __init__(self, nombre, precondiciones, efectos):
        self.nombre = nombre
        self.precondiciones = precondiciones
        self.efectos = efectos


estado_inicial = Estado(ubicaciones={'bloque': 'A'})

estado_objetivo = Estado(ubicaciones={'bloque': 'B'})
