from __future__ import annotations
import random
from collections import deque

from persona import Persona


class Hospital:
    """
    La clase hospital se encargará de gestionar
    la cantidad de personal de salud disponible
    como también las camas que se encuentran
    ocupadas, como las que no

    Atributos:
        self.__id: Es un código aleatorio para poder identificar
        específicamente al objeto "Hospital" dentro de la simulación.
        self.nombre: Nombre del hospital dentro de la simulación.
        self.personal_disponible: Una lista que almacena objetos
        de tipo 'Persona' que sean personal de salud.
        self.camas_disponibles: Límite de infectados por hospital.
        self.infectados_en_cama: Lista que almacena a los objetos
        de tipo 'Persona' que estén infectados.
        self.infectados_recuperados: Lista que almacena los id de
        los objetos de tipo 'Persona' que estaban infectados.

    """
    __slots__ = {
        "__id",
        "nombre",
        "personal_disponible",
        "camas_disponibles",
        "infectados_en_cama",
        "infectados_recuperados"
    }

    def __init__(self, _nombre_hospital: str, _personal_disponible: int, _camas_disponibles: int):
        """
        Constructor de la clase Hospital.

        :param _nombre_hospital: Nombre del hospital el cual
        se representara en la simulación.
        :param _camas_disponibles: número de camas con las cuales
        contara el hospital al inicio de la simulación.
        """
        self.__id = random.randint(1000, 9999)
        self.nombre = _nombre_hospital
        self.personal_disponible = []
        self.camas_disponibles = _camas_disponibles
        self.infectados_en_cama = deque(maxlen=_camas_disponibles)
        self.infectados_recuperados = []

    """
    *****************************************************************
                                Métodos
    *****************************************************************
    """

    def agregar_personal(self, _personal: Persona):
        """
        Como dice el nombre, es una función para asignarle
        personal médico al hospital.

        :param _personal: Es un objeto de la clase persona.
        """
        self.personal_disponible.append(_personal)

    def eliminar_personal(self, _indice_personal: int) -> Persona | None:
        """
        Esta función se encarga de sacar de la lista de
        trabajadores de salud del hospital al personal
        que corresponda el índice introducido.

        :param _indice_personal: Un número que sera la
        posición del personal en la lista.
        :return: Retorna al propio objeto persona, si hay
        error retorna 'None'.
        """
        try:
            return self.personal_disponible.pop(_indice_personal)
        except Exception as e:
            print(f"ERROR:: TIPO:{type(e).__name__}: {e}")
            return None

    @staticmethod
    def trasladar_personal(_hospital: Hospital, _personal: Persona) -> bool:
        """
        Función para trasladar personal de un hospital a otro. La
        idea es que en la simulación si un hospital tiene muchos
        pacientes se traslade personal de uno al otro.

        :param _hospital: Es un objeto de tipo Hospital.
        :param _personal: Es un objeto de tipo Persona.
        :return: Retorna True si se completa con éxito,
        Falso si falla.
        """
        try:
            _hospital.agregar_personal(_personal)
            return True
        except Exception as e:
            print(f"ERROR:: TIPO:{type(e).__name__}: {e}")
            return False

    def agregar_paciente(self, _paciente: Persona) -> bool:
        """
        Es una clase para agregar un infectado a la clase
        Hospital para luego este ser tratado.

        :param _paciente: Es un objeto de la clase persona.
        :return True si se logra realizar la acción "agregar"
        False si ocurre un error.
        """
        try:
            camas_sin_ocupar = self.camas_disponibles - len(self.infectados_en_cama)
            if camas_sin_ocupar > 0 and _paciente.esta_contagiado:
                self.infectados_en_cama.append(_paciente)
            return True
        except Exception as e:
            print(f"ERROR:: TIPO:{type(e).__name__}: {e}")
            return False
