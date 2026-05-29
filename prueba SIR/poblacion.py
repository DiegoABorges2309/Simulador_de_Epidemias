class Poblacion:
    @staticmethod
    def calcular_poblacion_susceptibles(_s_anterior: int, _d_susceptibles: float, _d_tiempo: int) -> int:
        return round(_s_anterior + _d_susceptibles * _d_tiempo)

    @staticmethod
    def calcular_poblacion_expuestos(_e_anterior: int, _d_expuestos: float, _d_tiempo: int) -> int:
        return round(_e_anterior + _d_expuestos * _d_tiempo)

    @staticmethod
    def calcular_poblacion_infectados(_i_anterior: int, _d_infectados: float, _d_tiempo: int) -> int:
        return round(_i_anterior + _d_infectados * _d_tiempo)

    @staticmethod
    def calcular_poblacion_recuperados(_r_anterior: int, _d_recuperados: float, _d_tiempo: int) -> int:
        return round(_r_anterior + _d_recuperados * _d_tiempo)
