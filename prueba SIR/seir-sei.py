from abc import ABC, abstractmethod
import matplotlib.pyplot as plt


class Grafica:
    def __init__(self):
        self.datos_eje_x = []
        self.datos_eje_y = []
        self.datos_eje_g = []
        self.datos_eje_h = []
        self.datos_eje_j = []

    def agregar_datos_x(self, _nuevo_dato):
        self.datos_eje_x.append(_nuevo_dato)

    def agregar_datos_y(self, _nuevo_dato):
        self.datos_eje_y.append(_nuevo_dato)

    def agregar_datos_g(self, _nuevo_dato):
        self.datos_eje_g.append(_nuevo_dato)

    def agregar_datos_h(self, _nuevo_dato):
        self.datos_eje_h.append(_nuevo_dato)

    def agregar_datos_j(self, _nuevo_dato):
        self.datos_eje_j.append(_nuevo_dato)

    def crear_grafica(
        self,
        _titulo,
        _x_titulo,
        _y_titulo,
    ):
        # plt.figure(figsize=(8, 8))

        plt.plot(self.datos_eje_x, self.datos_eje_y, label="Susceptibles", color="blue")
        plt.plot(self.datos_eje_x, self.datos_eje_g, label="Expuestos", color="yellow")
        plt.plot(self.datos_eje_x, self.datos_eje_h, label="Infectados", color="red")
        plt.plot(self.datos_eje_x, self.datos_eje_j, label="Recuperados", color="green")

        plt.title(_titulo)
        plt.xlabel(_x_titulo)
        plt.ylabel(_y_titulo)
        plt.grid(True)

        plt.legend()
        plt.show()


class ModeloInicial(ABC):
    def __init__(
        self,
        _n_poblacion,
        _infectados_inicio,
        _tasa_contagio,
        _tasa_incubacion,
        _tasa_picaduras,
    ):
        self.susceptibles = _n_poblacion - _infectados_inicio
        self.expuestos = 0
        self.infectados = _infectados_inicio
        self.beta = _tasa_contagio
        self.sigmma = _tasa_incubacion
        self.tasa_picaduras = _tasa_picaduras

    @abstractmethod
    def get_numero_poblacion(self):
        pass

    @abstractmethod
    def calcular_susceptibles(self, _modelo):
        pass

    @abstractmethod
    def calcular_expuestos(self, _modelo):
        pass

    @abstractmethod
    def calcular_infectados(self):
        pass

    def calcular_ecuacion(self, _modelo):
        return (
            self.tasa_picaduras
            * self.beta
            * _modelo.infectados
            / _modelo.get_numero_poblacion()
        ) * self.susceptibles


class SEIR(ModeloInicial):
    def __init__(
        self,
        _n_poblacion,
        _infectados_inicio,
        _tasa_contagio,
        _tasa_incubacion,
        _tasa_recuperacion,
        _tasa_picaduras,
    ):
        super().__init__(
            _n_poblacion,
            _infectados_inicio,
            _tasa_contagio,
            _tasa_incubacion,
            _tasa_picaduras,
        )
        self.gamma = _tasa_recuperacion
        self.recuperados = 0

    def get_numero_poblacion(self):
        return self.susceptibles + self.infectados + self.expuestos + self.recuperados

    def calcular_susceptibles(self, _modelo):
        return -(self.calcular_ecuacion(_modelo))

    def calcular_expuestos(self, _modelo):
        return self.calcular_ecuacion(_modelo) - self.sigmma * self.expuestos

    def calcular_infectados(self):
        return self.sigmma * self.expuestos - self.gamma * self.infectados

    def calcular_recuperados(self):
        return self.gamma * self.infectados


