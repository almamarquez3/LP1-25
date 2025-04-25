import datetime
from typing import List, Optional, TYPE_CHECKING
from geopy.geocoders import Nominatim
from geopy.distance import geodesic

if TYPE_CHECKING:
    from pacientes.paciente import Paciente
    from vehiculos.vehiculo import Vehiculo
    from centros_de_salud.cirujano import Cirujano


class CentroDeSalud:
    """
    Clase que representa a un centro de salud.

    Atributos:
        nombre (str): El nombre del centro de salud.
        direccion (str): La dirección del centro de salud.
        partido (str): El partido (municipio) donde se encuentra el centro de salud.
        provincia (str): La provincia donde se encuentra el centro de salud.
        telefono (str): El teléfono de contacto del centro de salud.
        cirujanos (List[Cirujano]): La lista de cirujanos del centro de salud.
        vehiculos (List[Vehiculo]): La lista de vehículos del centro de salud.
    """

    def __init__(
        self,
        nombre: str,
        direccion: str,
        partido: str,
        provincia: str,
        telefono: str,
        cirujanos: List["Cirujano"],  # Anotación de tipo condicional
        vehiculos: List["Vehiculo"],  # Anotación de tipo condicional
    ):
        """
        Inicializa un objeto CentroDeSalud.

        Args:
            nombre (str): El nombre del centro de salud.
            direccion (str): La dirección del centro de salud.
            partido (str): El partido (municipio) donde se encuentra el centro de salud.
            provincia (str): La provincia donde se encuentra el centro de salud.
            telefono (str): El teléfono de contacto del centro de salud.
            cirujanos (List[Cirujano]): La lista de cirujanos del centro de salud.
            vehiculos (List[Vehiculo]): La lista de vehículos del centro de salud.

        Raises:
            TypeError: Si alguno de los argumentos tiene un tipo incorrecto.
        """
        if not isinstance(nombre, str):
            raise TypeError("El nombre debe ser una cadena.")
        if not isinstance(direccion, str):
            raise TypeError("La dirección debe ser una cadena.")
        if not isinstance(partido, str):
            raise TypeError("El partido debe ser una cadena.")
        if not isinstance(provincia, str):
            raise TypeError("La provincia debe ser una cadena.")
        if not isinstance(telefono, str):
            raise TypeError("El teléfono debe ser una cadena.")
        if not isinstance(cirujanos, list):
            raise TypeError("La lista de cirujanos debe ser una lista.")
        for cirujano in cirujanos:
            if not isinstance(cirujano, object):  # Usamos object para evitar la circularidad
                raise TypeError("Cada cirujano en la lista debe ser un objeto Cirujano.")
        if not isinstance(vehiculos, list):
            raise TypeError("La lista de vehículos debe ser una lista.")
        for vehiculo in vehiculos:
            if not isinstance(vehiculo, object):  # Usamos object para evitar la circularidad
                raise TypeError("Cada vehículo en la lista debe ser un objeto Vehiculo.")

        self.nombre = nombre
        self.direccion = direccion
        self.partido = partido
        self.provincia = provincia
        self.telefono = telefono
        self.cirujanos = cirujanos
        self.vehiculos = vehiculos
        self.geolocator = Nominatim(user_agent="incucai_app")  # Inicializa el geolocator

    def calcular_tiempo_viaje(
        self, distancia: float, ubicacion_receptor: str
    ) -> float:
        """
        Calcula el tiempo estimado de viaje a un destino.

        Args:
            distancia (float): La distancia en kilómetros al destino.
            ubicacion_receptor (str): La ubicación del receptor (para obtener detalles si es necesario).

        Returns:
            float: El tiempo estimado de viaje en horas.

        Raises:
            TypeError: Si la distancia no es un número.
            ValueError: Si la distancia es negativa.
        """
        if not isinstance(distancia, (int, float)):
            raise TypeError("La distancia debe ser un número.")
        if distancia < 0:
            raise ValueError("La distancia no puede ser negativa.")

        #  Simple: Asumimos una velocidad promedio (esto podría ser más complejo)
        velocidad_promedio = 60  # km/h
        tiempo_viaje = distancia / velocidad_promedio
        return tiempo_viaje

    def seleccionar_vehiculo(
        self, distancia: float, ubicacion_receptor: str, grado_urgencia: int
    ) -> "Vehiculo":  # Anotación de tipo condicional
        """
        Selecciona el vehículo más apropiado para el transporte de un órgano.

        Args:
            distancia (float): La distancia al receptor.
            ubicacion_receptor (str): La ubicación del receptor.
            grado_urgencia (int): El grado de urgencia del trasplante.

        Returns:
            Vehiculo: El vehículo seleccionado.

        Raises:
            TypeError: Si la distancia o el grado de urgencia no son del tipo correcto.
            ValueError: Si no hay vehículos disponibles.
        """
        if not isinstance(distancia, (int, float)):
            raise TypeError("La distancia debe ser un número.")
        if not isinstance(grado_urgencia, int):
            raise TypeError("El grado de urgencia debe ser un entero.")

        vehiculo_seleccionado = None
        #  Lógica de selección de vehículo (simplificada)
        if distancia <= 100:  # Dentro de la misma ciudad/área
            for vehiculo in self.vehiculos:
                if vehiculo.tipo == "Terrestre":
                    vehiculo_seleccionado = vehiculo
                    break
        elif distancia <= 300:  # Dentro de la misma provincia
            for vehiculo in self.vehiculos:
                if vehiculo.tipo == "Helicoptero":
                    vehiculo_seleccionado = vehiculo
                    break
        else:  # Fuera de la provincia
            for vehiculo in self.vehiculos:
                if vehiculo.tipo == "Avion":
                    vehiculo_seleccionado = vehiculo
                    break

        if vehiculo_seleccionado is None:
            raise ValueError("No hay vehículos disponibles para el transporte.")

        return vehiculo_seleccionado

    def asignar_cirujano(self, fecha_operacion: datetime.date) -> "Cirujano":  # Anotación de tipo condicional
        """
        Asigna un cirujano disponible para una operación en una fecha determinada.

        Args:
            fecha_operacion (datetime.date): La fecha de la operación.

        Returns:
            Cirujano: El cirujano asignado.

        Raises:
            TypeError: Si la fecha de la operación no es del tipo correcto.
            ValueError: Si no hay cirujanos disponibles para la fecha.
        """
        if not isinstance(fecha_operacion, datetime.date):
            raise TypeError(
                "La fecha de la operación debe ser un objeto datetime.date."
            )

        cirujano_disponible = None
        #  Lógica de asignación de cirujano (simplificada)
        for cirujano in self.cirujanos:
            cirujano.disponible = cirujano.esta_disponible(fecha_operacion)
            if cirujano.disponible:
                cirujano_disponible = cirujano
                break

        if cirujano_disponible is None:
            raise ValueError("No hay cirujanos disponibles para la fecha especificada.")

        return cirujano_disponible

    def __str__(self) -> str:
        """
        Devuelve una representación en cadena del centro de salud.

        Returns:
            str: Una cadena que representa al centro de salud, incluyendo su nombre y dirección.
        """
        return f"Centro de Salud: {self.nombre}, Dirección: {self.direccion}"