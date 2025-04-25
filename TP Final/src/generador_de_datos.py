import datetime
import random
import uuid  # Para generar DNI únicos
from pacientes.paciente import Paciente
from pacientes.donante import Donante
from pacientes.receptor import Receptor
from organos.organo import Organo
from centrosdesalud.centro_de_salud import CentroDeSalud
from centrosdesalud.cirujano import Cirujano
from centrosdesalud.vehiculo import Vehiculo
from centrosdesalud.terrestre import Terrestre
from centrosdesalud.helicoptero import Helicoptero
from centrosdesalud.avion import Avion
from sistema.incucai import INCUCAI

#  Lista de nombres, apellidos, órganos, etc. para generar datos aleatorios
nombres = ["Juan", "Maria", "Carlos", "Ana", "Luis", "Sofia", "Pedro", "Laura"]
apellidos = ["Perez", "Gomez", "Rodriguez", "Lopez", "Garcia", "Martinez", "Fernandez", "Diaz"]
organos_posibles = ["Corazón", "Hígado", "Riñón", "Pulmones", "Páncreas", "Intestino"]
provincias_argentinas = [
    "Buenos Aires", "Córdoba", "Santa Fe", "Mendoza", "Tucumán", "Salta", "Entre Ríos",
    "Misiones", "Chaco", "Corrientes", "Jujuy", "Río Negro", "Neuquén", "Formosa",
    "San Juan", "San Luis", "La Rioja", "Catamarca", "Santiago del Estero", "La Pampa",
    "Santa Cruz", "Tierra del Fuego", "Chubut"
]
especialidades_cirujano = {
    "Corazón": "Cardiovascular",
    "Pulmones": "Pulmonar",
    "Piel": "Plástico",
    "Córneas": "Plástico",
    "Huesos": "Traumatólogo",
    "Intestino": "Gastroenterólogo",
    "Riñón": "Gastroenterólogo",
    "Hígado": "Gastroenterólogo",
    "Páncreas": "Gastroenterólogo"
}
patologias = ["Cardiomiopatía", "Insuficiencia Renal", "Fibrosis Quística", "Cirrosis", "Pancreatitis"]
tipos_sangre = ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"]


def generar_fecha_aleatoria(inicio, fin):
    """Genera una fecha aleatoria entre dos fechas."""
    return inicio + datetime.timedelta(
        seconds=random.randint(0, int((fin - inicio).total_seconds()))
    )


def generar_dni_unico():
    """Genera un DNI único (simulado)."""
    return str(uuid.uuid4().int)[:8]  #  Genera un número único de 8 dígitos


def crear_organos(cantidad):
    organos = []
    for _ in range(cantidad):
        nombre = random.choice(organos_posibles)
        organos.append(Organo(nombre=nombre))
    return organos


def crear_aviones(cantidad):
    aviones = []
    for _ in range(cantidad):
        velocidad = random.randint(800, 1000)  # Velocidad típica de un avión comercial
        aviones.append(Avion(velocidad=velocidad))
    return aviones


def crear_helicopteros(cantidad):
    helicopteros = []
    for _ in range(cantidad):
        velocidad = random.randint(200, 300)  # Velocidad típica de un helicóptero
        helicopteros.append(Helicoptero(velocidad=velocidad))
    return helicopteros


def crear_terrestres(cantidad):
    terrestres = []
    for _ in range(cantidad):
        velocidad = random.randint(60, 120)  # Velocidad típica de un vehículo terrestre
        terrestres.append(Terrestre(velocidad=velocidad))
    return terrestres


def crear_centros_de_salud(cantidad, cirujanos, vehiculos):
    centros_de_salud = {}
    cirujanos_asignados = random.sample(cirujanos, len(cirujanos))  # Mezclar cirujanos
    vehiculos_asignados = {
        "Avion": random.sample(vehiculos["Avion"], len(vehiculos["Avion"])),
        "Helicoptero": random.sample(vehiculos["Helicoptero"], len(vehiculos["Helicoptero"])),
        "Terrestre": random.sample(vehiculos["Terrestre"], len(vehiculos["Terrestre"]))
    }
    for i in range(cantidad):
        nombre = f"Hospital {random.choice(provincias_argentinas)} #{i + 1}"
        direccion = f"Calle {random.randint(1, 1000)}, {random.choice(provincias_argentinas)}"
        partido = "Capital"  # Simplificado
        provincia = random.choice(provincias_argentinas)
        telefono = f"{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}"
        #  Asignar cirujanos al centro de salud (distribución equitativa)
        num_cirujanos_centro = len(cirujanos) // cantidad
        cirujanos_del_centro = cirujanos_asignados[i * num_cirujanos_centro:(i + 1) * num_cirujanos_centro]
        #  Asignar vehículos al centro de salud (distribución equitativa)
        num_vehiculos_avion = len(vehiculos["Avion"]) // cantidad if cantidad else 0
        num_vehiculos_helicoptero = len(vehiculos["Helicoptero"]) // cantidad if cantidad else 0
        num_vehiculos_terrestre = len(vehiculos["Terrestre"]) // cantidad if cantidad else 0
        vehiculos_del_centro = []
        if num_vehiculos_avion:
            vehiculos_del_centro.extend(vehiculos_asignados["Avion"][i * num_vehiculos_avion:(i + 1) * num_vehiculos_avion])
        if num_vehiculos_helicoptero:
            vehiculos_del_centro.extend(vehiculos_asignados["Helicoptero"][i * num_vehiculos_helicoptero:(i + 1) * num_vehiculos_helicoptero])
        if num_vehiculos_terrestre:
            vehiculos_del_centro.extend(vehiculos_asignados["Terrestre"][i * num_vehiculos_terrestre:(i + 1) * num_vehiculos_terrestre])
        centros_de_salud[nombre] = CentroDeSalud(
            nombre=nombre,
            direccion=direccion,
            partido=partido,
            provincia=provincia,
            telefono=telefono,
            cirujanos=cirujanos_del_centro,
            vehiculos=vehiculos_del_centro,
        )
    return centros_de_salud


