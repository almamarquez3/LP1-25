import datetime
from abc import ABC, abstractmethod
from typing import List, Optional

class Vehiculo(ABC):
    """
    Clase abstracta que representa a un vehículo.

    Atributos:
        velocidad (float): La velocidad promedio del vehículo en km/h.
        registro_viajes (List[str]): El registro de los viajes realizados por el vehículo.
        tipo (str, opcional): El tipo de vehículo (terrestre, aéreo, etc.).
    """

    def __init__(self, velocidad: float, tipo: Optional[str] = None):
        """
        Inicializa un objeto Vehiculo.

        Args:
            velocidad (float): La velocidad promedio del vehículo en km/h.
            tipo (str, opcional): El tipo de vehículo (terrestre, aéreo, etc.).

        Raises:
            TypeError: Si la velocidad no es un número.
            ValueError: Si la velocidad es negativa.
        """
        if not isinstance(velocidad, (int, float)):
            raise TypeError("La velocidad debe ser un número.")
        if velocidad <= 0:
            raise ValueError("La velocidad debe ser mayor que 0.")

        self.velocidad = velocidad
        self.registro_viajes = []
        self.tipo = tipo

    @abstractmethod
    def calcular_tiempo_viaje(self, distancia: float, trafico: float = 0) -> float:
        """
        Calcula el tiempo de viaje para una distancia determinada.

        Args:
            distancia (float): La distancia a recorrer en km.
            trafico (float, opcional): El nivel de tráfico (por defecto 0).

        Returns:
            float: El tiempo de viaje en horas.
        """
        pass  # Método abstracto, implementado por las subclases

    def __str__(self) -> str:
        """
        Devuelve una representación en cadena del vehículo.

        Returns:
            str: Una cadena que representa al vehículo, incluyendo su tipo y velocidad.
        """

        return f"Vehículo: Tipo={self.tipo}, Velocidad={self.velocidad} km/h"