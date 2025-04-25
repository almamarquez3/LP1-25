import datetime
from typing import List, Dict, Optional, Tuple, TYPE_CHECKING

if TYPE_CHECKING:
    from pacientes.paciente import Paciente
    from pacientes.donante import Donante
    from pacientes.receptor import Receptor
    from organos.organo import Organo
    from centros_de_salud.centro_de_salud import CentroDeSalud


class INCUCAI:
    """
    Clase que representa al INCUCAI (Instituto Nacional Central Único Coordinador de Ablación e Implante).

    Atributos:
        donantes (Dict[str, Donante]): Un diccionario que almacena a los donantes, utilizando el DNI como clave.
        receptores (Dict[str, Receptor]): Un diccionario que almacena a los receptores, utilizando el DNI como clave.
        centros_de_salud (Dict[str, CentroDeSalud]): Un diccionario que almacena los centros de salud,
                                                    utilizando el nombre como clave.
    """

    def __init__(
        self,
        donantes: Optional[Dict[str, "Donante"]] = None,
        receptores: Optional[Dict[str, "Receptor"]] = None,
        centros_de_salud: Optional[Dict[str, "CentroDeSalud"]] = None,
    ):
        """
        Inicializa un objeto INCUCAI.

        Args:
            donantes (Dict[str, Donante], opcional): Un diccionario inicial de donantes.
            receptores (Dict[str, Receptor], opcional): Un diccionario inicial de receptores.
            centros_de_salud (Dict[str, CentroDeSalud], opcional): Un diccionario inicial de centros de salud.
        """
        self.donantes = donantes if donantes is not None else {}
        self.receptores = receptores if receptores is not None else {}
        self.centros_de_salud = centros_de_salud if centros_de_salud is not None else {}

    def registrar_paciente(self, paciente: "Paciente") -> None:
        """
        Registra a un paciente en el sistema, validando que no esté duplicado.

        Args:
            paciente (Paciente): El paciente a registrar (Donante o Receptor).

        Raises:
            TypeError: Si el paciente no es una instancia de Donante o Receptor.
            ValueError: Si el paciente ya está registrado en el sistema.
        """

        if not isinstance(paciente, (Donante, Receptor)):
            raise TypeError(
                "El paciente debe ser una instancia de Donante o Receptor."
            )

        if isinstance(paciente, Donante):
            if paciente.dni in self.donantes:
                raise ValueError(
                    f"El donante con DNI {paciente.dni} ya está registrado."
                )
            self.donantes[paciente.dni] = paciente
            self._buscar_coincidencias_donante(paciente)  # Buscar coincidencias al registrar donante
        elif isinstance(paciente, Receptor):
            if paciente.dni in self.receptores:
                raise ValueError(
                    f"El receptor con DNI {paciente.dni} ya está registrado."
                )
            self.receptores[paciente.dni] = paciente
            self._buscar_coincidencias_receptor(paciente)  # Buscar coincidencias al registrar receptor

    def quitar_donante(self, donante: "Donante") -> None:
        """
        Quita a un donante de la lista de donantes.

        Args:
            donante (Donante): El donante a quitar.

        Raises:
            TypeError: Si el donante no es una instancia de Donante.
            ValueError: Si el donante no está registrado en el sistema.
        """
        if not isinstance(donante, Donante):
            raise TypeError("El argumento debe ser un Donante.")
        if donante.dni not in self.donantes:
            raise ValueError(
                f"No se puede quitar al donante con DNI {donante.dni} porque no está registrado."
            )
        del self.donantes[donante.dni]

    def quitar_receptor(self, receptor: "Receptor") -> None:
        """
        Quita a un receptor de la lista de receptores.

        Args:
            receptor (Receptor): El receptor a quitar.

        Raises:
            TypeError: Si el receptor no es una instancia de Receptor.
            ValueError: Si el receptor no está registrado en el sistema.
        """
        if not isinstance(receptor, Receptor):
            raise TypeError("El argumento debe ser un Receptor.")
        if receptor.dni not in self.receptores:
            raise ValueError(
                f"No se puede quitar al receptor con DNI {receptor.dni} porque no está registrado."
            )
        del self.receptores[receptor.dni]

    def buscar_pacientes_en_espera_por_centro_de_salud(
        self, centro_de_salud: "CentroDeSalud"
    ) -> List["Receptor"]:
        """
        Busca todos los pacientes en la lista de espera (receptores) asociados a un centro de salud específico.

        Args:
            centro_de_salud (CentroDeSalud): El centro de salud para el cual se busca los pacientes en espera.

        Returns:
            List[Receptor]: Una lista de receptores asociados al centro de salud dado.

        Raises:
            TypeError: Si el centro de salud no es una instancia de CentroDeSalud.
        """
        if not isinstance(centro_de_salud, CentroDeSalud):
            raise TypeError(
                "El argumento debe ser una instancia de CentroDeSalud."
            )

        pacientes_en_espera = [
            receptor
            for receptor in self.receptores.values()
            if receptor.centro_salud_asociado == centro_de_salud
        ]
        return pacientes_en_espera

    def buscar_prioridad_receptor(self, receptor_dni: str) -> Optional[int]:
        """
        Busca la prioridad de un receptor en la lista de espera.

        Args:
            receptor_dni (str): El DNI del receptor a buscar.

        Returns:
            Optional[int]: La prioridad del receptor si se encuentra, None en caso contrario.

        Raises:
            TypeError: Si el DNI del receptor no es una cadena.
        """
        if not isinstance(receptor_dni, str):
            raise TypeError("El DNI del receptor debe ser una cadena.")

        if receptor_dni not in self.receptores:
            return None  # El receptor no está en la lista

        return self.receptores[receptor_dni].prioridad

    def imprimir_listado_donantes(self) -> None:
        """
        Imprime el listado de pacientes donantes.
        """
        print("Listado de Donantes:")
        for donante in self.donantes.values():
            print(donante)

    def imprimir_listado_receptores(self) -> None:
        """
        Imprime el listado de pacientes receptores.
        """
        print("Listado de Receptores:")
        for receptor in self.receptores.values():
            print(receptor)

    def _buscar_coincidencias_donante(self, donante: "Donante") -> None:
        """
        Busca y procesa coincidencias entre los órganos disponibles del donante y los receptores en espera.

        Args:
            donante (Donante): El donante para el cual se buscarán coincidencias.
        """

        for organo_donado in donante.organos_a_donar:
            posibles_receptores = [
                receptor
                for receptor in self.receptores.values()
                if receptor.organo_a_recibir.nombre == organo_donado.nombre
                and receptor.tipo_sangre == donante.tipo_sangre
            ]

            if posibles_receptores:
                #  Seleccionar el receptor de mayor prioridad (menor valor numérico)
                receptor_seleccionado = min(
                    posibles_receptores, key=lambda receptor: receptor.prioridad
                )
                self._procesar_trasplante(donante, receptor_seleccionado, organo_donado)

    def _buscar_coincidencias_receptor(self, receptor: "Receptor") -> None:
        """
        Busca y procesa coincidencias entre el órgano necesitado por el receptor y los donantes disponibles.

        Args:
            receptor (Receptor): El receptor para el cual se buscarán coincidencias.
        """

        posibles_donantes = [
            donante
            for donante in self.donantes.values()
            for organo_donado in donante.organos_a_donar
            if organo_donado.nombre == receptor.organo_a_recibir.nombre
            and donante.tipo_sangre == receptor.tipo_sangre
        ]

        if posibles_donantes:
            #  Seleccionar el primer donante encontrado (simplificación)
            donante_seleccionado = posibles_donantes[0]
            self._procesar_trasplante(
                donante_seleccionado, receptor, receptor.organo_a_recibir
            )

    def _procesar_trasplante(
        self, donante: "Donante", receptor: "Receptor", organo: "Organo"
    ) -> None:
        """
        Procesa el protocolo de trasplante entre un donante y un receptor.

        Args:
            donante (Donante): El donante del órgano.
            receptor (Receptor): El receptor del órgano.
            organo (Organo): El órgano a trasplantar.
        """

        centro_salud_donante = donante.centro_salud_asociado
        centro_salud_receptor = receptor.centro_salud_asociado

        #  Simulación de la obtención de datos de distancia y tráfico (reemplazar con lógica real si es posible)
        distancia = 150  #  Ejemplo: Distancia en km
        trafico = 0.2  #  Ejemplo: Nivel de tráfico (0 a 1)

        vehiculo = centro_salud_donante.seleccionar_vehiculo(
            distancia, centro_salud_receptor.direccion, receptor.grado_urgencia
        )
        cirujano = centro_salud_donante.asignar_cirujano(datetime.date.today())

        #  Simular la ablación del órgano
        organo.set_fecha_hora_ablacion(datetime.datetime.now())
        donante.quitar_organo_donado(organo)

        #  Simular el tiempo de viaje
        tiempo_viaje = vehiculo.calcular_tiempo_viaje(distancia, trafico)
        print(f"Tiempo estimado de viaje: {tiempo_viaje:.2f} horas")

        #  Verificar viabilidad del órgano (simplificado)
        if tiempo_viaje > 20:  #  Ejemplo: Límite de tiempo de 20 horas
            print(
                "¡Alerta! El tiempo de viaje excede el límite de viabilidad del órgano."
            )
            receptor.set_estado("Inestable")
            receptor.set_prioridad(1)  #  Máxima prioridad
            return

        #  Simular el trasplante
        exito_trasplante = cirujano.calcular_exito_trasplante(organo)

        if exito_trasplante:
            print("Trasplante Exitoso")
            self.quitar_receptor(receptor)
        else:
            print("Trasplante Fallido")
            receptor.set_estado("Inestable")
            receptor.set_prioridad(1)  #  Máxima prioridad

    def quitar_donantes_sin_organos(self) -> None:
        """
        Quita de la lista de donantes a aquellos cuyos órganos ya han sido utilizados en su totalidad.
        """

        donantes_a_quitar: List["Donante"] = [
            donante for donante in self.donantes.values() if not donante.organos_a_donar
        ]
        for donante in donantes_a_quitar:
            self.quitar_donante(donante)

    def buscar_receptores_por_centro_de_salud(
        self, centro_salud_nombre: str
    ) -> List["Receptor"]:
        """
        Busca todos los receptores asociados a un centro de salud específico por su nombre.

        Args:
            centro_salud_nombre (str): El nombre del centro de salud para el cual se busca los receptores.

        Returns:
            List[Receptor]: Una lista de receptores asociados al centro de salud dado.

        Raises:
            ValueError: Si no existe un centro de salud con el nombre proporcionado.
        """
        if centro_salud_nombre not in self.centros_de_salud:
            raise ValueError(
                f"No existe un centro de salud con el nombre: {centro_salud_nombre}"
            )

        centro_salud = self.centros_de_salud[centro_salud_nombre]
        receptores_del_centro = [
            receptor
            for receptor in self.receptores.values()
            if receptor.centro_salud_asociado == centro_salud
        ]
        return receptores_del_centro