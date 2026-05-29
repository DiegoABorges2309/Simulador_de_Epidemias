from sir import SIR


class SEIR(SIR):
    def __init__(self, _n_personas: int, _infect_inicio: int, _tasa_contagio: float, _tasa_recuperados: float,
                 _tasa_incubacion: float):
        super().__init__(_n_personas, _infect_inicio, _tasa_contagio, _tasa_recuperados)
        self.sigma = _tasa_incubacion
        self.expuestos = 0
        self.personas_totales = self.infectados + self.expuestos + self.infectados + self.recuperados

    def calcular_susceptibles(self) -> float:
        return - ((self.gamma * self.susceptibles * self.infectados) / self.personas_totales)

    def calcular_expuestos(self) -> float:
        return -(self.calcular_susceptibles()) - self.sigma * self.expuestos

    def calcular_infectados(self) -> float:
        return self.sigma * self.expuestos - self.gamma * self.infectados

    def calcular_recuperados(self) -> float:
        return self.gamma * self.infectados

    # =======================================
    #          calculo de personas
    # =======================================

    def calcular_personas_susceptibles(self, _d_tiempo: int) -> int:
        return round(self.susceptibles - (
                (self.gamma * self.susceptibles * self.infectados) / self.personas_totales)) * _d_tiempo

    def calcular_personas_expuestas(self, _d_tiempo: int) -> int:
        d_