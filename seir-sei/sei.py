"""
Definicion del modelo SEI para vectores
como tambien de su propia clase de datos
de la simulacion.
"""

from modelo_inicial import ModeloInicial, DatosSimulacion


class DatosSimulacionVector(DatosSimulacion):
    """
    Clase de datos propia y explusiva para el modelo
    SEI (vector).

    Hereda de la clase 'DatosSimulacion' del archivo
    'modelo_inicial.py'.
    """

    def __init__(
        self,
        _tasa_picaduras: float,
        _tasa_transmision: float,
        _tasa_incubacion: float,
        _tasa_nacimiento_vector: float,
        _tasa_muerte_vector: float,
    ):
        """
        Inicializa los datos necesarios del modelo SEI para la simualcion

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
        _tasa_nacimiento_vector
            Representa el porcentaje de nacimientos del vector
            respecto a la cantidad de poblacion de este mismo.
        _tasa_muerte_vector
            Representa el porcentaje de muertes del vector con
            respecto a la cantidad de poblacion de este mismo.
        """
        super().__init__(_tasa_picaduras, _tasa_transmision, _tasa_incubacion)
        self.tasa_nacimiento = _tasa_nacimiento_vector
        self.tasa_muerte = _tasa_muerte_vector


class Sei(ModeloInicial):
    """
    Clase del modelo SEI (vector) el cual ejecuta
    los calculos necesarios para la simualcion por
    parte del vector.

    Hereda de la clase 'ModeloInicial' del archivo
    'modelo_inicial.py'.
    """

    def __init__(
        self,
        _n_poblacion: int,
        _n_infectados_inicio: int,
        _datos_simulacion: DatosSimulacionVector,
    ):
        """
        Inicializa los datos necesarios para la simulacion del
        modelo SEI.

        Parameters
        ----------
        _n_poblacion
            Representa el numero inicial de la poblacion total
            de vectores.
        _n_infectados_inicio
            Representa el numero inicial de infectados
            de vectores.
        _datos_simulacion
            Representa un objeto de la clase 'DatosSimulacionVector'
            el cual contiene datos importantes para los calculos.
        """
        super().__init__(_n_poblacion, _n_infectados_inicio, _datos_simulacion)

    def get_poblacion_total(self) -> float:
        """
        Calcula el numero total de la poblacion en la simulacion
        en tiempo de ejecucion.

        Returns
        -------
            Retorna la suma de susceptibles, expuestos y infectados
            lo cual representa la poblacion total del vector.
        """
        return self.susceptibles + self.expuestos + self.infectados

    def calcular_susceptibles(
        self, _n_infectados_h: float, _n_poblacion_h: float
    ) -> float:
        """
        Funcion la cual resuelve la ecuacion de susceptibles(vector)

        Parameters
        ----------
        _n_infectados_h
            Representa el numero de infectados por parte de los humanos.
        _n_poblacion_h
            Representa el numero total de la poblacion de los humanos.

        Returns
        -------
            Retorna la derivada de susceptibles respecto al tiempo (dSv/dt).
        """
        n_nacimientos = (
            self.datos_simulacion.tasa_nacimiento * self.get_poblacion_total()
        )
        return (
            n_nacimientos
            - self.datos_simulacion.fuerza_infeccion
            * (_n_infectados_h / _n_poblacion_h)
            * self.susceptibles
            - self.datos_simulacion.tasa_muerte * self.susceptibles
        )

    def calcular_expuestos(
        self, _n_infectados_h: float, _n_poblacion_h: float
    ) -> float:
        """
        Funcion la cual resuelve la ecuacion de Expuestos(vector)

        Parameters
        ----------
        _n_infectados_h
            Representa el numero de infectados por parte de los humanos.
        _n_poblacion_h
            Representa el numero total de la poblacion de los humanos.

        Returns
        -------
            Retorna la derivada de expuestos respecto al tiempo (dEv/dt).
        """
        return (
            self.datos_simulacion.fuerza_infeccion
            * (_n_infectados_h / _n_poblacion_h)
            * self.susceptibles
            - self.datos_simulacion.tasa_incubacion * self.expuestos
            - self.datos_simulacion.tasa_muerte * self.expuestos
        )

    def calcular_infectados(self) -> float:
        """
        Funcion la cual resuelve la ecuacion de infectados(vector)

        Returns
        -------
            Retorna la derivada de infectados respecto al tiempo (dIv/dt).
        """
        return (
            self.datos_simulacion.tasa_incubacion * self.expuestos
            - self.datos_simulacion.tasa_muerte * self.infectados
        )
