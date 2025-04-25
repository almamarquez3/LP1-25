import datetime
from typing import Optional
import random


class Cirujano:
    """
    Clase que representa a un cirujano.

    Atributos:
        nombre (str): El nombre del cirujano.
        especialidad (str): La especialidad del cirujano.
        disponible (bool): Indica si el cirujano está disponible para una operación.
    """

    def __init__(self, nombre: str, especialidad: str):
        """
        Inicializa un objeto Cirujano.

        Args:
            nombre (str): El nombre del cirujano.
            especialidad (str): La especialidad del cirujano.

        Raises:
            TypeError: Si alguno de los argumentos tiene un tipo incorrecto.
        """
        if not isinstance(nombre, str):
            raise TypeError("El nombre debe ser una cadena.")
        if not isinstance(especialidad, str):
            raise TypeError("La especialidad debe ser una cadena.")

        self.nombre = nombre
        self.especialidad = especialidad
        self.disponible = True  # Inicialmente, el cirujano está disponible

    def calcular_exito_trasplante(self, organo: "Organo") -> bool:  # Anotación de tipo condicional
        """
        Calcula la probabilidad de éxito de un trasplante.

        Args:
            organo (Organo): El órgano a trasplantar.

        Returns:
            bool: True si el trasplante se considera exitoso (probabilidad mayor a 0.5), False en caso contrario.

        Raises:
            TypeError: Si el argumento no es un objeto Organo.
        """
        if not isinstance(organo, object):  # Usamos object para evitar la circularidad
            raise TypeError("El argumento debe ser un objeto Organo.")

        #  Simulación de la probabilidad de éxito (esto podría ser más complejo)
        probabilidad_exito = random.random()  # Un número aleatorio entre 0 y 1
        return probabilidad_exito > 0.5

    def esta_disponible(self, fecha_operacion: datetime.date) -> bool:
        """
        Verifica si el cirujano está disponible para una operación en una fecha determinada.

        Args:
            fecha_operacion (datetime.date): La fecha de la operación.

        Returns:
            bool: True si el cirujano está disponible, False en caso contrario.

        Raises:
            TypeError: Si la fecha de la operación no es del tipo correcto.
        """
        if not isinstance(fecha_operacion, datetime.date):
            raise TypeError(
                "La fecha de la operación debe ser un objeto datetime.date."
            )

        #  Simulación de la disponibilidad (esto podría ser más complejo,
        #  considerando horarios, otras cirugías, etc.)
        return self.disponible

    def __str__(self) -> str:
        """
        Devuelve una representación en cadena del cirujano.

        Returns:
            str: Una cadena que representa al cirujano, incluyendo su nombre y especialidad.
        """
        return f"Cirujano: {self.nombre}, Especialidad: {self.especialidad}"