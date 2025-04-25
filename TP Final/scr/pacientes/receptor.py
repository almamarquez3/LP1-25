import datetime
from typing import Optional, TYPE_CHECKING
from paciente import Paciente

if TYPE_CHECKING:
    from organos.organo import Organo
    from centros_de_salud.centro_de_salud import CentroDeSalud # Evita la dependencia circular


class Receptor(Paciente):
    """
    Clase que representa a un receptor de órganos.

    Atributos:
        organo_a_recibir (Organo): El órgano que el receptor necesita.
        fecha_agregado_lista_espera (datetime.date): La fecha en que el receptor fue agregado a la lista de espera.
        prioridad (int): La prioridad del receptor en la lista de espera.
        patologia (str): La patología que requiere el trasplante.
        grado_urgencia (int): El grado de urgencia del receptor.
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
        organo_a_recibir: "Organo",  # Anotación de tipo condicional
        fecha_agregado_lista_espera: datetime.date,
        prioridad: int,
        patologia: str,
        grado_urgencia: int,
    ):
        """
        Inicializa un objeto Receptor.

        Args:
            nombre (str): El nombre del receptor.
            dni (str): El DNI del receptor (debe ser único).
            fecha_nacimiento (datetime.date): La fecha de nacimiento del receptor.
            sexo (str): El sexo del receptor.
            telefono (str): El teléfono de contacto del receptor.
            tipo_sangre (str): El tipo de sangre del receptor.
            centro_salud_asociado (CentroDeSalud): El centro de salud asociado al receptor.
            estado (str): El estado del receptor.
            organo_a_recibir (Organo): El órgano que el receptor necesita.
            fecha_agregado_lista_espera (datetime.date): La fecha en que el receptor fue agregado a la lista de espera.
            prioridad (int): La prioridad del receptor en la lista de espera.
            patologia (str): La patología que requiere el trasplante.
            grado_urgencia (int): El grado de urgencia del receptor.

        Raises:
            TypeError: Si alguno de los argumentos tiene un tipo incorrecto.
            ValueError: Si la prioridad o el grado de urgencia son inválidos.
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

        if not isinstance(organo_a_recibir, object):  # Usamos object para evitar la circularidad
            raise TypeError("El órgano a recibir debe ser un objeto Organo.")
        if not isinstance(fecha_agregado_lista_espera, datetime.date):
            raise TypeError(
                "La fecha de agregado a la lista de espera debe ser un objeto datetime.date."
            )
        if not isinstance(prioridad, int):
            raise TypeError("La prioridad debe ser un entero.")
        if not isinstance(patologia, str):
            raise TypeError("La patología debe ser una cadena.")
        if not isinstance(grado_urgencia, int):
            raise TypeError("El grado de urgencia debe ser un entero.")

        if prioridad <= 0:
            raise ValueError("La prioridad debe ser mayor que 0.")
        if grado_urgencia <= 0:
            raise ValueError("El grado de urgencia debe ser mayor que 0.")

        self.organo_a_recibir = organo_a_recibir
        self.fecha_agregado_lista_espera = fecha_agregado_lista_espera
        self.prioridad = prioridad
        self.patologia = patologia
        self.grado_urgencia = grado_urgencia

    def set_estado(self, estado: str) -> None:
        """
        Establece el estado del receptor.

        Args:
            estado (str): El nuevo estado del receptor.

        Raises:
            TypeError: Si el estado no es una cadena.
        """
        if not isinstance(estado, str):
            raise TypeError("El estado debe ser una cadena.")
        self.estado = estado

    def set_prioridad(self, prioridad: int) -> None:
        """
        Establece la prioridad del receptor en la lista de espera.

        Args:
            prioridad (int): La nueva prioridad del receptor.

        Raises:
            TypeError: Si la prioridad no es un entero.
            ValueError: Si la prioridad es inválida (menor o igual a 0).
        """
        if not isinstance(prioridad, int):
            raise TypeError("La prioridad debe ser un entero.")
        if prioridad <= 0:
            raise ValueError("La prioridad debe ser mayor que 0.")
        self.prioridad = prioridad

    def __str__(self) -> str:
        """
        Devuelve una representación en cadena del receptor.

        Returns:
            str: Una cadena que representa al receptor, incluyendo su nombre, DNI y órgano a recibir.
        """
        return f"Receptor: {self.nombre}, DNI: {self.dni}, Órgano a Recibir: {self.organo_a_recibir.nombre if self.organo_a_recibir else None}"

    def __lt__(self, other: "Receptor") -> bool:
        """
        Compara dos receptores por su prioridad.

        Args:
            other (Receptor): El otro receptor a comparar.

        Returns:
            bool: True si este receptor tiene menor prioridad (mayor urgencia) que el otro, False en caso contrario.

        Raises:
            TypeError: Si el otro objeto no es un Receptor.
        """
        if not isinstance(other, Receptor):
            raise TypeError("No se puede comparar un Receptor con un objeto de otro tipo.")
        return self.prioridad < other.prioridad