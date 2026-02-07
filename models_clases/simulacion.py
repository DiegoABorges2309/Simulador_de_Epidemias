
class Simulacion():
    def __init__(self, poblacion_total, cant_contagio_inicial, area_km2, capacidad_hospitalaria):
        self.poblacion_total = poblacion_total
        self.cant_contagio_inicial = cant_contagio_inicial
        self.area_km2 = area_km2
        self.capacidad_hospitalaria = capacidad_hospitalaria
        self.id_simulacion = None
        