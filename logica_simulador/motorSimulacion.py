import random
from models_clases.paciente import Paciente
from models_clases.virus import Virus
from models_clases.simulacion import Simulacion
from logic_core.estructuras import ColaHospital

class MotorSimulacion:
    def __init__(self, db, virus_obj, simulacion_obj):
        self.db = db
        self.virus = virus_obj
        self.simulacion = simulacion_obj
        self.poblacion = [Paciente(id_paciente=i) for i in range(self.simulacion.poblacion_total)]
        self.cola_hospital = ColaHospital()
        self.densidad = self.simulacion.poblacion_total / self.simulacion.area_km2
        self.resultados = [0,0,0,0,0,0,0]
        self.estado = ["sanos", "infectados", "recuperados", "fallecidos", "espera"]

        self.limites = {
            "Aéreo": 2.5,
            "Respiratorio": 2.0,
            "Contacto Directo": 1.2,
            "Fómites": 1.5,
        }        
        tope = self.limites.get(self.virus.tipo_transmision, 1.5)
        self.factor_densidad = min(tope, max(1.0, self.densidad / 50)) 
        self.id_simulacion = self.db.insertar_simulacion(self.virus, self.simulacion)

    def iniciar_epidemia(self):
        if self.simulacion.cant_contagio_inicial > len(self.poblacion):
            self.simulacion.cant_contagio_inicial = len(self.poblacion)
        iniciales = random.sample(self.poblacion, self.simulacion.cant_contagio_inicial)
        for p in iniciales:
            p.infectar(0)

    def mostrar_resultados(self):
        for i in range(len(self.estado)):
            print(f"{self.estado[i]}::{self.resultados[i]}")

    def ejecutar_simulacion(self, limite_seguridad=None):
        self.iniciar_epidemia()
        dia = 0
        conteo = None
        while True:
            if conteo is not None:
                for i in range(len(self.estado)):
                    self.resultados[i] = +conteo[self.estado[i]]
            conteo = {"sanos": 0, "infectados": 0, "recuperados": 0, "fallecidos": 0, "espera": 0}

            infectados_activos = [p for p in self.poblacion if p.estado == "Infectado"]
            
            for p in infectados_activos:
                p.dias_enfermo += 1
                if p.dias_enfermo >= self.virus.tiempo_recuperacion:
                    p.estado = "Recuperado"
                    p.en_hospital = False
                    continue
                riesgo_base = self.virus.tasa_letalidad
                modificador = 0.5 if p.en_hospital else 1.5
                if random.random() < (riesgo_base * modificador):
                    p.estado = "Fallecido"
                    p.en_hospital = False 
                    continue
            
            self.cola_hospital.quitar_fallecidos()

            sanos = [p for p in self.poblacion if p.estado == "Sano"]
            if len(infectados_activos) > 0 and len(sanos) > 0:
                tasa_dinamica = (len(infectados_activos) / len(self.poblacion)) * \
                                self.virus.probabilidad_contagio * self.factor_densidad
                for p in sanos:
                    if random.random() < tasa_dinamica:
                        p.infectar(dia)

            pacientes_en_cama = [p for p in self.poblacion if p.en_hospital]
            camas_libres = self.simulacion.capacidad_hospitalaria - len(pacientes_en_cama)
            while camas_libres > 0 and not self.cola_hospital.esta_vacia():
                self.cola_hospital.paciente_atendido(dia)
                camas_libres -= 1
            
            recien_infectados = [p for p in self.poblacion if p.estado == "Infectado" and not p.en_hospital and p.dia_ingreso_cola is None]
            for p in recien_infectados:
                if camas_libres > 0:
                    p.en_hospital = True
                    p.dia_atencion = dia
                    camas_libres -= 1
                else:
                    self.cola_hospital.agregar_paciente(p, dia)
            for p in self.poblacion:
                if p.estado == "Sano": conteo["sanos"] += 1
                elif p.estado == "Infectado": conteo["infectados"] += 1
                elif p.estado == "Recuperado": conteo["recuperados"] += 1
                elif p.estado == "Fallecido": conteo["fallecidos"] += 1
            
            conteo["espera"] = self.cola_hospital.tamano_cola()
            conteo["numero_dia"] = dia
            print(conteo["numero_dia"])
            self.db.insertar_dia(self.id_simulacion, conteo)

            if len([p for p in self.poblacion if p.estado == "Infectado"]) == 0:
                print(f"--- Simulación finalizada el día {dia}: El virus se extinguió ---")
                break
            dia += 1
        self.resultados[5] = self.limites[self.virus.tipo_transmision]
        self.resultados[6]=dia
        self.registrar_pacientes_hospitalizados()
        return self.resultados

    def registrar_pacientes_hospitalizados(self):
        for p in self.poblacion:
            if p.dia_ingreso_cola is not None or p.en_hospital or p.dia_atencion is not None:
                self.db.insertar_paciente_final(self.id_simulacion, p)
        print("Datos de hospitalización guardados con éxito.")