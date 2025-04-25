import datetime
from typing import List, Optional, TYPE_CHECKING
from paciente import Paciente

if TYPE_CHECKING:
    from organos.organo import Organo  # Evita la dependencia circular

class Donante(Paciente):
    """
    Clase que representa a un donante de órganos.

    Atributos:
        fecha_hora_fallecimiento (datetime.datetime): La fecha y hora del fallecimiento del donante.
        fecha_hora_comienzo_ablacion (datetime.datetime): La fecha y hora del comienzo de la ablación.
        organos_a_donar (List[Organo]): La lista de órganos que el donante puede donar.
    """

    def __init__(
        self,
        nombre: str,
        dni: str,
        fecha_nacimiento: datetime.date,
        sexo: str,
        telefono: str,
        tipo_sangre: str,
        centro_salud_asociado: "CentroDeSalud",  # Anotación de tipo condicional
        estado: str,
        fecha_hora_fallecimiento: datetime.datetime,
        fecha_hora_comienzo_ablacion: datetime.datetime,
        organos_a_donar: List["Organo"],  # Anotación de tipo condicional
    ):
        """
        Inicializa un objeto Donante.

        Args:
            nombre (str): El nombre del donante.
            dni (str): El DNI del donante (debe ser único).
            fecha_nacimiento (datetime.date): La fecha de nacimiento del donante.
            sexo (str): El sexo del donante.
            telefono (str): El teléfono de contacto del donante.
            tipo_sangre (str): El tipo de sangre del donante.
            centro_salud_asociado (CentroDeSalud): El centro de salud asociado al donante.
            estado (str): El estado del donante.
            fecha_hora_fallecimiento (datetime.datetime): La fecha y hora del fallecimiento del donante.
            fecha_hora_comienzo_ablacion (datetime.datetime): La fecha y hora del comienzo de la ablación.
            organos_a_donar (List[Organo]): La lista de órganos que el donante puede donar.

        Raises:
            TypeError: Si alguno de los argumentos tiene un tipo incorrecto.
        """
        super().__init__(
            nombre,
            dni,
            fecha_nacimiento,
            sexo,
            telefono,
            tipo_sangre,
            centro_salud_asociado,
            estado,
        )  # Llama al constructor de la clase padre (Paciente)

        if not isinstance(fecha_hora_fallecimiento, datetime.datetime):
            raise TypeError(
                "La fecha y hora de fallecimiento debe ser un objeto datetime.datetime."
            )
        if not isinstance(fecha_hora_comienzo_ablacion, datetime.datetime):
            raise TypeError(
                "La fecha y hora de comienzo de la ablación debe ser un objeto datetime.datetime."
            )
        if not isinstance(organos_a_donar, list):
            raise TypeError("La lista de órganos a donar debe ser una lista.")
        for organo in organos_a_donar:
            if not isinstance(organo, object):  # Usamos object para evitar la circularidad
                raise TypeError("Cada órgano en la lista debe ser un objeto Organo.")

        self.fecha_hora_fallecimiento = fecha_hora_fallecimiento
        self.fecha_hora_comienzo_ablacion = fecha_hora_comienzo_ablacion
        self.organos_a_donar = organos_a_donar

    def quitar_organo_donado(self, organo: "Organo") -> None:
        """
        Quita un órgano de la lista de órganos a donar.

        Args:
            organo (Organo): El órgano a quitar de la lista.

        Raises:
            TypeError: Si el argumento no es un objeto Organo.
            ValueError: Si el órgano no está en la lista de órganos a donar.
        """
        if not isinstance(organo, object):  # Usamos object para evitar la circularidad
            raise TypeError("El argumento debe ser un objeto Organo.")
        if organo not in self.organos_a_donar:
            raise ValueError("El órgano no está en la lista de órganos a donar.")
        self.organos_a_donar.remove(organo)

    def __str__(self) -> str:
        """
        Devuelve una representación en cadena del donante.

        Returns:
            str: Una cadena que representa al donante, incluyendo su nombre y DNI.
        """

        return f"Donante: {self.nombre}, DNI: {self.dni}"