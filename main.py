
from data_base import DataBase
from models_clases.virus import Virus
from models_clases.simulacion import Simulacion
from logic_core.motorSimulacion import MotorSimulacion

def ejecutar_prueba():

    db = DataBase()


    virus_prueba = Virus("COVID-20", "Aéreo", 0.05, 14)

 
    sim_prueba = Simulacion(1000, 10, 5, 50)

    print("--- INICIO ---")
    print(f"Virus: {virus_prueba.nombre}")
    print(f"Población: {sim_prueba.poblacion_total} personas.")
    print("-----------------------------------------------------")

    motor = MotorSimulacion(db, virus_prueba, sim_prueba)

  
    motor.ejecutar_simulacion(limite_seguridad=365)

    print("\n--- SIMULACIÓN COMPLETADA CON ÉXITO ---")
    print("Los datos han sido guardados en 'simulacion_v1.db'.")

if __name__ == "__main__":
    ejecutar_prueba()