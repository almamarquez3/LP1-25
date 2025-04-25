from typing import List, Optional
from centrosdesalud.vehiculo import Vehiculo

class Terrestre(Vehiculo):
    """
    Clase que representa a un vehículo terrestre.

    Atributos:
        velocidad (float): La velocidad promedio del vehículo terrestre en km/h.
        registro_viajes (List[str]): El registro de los viajes realizados por el vehículo terrestre.
    """

    def __init__(self, velocidad: float):
        """
        Inicializa un objeto Terrestre.

        Args:
            velocidad (float): La velocidad promedio del vehículo terrestre en km/h.

        Raises:
            TypeError: Si la velocidad no es un número.
            ValueError: Si la velocidad es negativa.
        """
        super().__init__(velocidad, tipo="Terrestre")

    def calcular_tiempo_viaje(self, distancia: float, trafico: float) -> float:
        """
        Calcula el tiempo de viaje para un vehículo terrestre, considerando el tráfico.

        Args:
            distancia (float): La distancia a recorrer en km.
            trafico (float): El nivel de tráfico (un valor entre 0 y 1, donde 0 es sin tráfico y 1 es tráfico máximo).

        Returns:
            float: El tiempo de viaje en horas.

        Raises:
            TypeError: Si la distancia o el tráfico no son números.
            ValueError: Si la distancia es negativa o el tráfico está fuera del rango válido.
        """
        if not isinstance(distancia, (int, float)):
            raise TypeError("La distancia debe ser un número.")
        if not isinstance(trafico, (int, float)):
            raise TypeError("El tráfico debe ser un número.")
        if distancia <= 0:
            raise ValueError("La distancia debe ser mayor que 0.")
        if not 0 <= trafico <= 1:
            raise ValueError("El tráfico debe estar entre 0 y 1.")

        tiempo_viaje = distancia / (self.velocidad * (1 - trafico))
        return tiempo_viaje

    def __str__(self) -> str:
        """
        Devuelve una representación en cadena del vehículo terrestre.

        Returns:
            str: Una cadena que representa al vehículo terrestre, incluyendo su velocidad.
        """

        return f"Vehículo Terrestre: Velocidad={self.velocidad} km/h"