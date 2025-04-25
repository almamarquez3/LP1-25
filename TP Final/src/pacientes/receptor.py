import datetime
from typing import Optional, TYPE_CHECKING
from pacientes.paciente import Paciente


from organos.organo import Organo
from centrosdesalud.centro_de_salud import CentroDeSalud # Evita la dependencia circular

class Receptor(Paciente):
    """
    Representa a un paciente que es receptor de órganos en el sistema.
    Hereda de la clase Paciente y añade atributos específicos de un receptor.
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
        organo_a_recibir: Optional[Organo],
        fecha_agregado_lista_espera: Optional[datetime.date],
        prioridad: int,
        patologia: str,
        grado_urgencia: int,
        hla_match: Optional[int] = None,  # Nuevo atributo
    ):
        """
        Inicializa una instancia de la clase Receptor.

        Args:
            nombre (str): Nombre completo del receptor.
            dni (str): Documento Nacional de Identidad del receptor.
            fecha_nacimiento (datetime.date): Fecha de nacimiento del receptor.
            sexo (str): Sexo del receptor ('M' para masculino, 'F' para femenino).
            telefono (str): Número de teléfono del receptor.
            tipo_sangre (str): Tipo de sangre del receptor (ej. 'A+', 'O-').
            centro_salud_asociado (Optional[CentroDeSalud]): Centro de salud asociado al receptor.
            estado (str): Estado actual del receptor (ej. 'En Espera').
            organo_a_recibir (Optional[Organo]): Objeto Organo que el receptor necesita.
            fecha_agregado_lista_espera (Optional[datetime.date]): Fecha en que el receptor fue agregado a la lista de espera.
            prioridad (int): Nivel de prioridad del receptor en la lista de espera (menor valor indica mayor prioridad).
            patologia (str): Patología que causa la necesidad del trasplante.
            grado_urgencia (int): Grado de urgencia del trasplante (ej. 1 para alta, 3 para baja).
            hla_match (Optional[int]): Puntuación de compatibilidad HLA (si está disponible, entre 0 y 6).

        Raises:
            TypeError: Si el órgano a recibir no es una instancia de la clase Organo (si se proporciona).
            ValueError: Si la prioridad no es un entero positivo.
            ValueError: Si el grado de urgencia no es un entero positivo.
            ValueError: Si el valor de HLA Match no está entre 0 y 6 (si se proporciona).
        """
        super().__init__(nombre, dni, fecha_nacimiento, sexo, telefono, tipo_sangre, centro_salud_asociado, estado)
        if organo_a_recibir is not None and not isinstance(organo_a_recibir, Organo):
            raise TypeError("El órgano a recibir debe ser una instancia de la clase Organo.")
        self.organo_a_recibir = organo_a_recibir
        self.fecha_agregado_lista_espera = fecha_agregado_lista_espera
        if not isinstance(prioridad, int) or prioridad <= 0:
            raise ValueError("La prioridad debe ser un entero positivo.")
        self.prioridad = prioridad
        self.patologia = patologia
        if not isinstance(grado_urgencia, int) or grado_urgencia <= 0:
            raise ValueError("El grado de urgencia debe ser un entero positivo.")
        self.grado_urgencia = grado_urgencia
        if hla_match is not None and not (0 <= hla_match <= 6):
            raise ValueError("El valor de HLA Match debe estar entre 0 y 6.")
        self.hla_match = hla_match

    def __str__(self):
        """
        Retorna una representación en cadena legible del objeto Receptor.
        """
        return f"Receptor: {self.nombre}, DNI: {self.dni}, Tipo de Sangre: {self.tipo_sangre}, HLA: {self.hla_match}, Órgano a Recibir: {self.organo_a_recibir.nombre if self.organo_a_recibir else None}, Prioridad: {self.prioridad}"

    def actualizar_prioridad(self, nueva_prioridad: int):
        """
        Actualiza la prioridad del receptor en la lista de espera.

        Args:
            nueva_prioridad (int): El nuevo nivel de prioridad (menor valor indica mayor prioridad).

        Raises:
            ValueError: Si la nueva prioridad no es un entero positivo.
        """
        if not isinstance(nueva_prioridad, int) or nueva_prioridad <= 0:
            raise ValueError("La nueva prioridad debe ser un entero positivo.")
        self.prioridad = nueva_prioridad

    def recibir_organo(self, organo_donado: Organo):
        """
        Marca al receptor como trasplantado y registra el órgano recibido.

        Args:
            organo_donado (Organo): El objeto Organo que ha sido trasplantado al receptor.

        Raises:
            TypeError: Si el órgano donado no es una instancia de la clase Organo.
        """
        if not isinstance(organo_donado, Organo):
            raise TypeError("El órgano donado debe ser una instancia de la clase Organo.")
        print(f"El receptor {self.nombre} ha recibido un trasplante de {organo_donado.nombre}.")
        self.estado = "Trasplantado"
        self.organo_a_recibir = organo_donado # Ahora el receptor tiene el órgano