class SEI(ModeloInicial):
    def __init__(
        self,
        _n_poblacion,
        _infectados_inicio,
        _tasa_contagio,
        _tasa_incubacion,
        _tasa_picaduras,
        _tasa_nacimiento,
        _tasa_muerte,
    ):
        super().__init__(
            _n_poblacion,
            _infectados_inicio,
            _tasa_contagio,
            _tasa_incubacion,
            _tasa_picaduras,
        )
        self.lamda = _tasa_nacimiento * _n_poblacion
        self.mu = _tasa_muerte

    def get_numero_poblacion(self):
        return self.susceptibles + self.expuestos + self.infectados

    def calcular_susceptibles(self, _modelo):
        return (
            self.lamda - self.calcular_ecuacion(_modelo) - self.mu * self.susceptibles
        )

    def calcular_expuestos(self, _modelo):
        return (
            self.calcular_ecuacion(_modelo)
            - self.sigmma * self.expuestos
            - self.mu * self.expuestos
        )

    def calcular_infectados(self):
        return self.sigmma * self.expuestos - self.mu * self.infectados


class Simulacion:
    def __init__(self):
        self.humano = SEIR(15000, 500, 0.425, 0.1667, 0.1, 0.5)
        self.mosquito = SEI(30000, 1000, 0.375, 0.1, 0.5, 0.0714, 0.07)
        self.grafica = Grafica()

    def calcular_determinantes(self, _dt):
        sh = self.humano.calcular_susceptibles(self.mosquito) * _dt
        eh = self.humano.calcular_expuestos(self.mosquito) * _dt
        ih = self.humano.calcular_infectados() * _dt
        rh = self.humano.calcular_recuperados() * _dt

        sm = self.mosquito.calcular_susceptibles(self.humano) * _dt
        em = self.mosquito.calcular_expuestos(self.humano) * _dt
        im = self.mosquito.calcular_infectados() * _dt

        return [[sh, eh, ih, rh], [sm, em, im]]

    def guardar_nuevos_datos(self, _determinante_tiempo):
        _lista_determinantes = self.calcular_determinantes(_determinante_tiempo)
        for index, model in enumerate([self.humano, self.mosquito]):
            model.susceptibles += _lista_determinantes[index][0]
            model.expuestos += _lista_determinantes[index][1]
            model.infectados += _lista_determinantes[index][2]
            if isinstance(model, SEIR):
                model.recuperados += _lista_determinantes[index][3]

    def inicio(self):
        valor = True
        dt = 0.01
        paso = 0
        while valor:
            paso += 1
            dia_real = dt * paso
            sh = self.humano.susceptibles
            eh = self.humano.expuestos
            ih = self.humano.infectados
            rh = self.humano.recuperados

            sm = self.mosquito.susceptibles
            em = self.mosquito.expuestos
            im = self.mosquito.infectados
            print("")
            print("=====================================")
            print(f"DIA:{dia_real}")
            print("=====================================")
            print("")
            print("HUMANO")
            print("-------------------------------------")
            print(f"Susceptibles:{sh}")
            print("-------------------------------------")
            print(f"Expuestos:{eh}")
            print("-------------------------------------")
            print(f"Infectados:{ih}")
            print("-------------------------------------")
            print(f"Recuperados:{rh}")
            print("-------------------------------------")
            print(f"POBLACION TOTAL: {(self.humano.get_numero_poblacion())}")
            print("-------------------------------------")
            print("")
            print("")
            print("MOSQUITO")
            print("-------------------------------------")
            print(f"Susceptibles:{sm}")
            print("-------------------------------------")
            print(f"Expuestos:{em}")
            print("-------------------------------------")
            print(f"Infectados:{im}")
            print("-------------------------------------")
            print(f"POBLACION TOTAL: {(self.mosquito.get_numero_poblacion())}")
            print("-------------------------------------")
            if paso % 1 == 0:
                self.grafica.agregar_datos_x(paso // 10)
                self.grafica.agregar_datos_y(sh)
                self.grafica.agregar_datos_g(eh)
                self.grafica.agregar_datos_h(ih)
                self.grafica.agregar_datos_j(rh)
            self.guardar_nuevos_datos(dt)
            if (eh + ih + em + im) < 1:
                valor = False
        self.grafica.crear_grafica("MODELO SEIR", "Dias", "Poblacion Humanos")


if __name__ == "__main__":
    hola = Simulacion()
    hola.inicio()
