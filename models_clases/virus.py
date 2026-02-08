
class Virus():
    def __init__ (self, nombre, tipo_transmision, tasa_letalidad, tiempo_recuperacion):
        self.nombre = nombre
        self.tipo_transmision = tipo_transmision
        self.tasa_letalidad = tasa_letalidad
        self.tiempo_recuperacion = tiempo_recuperacion
        
        probabilidades = {
            "Aéreo": 0.80,
            "Respiratorio": 0.30,
            "Contacto Directo": 0.12, 
            "Fómites": 0.10
        }
        
        self.probabilidad_contagio = probabilidades.get(tipo_transmision, 0.0)

