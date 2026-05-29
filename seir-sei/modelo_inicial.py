"""
Archivo inicial donde se encuentra la logica inicial
del modelo SEIR-SEI que usamos, aqui se encuentran
las clases padres del modelo.
"""

from abc import ABC, abstractmethod


class DatosSimulacion(ABC):
    """
    Clase inicial de datos necesarios para los modelos,
    esta clase cumple como funcion almacenar los valores
    que seran usados para calcular las ecuaciones
    """

    def __init__(
        self, _tasa_picaduras: float, _tasa_transmision: float, _tasa_incubacion: float
    ):
        """
        Inicializa los datos necesarios para la simualcion

        Parameters
        ----------
        _tasa_picaduras
            Representa el promedio de picaduras que puede realizar un mosquito por dia.
        _tasa_transmision
            Representa la tasa que tiene el dengue en infectar a un vector
            o persona despues de una picadura.
        _tasa_incubacion
            Representa el tiempo que tarda el dengue en ser infeccioso dentro
            del huesped (humano o vector).
        """
        self.fuerza_infeccion = _tasa_picaduras * _tasa_transmision
        self.tasa_incubacion = _tasa_incubacion


class ModeloInicial(ABC):
    """
    Clase padre para los modelos SEIR-SEI el cual
    establece variables que comparten entre si.
    """

    def __init__(self, _n_poblacion: int, _n_infectados_inicio: int, _datos_simulacion):
        """
        Inicializa los datos necesarios para el modelo SEIR-SEI

        Parameters
        ----------
        _n_poblacion
            Representa el numero inicial que se tomara para la simualacion
            tanto para humano y vector.
        _n_infectados_inicio
            Representa el numero inicial de infectados que se tomara
            para la simualcion tanto para humano y vector.
        _datos_simulacion
            Representa un objeto de la clase 'DatosSimulacion' el
            cual se tomara para extraer los datos para las ecuaciones.
        """
        self.susceptibles = _n_poblacion - _n_infectados_inicio
        self.expuestos = 0
        self.infectados = _n_infectados_inicio
        self.datos_simulacion = _datos_simulacion

    @abstractmethod
    def get_poblacion_total(self) -> float:
        """
        Calculo de la poblacion total de humanos o vectores
        mientras corre la simulacion.
        """
        pass

    @abstractmethod
    def calcular_susceptibles(self, kwargs) -> float:
        """
        Funcion abstracta del calculo de la ecuacion
        de los susceptibles.
        """
        pass

    @abstractmethod
    def calcular_expuestos(self, kwargs) -> float:
        """
        Funcion abstracta del calculo de la ecuacion
        de los expuestos.
        """
        pass

    @abstractmethod
    def calcular_infectados(self) -> float:
        """
        Funcion abstracta del calculo de la ecuacion
        de los infectados
        """
        pass
