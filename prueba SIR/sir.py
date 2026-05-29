from abc import ABC, abstractmethod


class SIR(ABC):
    def __init__(self, _n_personas: int, _infect_inicio: int, _tasa_contagio: float, _tasa_recuperados: float):
        self.susceptibles = _n_personas - _infect_inicio
        self.infectados = _infect_inicio
        self.recuperados = 0
        self.beta = _tasa_contagio
        self.gamma = _tasa_recuperados

    @abstractmethod
    def calcular_susceptibles(self) -> float:
        pass

    @abstractmethod
    def calcular_infectados(self) -> float:
        pass

    @abstractmethod
    def calcular_recuperados(self) -> float:
        pass
