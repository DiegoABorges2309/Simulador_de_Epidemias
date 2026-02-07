
class Virus ():
    def __init__ (self, nombre, tasa_letalidad, tiempo_recuperacion, tipo_transmision):
        self.nombre = nombre
        self.tipo_transmision = tipo_transmision
        self.tasa_letalidad = tasa_letalidad
        self.tiempo_recuperacion = tiempo_recuperacion
        
        probabilidades = {
            "Aérea": 0.80,
            "Respiratoria": 0.30,
            "Contacto Directo": 0.12, 
            "Fómites": 0.10
        }
        
        self.probabilidad_contagio = probabilidades.get(tipo_transmision, 0.0)

