import datetime
from typing import List, Optional
from organos.organo import Organo
from centrosdesalud.vehiculo import Vehiculo   
from centrosdesalud.centro_de_salud import CentroDeSalud
from centrosdesalud.cirujano import Cirujano
from pacientes.donante import Donante
from pacientes.receptor import Receptor
from sistema.incucai import INCUCAI
from centrosdesalud.terrestre import Terrestre
from centrosdesalud.helicoptero import Helicoptero

def main():
    #  Crear algunos objetos
    corazon = Organo(nombre="Corazón")
    rinon = Organo(nombre="Riñón")

    centro_salud_1 = CentroDeSalud(
        nombre="Hospital Central",
        direccion="Calle Principal 123",
        partido="Capital",
        provincia="Buenos Aires",
        telefono="123-456-7890",
        cirujanos=[],
        vehiculos=[],
    )

    cirujano_1 = Cirujano(nombre="Dr. Smith", especialidad="Cardiovascular")
    centro_salud_1.cirujanos.append(cirujano_1)

    terrestre_1 = Terrestre(velocidad=80)
    helicoptero_1 = Helicoptero(velocidad=250)
    centro_salud_1.vehiculos.extend([terrestre_1, helicoptero_1])

    donante_1 = Donante(
        nombre="Juan Perez",
        dni="12345678",
        fecha_nacimiento=datetime.date(1970, 1, 1),
        sexo="M",
        telefono="987-654-3210",
        tipo_sangre="A+",
        centro_salud_asociado=centro_salud_1,
        estado="Crítico",
        fecha_hora_fallecimiento=datetime.datetime(2024, 3, 10, 10, 0, 0),
        fecha_hora_comienzo_ablacion=datetime.datetime(2024, 3, 10, 12, 0, 0),
        organos_a_donar=[corazon, rinon],
    )

    receptor_1 = Receptor(
        nombre="Maria Gomez",
        dni="87654321",
        fecha_nacimiento=datetime.date(1985, 5, 15),
        sexo="F",
        telefono="555-123-4567",
        tipo_sangre="A+",
        centro_salud_asociado=centro_salud_1,
        estado="En Espera",
        organo_a_recibir=corazon,
        fecha_agregado_lista_espera=datetime.date(2024, 3, 1, 0, 0, 0),
        prioridad=1,
        patologia="Cardiomiopatía",
        grado_urgencia=1,
    )

    incucai = INCUCAI()

    #  Registrar pacientes
    try:
        incucai.registrar_paciente(donante_1)
        incucai.registrar_paciente(receptor_1)
    except ValueError as e:
        print(f"Error al registrar paciente: {e}")

    #  Imprimir listados
    incucai.imprimir_listado_donantes()
    incucai.imprimir_listado_receptores()

    #  Buscar receptores por centro de salud
    receptores_hospital = incucai.buscar_receptores_por_centro_de_salud(
        centro_salud_nombre="Hospital Central"
    )
    print("\nReceptores en Hospital Central:")
    for receptor in receptores_hospital:
        print(receptor)

    #  Simular un trasplante (esto es solo un ejemplo, la lógica real es más compleja)
    if donante_1.organos_a_donar and receptor_1.organo_a_recibir:
        incucai._procesar_trasplante(donante_1, receptor_1, corazon)

if __name__ == "__main__":
    main()