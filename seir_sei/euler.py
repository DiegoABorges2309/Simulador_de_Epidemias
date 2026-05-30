from seir import Seir
from sei import Sei
from dataclasses import dataclass, field


@dataclass
class VariablesModeloSeir:
    lista_paso_tiempo: list = field(default_factory=list)
    lista_susceptibles: list = field(default_factory=list)
    lista_expuestos: list = field(default_factory=list)
    lista_infectados: list = field(default_factory=list)
    lista_recuperados: list = field(default_factory=list)


@dataclass
class VariablesModeloSei:
    lista_paso_tiempo: list = field(default_factory=list)
    lista_susceptibles: list = field(default_factory=list)
    lista_expuestos: list = field(default_factory=list)
    lista_infectados: list = field(default_factory=list)


class Euler:
    def __init__(self, paso_tiempo: float, tiempo_final: float):
        self.paso_tiempo = paso_tiempo
        self.tiempo_final = tiempo_final
        self.dias_reales = 0
        self.variables_h = VariablesModeloSeir()
        self.variables_v = VariablesModeloSei()

    def calculo_euler(self, modelo_seir: Seir, modelo_sei: Sei):
        self.agregar_paso_tiempo()
        self.agregar_variables_h(
            [
                modelo_seir.susceptibles,
                modelo_seir.expuestos,
                modelo_seir.infectados,
                modelo_seir.recuperados,
            ]
        )
        self.agregar_variables_v(
            [
                modelo_sei.susceptibles,
                modelo_sei.expuestos,
                modelo_sei.infectados,
            ]
        )
        while self.dias_reales < self.tiempo_final:
            self.dias_reales += self.paso_tiempo
            calculo_nuevo_h = self.recalcular_metodo_seir(modelo_seir, modelo_sei)
            calculo_nuevo_v = self.recalcular_metodo_sei(modelo_sei, modelo_seir)
            self.agregar_paso_tiempo()
            self.agregar_variables_h(calculo_nuevo_h)
            self.agregar_variables_v(calculo_nuevo_v)
            self.actualizar_metodo_sei(modelo_sei)
            self.actualizar_metodo_seir(modelo_seir)

    def agregar_paso_tiempo(self):
        self.variables_h.lista_paso_tiempo.append(self.dias_reales)
        self.variables_v.lista_paso_tiempo.append(self.dias_reales)

    # ====================================
    #          variables humanos
    # ====================================
    def agregar_variables_h(self, calculo_nuevo_h: list):
        self.variables_h.lista_susceptibles.append(calculo_nuevo_h[0])
        self.variables_h.lista_expuestos.append(calculo_nuevo_h[1])
        self.variables_h.lista_infectados.append(calculo_nuevo_h[2])
        self.variables_h.lista_recuperados.append(calculo_nuevo_h[3])

    def recalcular_susceptibles_h(self, modelo_seir: Seir, modelo_sei: Sei) -> float:
        return self.variables_h.lista_susceptibles[
            -1
        ] + self.paso_tiempo * modelo_seir.calcular_susceptibles(
            modelo_sei.infectados, modelo_sei.get_poblacion_total()
        )

    def recalcular_expuestos_h(self, modelo_seir: Seir, modelo_sei: Sei) -> float:
        return self.variables_h.lista_expuestos[
            -1
        ] + self.paso_tiempo * modelo_seir.calcular_expuestos(
            modelo_sei.infectados, modelo_sei.get_poblacion_total()
        )

    def recalcular_infectados_h(self, modelo_seir: Seir) -> float:
        return (
            self.variables_h.lista_infectados[-1]
            + self.paso_tiempo * modelo_seir.calcular_infectados()
        )

    def recalcular_recuperados_h(self, modelo_seir: Seir) -> float:
        return (
            self.variables_h.lista_recuperados[-1]
            + self.paso_tiempo * modelo_seir.calcular_recuperados()
        )

    def recalcular_metodo_seir(self, modelo_seir: Seir, modelo_sei: Sei) -> list:
        euler_susceptibles = self.recalcular_susceptibles_h(modelo_seir, modelo_sei)
        euler_expuestos = self.recalcular_expuestos_h(modelo_seir, modelo_sei)
        euler_infectados = self.recalcular_infectados_h(modelo_seir)
        euler_recuperados = self.recalcular_recuperados_h(modelo_seir)

        return [
            euler_susceptibles,
            euler_expuestos,
            euler_infectados,
            euler_recuperados,
        ]

    def actualizar_metodo_seir(self, modelo_seir: Seir):
        modelo_seir.actualizar_variables(
            self.variables_h.lista_susceptibles[-1],
            self.variables_h.lista_expuestos[-1],
            self.variables_h.lista_infectados[-1],
            self.variables_h.lista_recuperados[-1],
        )

    # ====================================
    #          variables vector
    # ====================================
    def agregar_variables_v(self, calculos_nuevo_v: list):
        self.variables_v.lista_susceptibles.append(calculos_nuevo_v[0])
        self.variables_v.lista_expuestos.append(calculos_nuevo_v[1])
        self.variables_v.lista_infectados.append(calculos_nuevo_v[2])

    def recalcular_susceptibles_v(self, modelo_sei: Sei, modelo_seir: Seir) -> float:
        return self.variables_v.lista_susceptibles[
            -1
        ] + self.paso_tiempo * modelo_sei.calcular_susceptibles(
            modelo_seir.infectados, modelo_seir.get_poblacion_total()
        )

    def recalcular_expuestos_v(self, modelo_sei: Sei, modelo_seir: Seir) -> float:
        return self.variables_v.lista_expuestos[
            -1
        ] + self.paso_tiempo * modelo_sei.calcular_expuestos(
            modelo_seir.infectados, modelo_seir.get_poblacion_total()
        )

    def recalcular_infectados_v(self, modelo_sei: Sei) -> float:
        return (
            self.variables_v.lista_infectados[-1]
            + self.paso_tiempo * modelo_sei.calcular_infectados()
        )

    def recalcular_metodo_sei(self, modelo_sei: Sei, modelo_seir: Seir) -> list:
        euler_susceptibles = self.recalcular_susceptibles_v(modelo_sei, modelo_seir)
        euler_expuestos = self.recalcular_expuestos_v(modelo_sei, modelo_seir)
        euler_infectados = self.recalcular_infectados_v(modelo_sei)

        return [euler_susceptibles, euler_expuestos, euler_infectados]

    def actualizar_metodo_sei(self, modelo_sei: Sei):
        modelo_sei.actualizar_variables(
            self.variables_v.lista_susceptibles[-1],
            self.variables_v.lista_expuestos[-1],
            self.variables_v.lista_infectados[-1],
        )
