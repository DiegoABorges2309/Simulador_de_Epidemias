import random


def definir_hobby(_es_personal_salud: bool) -> bool:
    """
    Función para determinar si una persona tiene el hobby
    'Fiestero' o no
    :param _es_personal_salud: es una variable booleana
    porque si es de salud es menos probable que sea 'fiestero'.
    Las personas tienen un 28% de ser fiesteras
    :return: si es fiestero retorna 'True' o 'False' si no
    """
    posibilidad = 28
    if _es_personal_salud:
        posibilidad = 10
    if random.randint(0, 100) < posibilidad:
        return True
    return False


def definir_ocupacion() -> bool:
    """
    Función para determinar si una persona es del
    sector salud. Este atributo influye en su
    riesgo de ser contaminada. Las personas tienen
    un 33% de ser trabajadores de salud.
    :return: Si es personal salud retorna 'True' o 'False' si no
    """
    if random.randint(0, 100) < 33:
        return True
    return False


class Persona:
    """
    Es la clase que se encargara de procesar/manejar
    la información, atributos y métodos propios de los
    infectados/sanos.

    Atributos:
        self.id: Es un código aleatorio para poder identificar
        específicamente al objeto "persona" dentro de la simulación.
        Self.esta_contagiado: estado de contagiado/sano.
        Self.dias_enfermo: días después del contagio.
        Self.en_hospital: si está ingresado o no.
        Self.dias_hospital: días en el hospital.
    Nuevos atributos de la version 2:
        Self.posición_x: posición del objeto en el eje X.
        Self.posición_y: posición del objeto en el eje Y.
        Self.ocupación: el trabajo de la persona influye directamente
        en el riego de contagio.
        Self.es_fiestero: si es una persona que se expone a sitios
        muy concurridos como reuniones influye directamente
        en el riesgo de contagio.
    """
    __slots__ = [
        "__id",
        "esta_contagiado",
        "dias_enfermo",
        "esta_en_hospital",
        "dias_hospital",
        "posicion_x",
        "posicion_y",
        "es_personal_salud",
        "es_fiestero"
    ]

    def __init__(self) -> None:
        self.__id = random.randint(100000000, 999999999)
        self.esta_contagiado = False
        self.dias_enfermo = 0
        self.esta_en_hospital = False
        self.dias_hospital = 0
        self.posicion_x = 0.0
        self.posicion_y = 0.0
        self.es_personal_salud = definir_ocupacion()
        self.es_fiestero = definir_hobby(self.es_personal_salud)

    # Getters:
    def get_id_persona(self) -> int:
        return self.__id