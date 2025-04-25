from typing import List, Optional
from centrosdesalud.vehiculo import Vehiculo

class Avion(Vehiculo):
    """
    Clase que representa a un avión.

    Atributos:
        velocidad (float): La velocidad promedio del avión en km/h.
        registro_viajes (List[str]): El registro de los viajes realizados por el avión.
    """

    def __init__(self, velocidad: float):
        """
        Inicializa un objeto Avion.

        Args:
            velocidad (float): La velocidad promedio del avión en km/h.

        Raises:
            TypeError: Si la velocidad no es un número.
            ValueError: Si la velocidad es negativa.
        """

        super().__init__(velocidad, tipo="Avion")

    def calcular_tiempo_viaje(self, distancia: float, trafico: float = 0) -> float:
        """
        Calcula el tiempo de viaje para un avión (el tráfico no afecta a los aviones).

        Args:
            distancia (float): La distancia a recorrer en km.
            trafico (float, opcional): El nivel de tráfico (ignorado para aviones).

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
        Devuelve una representación en cadena del avión.

        Returns:
            str: Una cadena que representa al avión, incluyendo su velocidad.
        """

        return f"Vehículo Avión: Velocidad={self.velocidad} km/h"