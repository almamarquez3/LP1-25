from typing import List, Optional
from centrosdesalud.vehiculo import Vehiculo

class Helicoptero(Vehiculo):
    """
    Clase que representa a un helicóptero.

    Atributos:
        velocidad (float): La velocidad promedio del helicóptero en km/h.
        registro_viajes (List[str]): El registro de los viajes realizados por el helicóptero.
    """

    def __init__(self, velocidad: float):
        """
        Inicializa un objeto Helicoptero.

        Args:
            velocidad (float): La velocidad promedio del helicóptero en km/h.

        Raises:
            TypeError: Si la velocidad no es un número.
            ValueError: Si la velocidad es negativa.
        """

        super().__init__(velocidad, tipo="Helicoptero")

    def calcular_tiempo_viaje(self, distancia: float, trafico: float = 0) -> float:
        """
        Calcula el tiempo de viaje para un helicóptero (el tráfico no afecta a los helicópteros).

        Args:
            distancia (float): La distancia a recorrer en km.
            trafico (float, opcional): El nivel de tráfico (ignorado para helicópteros).

        Returns:
            float: El tiempo de viaje en horas.

        Raises:
            TypeError: Si la distancia no es un número.
            ValueError: Si la distancia es negativa.
        """
        if not isinstance(distancia, (int, float)):
            raise TypeError("La distancia debe ser un número.")
        if distancia <= 0:
            raise ValueError("La distancia debe ser mayor que 0.")

        tiempo_viaje = distancia / self.velocidad
        return tiempo_viaje

    def __str__(self) -> str:
        """
        Devuelve una representación en cadena del helicóptero.

        Returns:
            str: Una cadena que representa al helicóptero, incluyendo su velocidad.
        """

        return f"Vehículo Helicóptero: Velocidad={self.velocidad} km/h"
