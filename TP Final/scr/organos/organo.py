import datetime
from typing import Optional

class Organo:
    """
    Clase que representa a un órgano.

    Atributos:
        nombre (str): El nombre del órgano.
        fecha_hora_ablacion (datetime.datetime, opcional): La fecha y hora de la ablación del órgano.
    """

    def __init__(self, nombre: str, fecha_hora_ablacion: Optional[datetime.datetime] = None):
        """
        Inicializa un objeto Organo.

        Args:
            nombre (str): El nombre del órgano.
            fecha_hora_ablacion (datetime.datetime, opcional): La fecha y hora de la ablación del órgano.
                                                        Puede ser None si la ablación aún no se ha realizado.

        Raises:
            TypeError: Si el nombre no es una cadena o si la fecha y hora de ablación no es un objeto datetime.datetime
                       cuando se proporciona.
        """
        if not isinstance(nombre, str):
            raise TypeError("El nombre del órgano debe ser una cadena.")
        if fecha_hora_ablacion is not None and not isinstance(fecha_hora_ablacion, datetime.datetime):
            raise TypeError("La fecha y hora de ablación debe ser un objeto datetime.datetime.")

        self.nombre = nombre
        self.fecha_hora_ablacion = fecha_hora_ablacion

    def set_fecha_hora_ablacion(self, fecha_hora: datetime.datetime) -> None:
        """
        Establece la fecha y hora de la ablación del órgano.

        Args:
            fecha_hora (datetime.datetime): La fecha y hora de la ablación.

        Raises:
            TypeError: Si la fecha y hora no es un objeto datetime.datetime.
        """
        if not isinstance(fecha_hora, datetime.datetime):
            raise TypeError("La fecha y hora de ablación debe ser un objeto datetime.datetime.")
        self.fecha_hora_ablacion = fecha_hora

    def __str__(self) -> str:
        """
        Devuelve una representación en cadena del órgano.

        Returns:
            str: Una cadena que representa al órgano, incluyendo su nombre y, si está disponible,
                 la fecha y hora de la ablación.
        """
        fecha_hora_str = self.fecha_hora_ablacion.strftime("%Y-%m-%d %H:%M:%S") if self.fecha_hora_ablacion else "No disponible"
        return f"Órgano: {self.nombre}, Ablación: {fecha_hora_str}"