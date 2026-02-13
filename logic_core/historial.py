class PilaHistorial():
    def __init__(self):
        self.historial_estados = []

    def apilar_estado(self, _data):
        self.historial_estados.append(_data)

    def deshacer_y_mostrar(self):

        if self.esta_vacia():
            print("(!) No hay estados anteriores para retroceder")
            return None
        
        estado_restaurado = self.historial_estados.pop()
        
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
    
    

