
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
    
class PilaHistorial():
    def __init__(self):
        self.historial_estados = []

    def apilar_estado(self, dia, poblacion, infectados, recuperados, fallecidos, tipo_transmision, area):
      
        estado = {
            "dia": dia,
            "poblacion_total": poblacion,
            "infectados": infectados,
            "recuperados": recuperados,
            "fallecidos": fallecidos,
            "tipo_transmision": tipo_transmision,
            "area": area
        }
        self.historial_estados.append(estado)
        print(f"[DEBUG] Estado del día {dia} guardado en la pila")

    def deshacer_y_mostrar(self):

        if self.esta_vacia():
            print("(!) No hay estados anteriores para retroceder")
            return None
        
        estado_restaurado = self.historial_estados.pop()
        
      
        
        self._imprimir_resumen(estado_restaurado)
        
        return estado_restaurado

    def _imprimir_resumen(self, estado):
    
        print("\n" + "="*50)
        print(f"DÍA {estado['dia']}")
        print("="*50)
        print(f"Población Total: {estado['poblacion_total']}")
        print(f"Tipo Transmisión: {estado['tipo_transmision']}")
        print(f"n Área Geográfica: {estado['area']} km²")
        print("-" * 20)
        print(f"Infectados: {estado['infectados']}")
        print(f"Fallecidos: {estado['fallecidos']}")
        print(f" Recuperados: {estado['recuperados']}")
        print("="*50 + "\n")

    def esta_vacia(self):
        return len(self.historial_estados) == 0

    def ver_tope(self):
        if not self.esta_vacia():
            return self.historial_estados[-1]
        return None
    
    

