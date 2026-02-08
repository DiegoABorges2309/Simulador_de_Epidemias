
from models_clases.paciente import Paciente


class ColaHospital():
    def __init__(self):
        self.cola_pacientes = []
        
    def agregar_paciente(self, paciente, dia_actual):
        if paciente.estado == "Infectado":
            
            paciente.dia_ingreso_cola = dia_actual
            self.cola_pacientes.append(paciente)
        
    
    def paciente_atendido(self, dia_actual):
        if not self.esta_vacia():
            paciente = self.cola_pacientes.pop(0)
            paciente.dia_atencion = dia_actual
            paciente.en_hospital = True
            return paciente
        return None
            
    
    
    def esta_vacia(self):
        return len(self.cola_pacientes) == 0
    
    def quitar_fallecidos(self):
        self.cola_pacientes = [p for p in self.cola_pacientes if p.estado != "Fallecido" ]
    
    def tamano_cola(self):
        return len(self.cola_pacientes)
    
    
    

