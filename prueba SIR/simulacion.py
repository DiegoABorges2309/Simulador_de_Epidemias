from sir import SIR
from seir import SEIR
from poblacion import Poblacion


class Simulacion:
    def __init__(self):
        self.seir = SEIR(15000, 15, 0.18, 0.09, 0.11)

    def iniciar(self):
        for i in range(100):
            dia = i + 1
            d_susceptibles = self.seir.calcular_susceptibles()
            d_expuestos = self.seir.calcular_expuestos()
            d_infectados = self.seir.calcular_infectados()
            d_recuperados = self.seir.calcular_recuperados()

            p_susceptibles = Poblacion.calcular_poblacion_susceptibles(self.seir.susceptibles, d_susceptibles, dia)
            p_expuestos = Poblacion.calcular_poblacion_expuestos(self.seir.expuestos, d_expuestos, dia)
            p_infectados = Poblacion.calcular_poblacion_infectados(self.seir.infectados, d_infectados, dia)
            p_recuperados = Poblacion.calcular_poblacion_recuperados(self.seir.recuperados, d_recuperados, dia)

            self.seir.susceptibles = p_susceptibles
            self.seir.expuestos = p_expuestos
            self.seir.infectados = p_infectados
            self.seir.recuperados = p_recuperados


            print(f"DIA:: {dia}")
            print(f"DETERMINANTES:: S= {d_susceptibles}; E= {d_expuestos}; I= {d_infectados}; R= {d_recuperados}")
            print(f"PERSONAS:: S= {p_susceptibles}; E= {p_expuestos}; I= {p_infectados}; R= {p_recuperados}")
