import datetime
from typing import List, Optional, TYPE_CHECKING
from pacientes.paciente import Paciente


from organos.organo import Organo  # Evita la dependencia circular
from centrosdesalud.centro_de_salud import CentroDeSalud  # Evita la dependencia circular

class Donante(Paciente):
    """
    Representa a un paciente que es donante de órganos en el sistema.
    Hereda de la clase Paciente y añade atributos específicos de un donante.
    """
    def __init__(
        self,
        nombre: str,
        dni: str,
        fecha_nacimiento: datetime.date,
        sexo: str,
        telefono: str,
        tipo_sangre: str,
        centro_salud_asociado: Optional[CentroDeSalud],
        estado: str,
        fecha_hora_fallecimiento: datetime.datetime,
        fecha_hora_comienzo_ablacion: datetime.datetime,
        organos_a_donar: List[Organo],
        hla_match: Optional[int] = None,  # Nuevo atributo
    ):
        """
        Inicializa una instancia de la clase Donante.

        Args:
            nombre (str): Nombre completo del donante.
            dni (str): Documento Nacional de Identidad del donante.
            fecha_nacimiento (datetime.date): Fecha de nacimiento del donante.
            sexo (str): Sexo del donante ('M' para masculino, 'F' para femenino).
            telefono (str): Número de teléfono del donante.
            tipo_sangre (str): Tipo de sangre del donante (ej. 'A+', 'O-').
            centro_salud_asociado (Optional[CentroDeSalud]): Centro de salud asociado al donante.
            estado (str): Estado actual del donante (ej. 'Crítico').
            fecha_hora_fallecimiento (datetime.datetime): Fecha y hora del fallecimiento del donante.
            fecha_hora_comienzo_ablacion (datetime.datetime): Fecha y hora en que comienza la ablación de órganos.
            organos_a_donar (List[Organo]): Lista de objetos Organo que el donante puede donar.
            hla_match (Optional[int]): Puntuación de compatibilidad HLA (si está disponible, entre 0 y 6).

        Raises:
            ValueError: Si la fecha y hora de fallecimiento no son anteriores a la fecha y hora de comienzo de la ablación.
            TypeError: Si la lista de órganos a donar no es una lista.
            ValueError: Si el valor de HLA Match no está entre 0 y 6 (si se proporciona).
        """
        super().__init__(nombre, dni, fecha_nacimiento, sexo, telefono, tipo_sangre, centro_salud_asociado, estado)
        if fecha_hora_fallecimiento >= fecha_hora_comienzo_ablacion:
            raise ValueError("La fecha y hora de fallecimiento deben ser anteriores a la fecha y hora de comienzo de la ablación.")
        self.fecha_hora_fallecimiento = fecha_hora_fallecimiento
        self.fecha_hora_comienzo_ablacion = fecha_hora_comienzo_ablacion
        if not isinstance(organos_a_donar, list):
            raise TypeError("La lista de órganos a donar debe ser una lista.")
        self.organos_a_donar = organos_a_donar
        if hla_match is not None and not (0 <= hla_match <= 6):
            raise ValueError("El valor de HLA Match debe estar entre 0 y 6.")
        self.hla_match = hla_match

    def __str__(self):
        """
        Retorna una representación en cadena legible del objeto Donante.
        """
        return f"Donante: {self.nombre}, DNI: {self.dni}, Tipo de Sangre: {self.tipo_sangre}, HLA: {self.hla_match}, Órganos a Donar: {[organo.nombre for organo in self.organos_a_donar]}"

    def agregar_organo_a_donar(self, organo: Organo):
        """
        Agrega un órgano a la lista de órganos a donar del donante.

        Args:
            organo (Organo): El objeto Organo a agregar.

        Raises:
            TypeError: Si el órgano a agregar no es una instancia de la clase Organo.
        """
        if not isinstance(organo, Organo):
            raise TypeError("El órgano a agregar debe ser una instancia de la clase Organo.")
        self.organos_a_donar.append(organo)

    def remover_organo_a_donar(self, organo: Organo):
        """
        Remueve un órgano de la lista de órganos a donar del donante.

        Args:
            organo (Organo): El objeto Organo a remover.

        Raises:
            TypeError: Si el órgano a remover no es una instancia de la clase Organo.
        """
        if not isinstance(organo, Organo):
            raise TypeError("El órgano a remover debe ser una instancia de la clase Organo.")
        if organo in self.organos_a_donar:
            self.organos_a_donar.remove(organo)
        else:
            print(f"{organo.nombre} no está en la lista de órganos a donar de {self.nombre}.")