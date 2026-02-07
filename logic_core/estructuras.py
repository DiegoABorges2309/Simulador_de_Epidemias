class Cola_Gestion_Hospitalaria():
    #hola
    def __init__(self):
        self.cola_pacientes = []
        
    def agregar_paciente(self, paciente):
        self.cola_pacientes.append(paciente)
    
    def paciente_atendido(self):
        if not self.esta_vacia():
            return self.cola_pacientes.pop(0)
            
        return None
    
    def esta_vacia(self):
        return len(self.cola_pacientes) == 0
    
    def tamano_cola(self):
        return len(self.cola_pacientes)
    


class Pila_Historial():
    def __init__(self):
        self.__historial = []
    
    def agregar_historial(self, simulacion):
        self.__historial.append(simulacion)
        
    def eliminar_historial(self):
        if not self.esta_vacia():
            self.__historial.pop()
        
        return None
    
    def mostar_tope(self):
        if not self.esta_vacia():
            return self.__historial[-1]
        return None
    
    def esta_vacia(self):
        return len(self.__historial) == 0
    
    def tamano_pila(self):
        return len(self.__historial)
    
    