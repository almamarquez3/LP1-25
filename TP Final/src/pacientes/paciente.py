import datetime
from abc import ABC, abstractmethod
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from centrosdesalud.centro_de_salud import CentroDeSalud  # Evita la dependencia circular

class Paciente(ABC):
    """
    Clase abstracta que representa a un paciente en el sistema del INCUCAI.

    Atributos:
        nombre (str): El nombre del paciente.
        dni (str): El DNI del paciente (debe ser único).
        fecha_nacimiento (datetime.date): La fecha de nacimiento del paciente.
        sexo (str): El sexo del paciente.
        telefono (str): El teléfono de contacto del paciente.
        tipo_sangre (str): El tipo de sangre del paciente.
        centro_salud_asociado (CentroDeSalud): El centro de salud asociado al paciente.
        estado (str): El estado del paciente.
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
    ):
        """
        Inicializa un objeto Paciente.

        Args:
            nombre (str): El nombre del paciente.
            dni (str): El DNI del paciente (debe ser único).
            fecha_nacimiento (datetime.date): La fecha de nacimiento del paciente.
            sexo (str): El sexo del paciente.
            telefono (str): El teléfono de contacto del paciente.
            tipo_sangre (str): El tipo de sangre del paciente.
            centro_salud_asociado (CentroDeSalud): El centro de salud asociado al paciente.
            estado (str): El estado del paciente.

        Raises:
            TypeError: Si alguno de los argumentos tiene un tipo incorrecto.
            ValueError: Si el DNI está vacío o tiene un formato inválido.
        """
        if not isinstance(nombre, str):
            raise TypeError("El nombre debe ser una cadena.")
        if not isinstance(dni, str):
            raise TypeError("El DNI debe ser una cadena.")
        if not dni:
            raise ValueError("El DNI no puede estar vacío.")
        if not isinstance(fecha_nacimiento, datetime.date):
            raise TypeError("La fecha de nacimiento debe ser un objeto datetime.date.")
        if not isinstance(sexo, str):
            raise TypeError("El sexo debe ser una cadena.")
        if not isinstance(telefono, str):
            raise TypeError("El teléfono debe ser una cadena.")
        if not isinstance(tipo_sangre, str):
            raise TypeError("El tipo de sangre debe ser una cadena.")
        if not isinstance(centro_salud_asociado, object):  # Usamos object para evitar la circularidad
            raise TypeError("El centro de salud asociado debe ser un objeto CentroDeSalud.")
        if not isinstance(estado, str):
            raise TypeError("El estado debe ser una cadena.")

        self.nombre = nombre
        self.dni = dni
        self.fecha_nacimiento = fecha_nacimiento
        self.sexo = sexo
        self.telefono = telefono
        self.tipo_sangre = tipo_sangre
        self.centro_salud_asociado = centro_salud_asociado
        self.estado = estado

    def get_dni(self) -> str:
        """
        Obtiene el DNI del paciente.

        Returns:
            str: El DNI del paciente.
        """
        return self.dni

    def set_telefono(self, telefono: str) -> None:
        """
        Establece el teléfono de contacto del paciente.

        Args:
            telefono (str): El nuevo teléfono de contacto.

        Raises:
            TypeError: Si el teléfono no es una cadena.
        """
        if not isinstance(telefono, str):
            raise TypeError("El teléfono debe ser una cadena.")
        self.telefono = telefono

    @abstractmethod
    def __str__(self) -> str:
        """
        Método abstracto para obtener una representación en cadena del paciente.
        Debe ser implementado por las subclases (Donante, Receptor).

        Returns:
            str: Una representación en cadena del paciente.
        """
        pass

    def __eq__(self, other: object) -> bool:
        """
        Compara dos pacientes por su DNI.

        Args:
            other (object): El otro objeto a comparar.

        Returns:
            bool: True si los pacientes tienen el mismo DNI, False en caso contrario.
        """
        if not isinstance(other, Paciente):
            return False
        return self.dni == other.dni