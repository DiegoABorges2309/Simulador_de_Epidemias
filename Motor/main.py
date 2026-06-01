from motor_simulacion import Motor
from seir_sei.seir import DatosSimulacionHumanos
from seir_sei.sei import DatosSimulacionVector

if __name__ == "__main__":
    datos_h = DatosSimulacionHumanos(0.5, 0.3, 0.2, 0.14)
    datos_v = DatosSimulacionVector(0.5, 0.3, 0.1, 0.07, 0.07)
    engine = Motor(10000, 10, datos_h, 20000, 100, datos_v)
    engine.iniciar_simulacion()
    for indice, content in enumerate(engine.lista_de_dias):
        pass
