
class Paciente():
    def __init__(self, id_paciente, estado="Sano"):
        self.id = id_paciente
        self.estado = estado
        self.dia_contagio = None
        self.dia_ingreso_cola = None
        self.dia_atencion = None
        self.dias_enfermo = 0