def crear_cirujanos(cantidad):
    cirujanos = []
    for i in range(cantidad):
        nombre = f"Dr. {random.choice(nombres)} {random.choice(apellidos)}"
        organo = random.choice(list(especialidades_cirujano.keys()))
        especialidad = especialidades_cirujano[organo]
        cirujanos.append(Cirujano(nombre=nombre, especialidad=especialidad))
    return cirujanos


def crear_pacientes(cantidad, centros_de_salud, es_donante=False):
    pacientes = []
    for _ in range(cantidad):
        nombre = f"{random.choice(nombres)} {random.choice(apellidos)}"
        dni = generar_dni_unico()
        fecha_nacimiento = generar_fecha_aleatoria(
            datetime.date(1950, 1, 1), datetime.date(2000, 12, 31)
        )
        sexo = random.choice(["M", "F"])
        telefono = f"{random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}"
        tipo_sangre = random.choice(tipos_sangre)
        centro_salud_asociado = random.choice(list(centros_de_salud.values()))
        hla_match = random.randint(0, 6)  # Generar un valor aleatorio para HLA

        if es_donante:
            fecha_hora_fallecimiento = generar_fecha_aleatoria(
                datetime.datetime(2024, 1, 1, 0, 0, 0), datetime.datetime(2025, 4, 20, 23, 59, 59)
            )
            fecha_hora_comienzo_ablacion = fecha_hora_fallecimiento + datetime.timedelta(hours=random.randint(1, 24))
            num_organos_a_donar = random.randint(1, 3)
            num_cirujanos_disponibles = len(centro_salud_asociado.cirujanos)
            num_organos_a_donar = min(num_organos_a_donar, num_cirujanos_disponibles)
            organos_a_donar = random.sample(centro_salud_asociado.cirujanos, num_organos_a_donar)  # Usar cirujanos como placeholder para órganos
            paciente = Donante(
                nombre=nombre,
                dni=dni,
                fecha_nacimiento=fecha_nacimiento,
                sexo=sexo,
                telefono=telefono,
                tipo_sangre=tipo_sangre,
                centro_salud_asociado=centro_salud_asociado,
                estado="Crítico",
                fecha_hora_fallecimiento=fecha_hora_fallecimiento,
                fecha_hora_comienzo_ablacion=fecha_hora_comienzo_ablacion,
                organos_a_donar=organos_a_donar,
                hla_match=hla_match,  # Asignar el valor de HLA
            )
        else:  # Receptor
            nombre_organo_a_recibir = random.choice(organos_posibles)
            organo_a_recibir = Organo(nombre=nombre_organo_a_recibir)
            fecha_agregado_lista_espera = generar_fecha_aleatoria(
                datetime.datetime(2023, 1, 1, 0, 0, 0), datetime.datetime(2024, 3, 1, 23, 59, 59)
            ).date()
            prioridad = random.randint(1, 100)  # 1 es la más alta
            patologia = random.choice(patologias)
            grado_urgencia = random.randint(1, 3)  # Ejemplo: 1-Alta, 2-Media, 3-Baja
            paciente = Receptor(
                nombre=nombre,
                dni=dni,
                fecha_nacimiento=fecha_nacimiento,
                sexo=sexo,
                telefono=telefono,
                tipo_sangre=tipo_sangre,
                centro_salud_asociado=centro_salud_asociado,
                estado="En Espera",
                organo_a_recibir=organo_a_recibir,
                fecha_agregado_lista_espera=fecha_agregado_lista_espera,
                prioridad=prioridad,
                patologia=patologia,
                grado_urgencia=grado_urgencia,
                hla_match=hla_match,  # Asignar el valor de HLA
            )
        pacientes.append(paciente)
    return pacientes


def creador_de_datos():
    #  Crear órganos
    organos = crear_organos(10)  # 10 órganos de ejemplo

    #  Crear vehículos
    aviones = crear_aviones(3)
    helicopteros = crear_helicopteros(10)
    terrestres = crear_terrestres(45)
    vehiculos = {
        "Avion": aviones,
        "Helicoptero": helicopteros,
        "Terrestre": terrestres
    }

    #  Crear cirujanos
    cirujanos = crear_cirujanos(45)

    #  Crear centros de salud
    centros_de_salud = crear_centros_de_salud(45, cirujanos, vehiculos)

    #  Crear pacientes (donantes y receptores)
    donantes = crear_pacientes(500, centros_de_salud, es_donante=True)
    receptores = crear_pacientes(500, centros_de_salud, es_donante=False)

    incucai = INCUCAI(
        donantes={donante.dni: donante for donante in donantes},
        receptores={receptor.dni: receptor for receptor in receptores},
        centros_de_salud=centros_de_salud,
    )

    #  Ejemplo de operaciones (puedes agregar más pruebas aquí)
    incucai.imprimir_listado_donantes()
    incucai.imprimir_listado_receptores()

    #  Buscar receptores por centro de salud (ejemplo)
    centro_salud_ejemplo = random.choice(list(incucai.centros_de_salud.values()))
    receptores_centro = incucai.buscar_receptores_por_centro_de_salud(centro_salud_nombre=centro_salud_ejemplo.nombre)
    print(f"\nReceptores en {centro_salud_ejemplo.nombre}:")
    for receptor in receptores_centro:
        print(receptor)

    return incucai