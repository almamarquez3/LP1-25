
class Persona:
    def __init__(self, nombre, apellido, saturacion_o2, temperatura, frec_cardiaca, presion_sistolica, presion_diastolica, enfermedad=None):
        self.nombre = nombre
        self.apellido= apellido
        self.saturacion_o2 = saturacion_o2
        self.temperatura = temperatura
        self.frec_cardiaca = frec_cardiaca
        self.presion_sistolica = presion_sistolica
        self.presion_diastolica = presion_diastolica
        self.enfermedad = enfermedad
    

    def contagiar(self, persona):
        if persona.enfermedad==None:
            persona.enfermedad = self.enfermedad
            print('\nPaciente', persona.nombre, 'contagiado con', self.enfermedad.nombre)
        else: 
            pass
    

class Enfermedad:
    def __init__(self, nombre):
        self.nombre = nombre

    
    def enfermar_pacientes(self, persona):
        if self.nombre=='tuberculosis':
            persona.saturacion_o2=persona.saturacion_o2-persona.saturacion_o2*0.1
            persona.temperatura=persona.temperatura+5

        elif self.nombre=='neumonia_viral':
            persona.frec_cardiaca=persona.frec_cardiaca+15
            persona.saturacion_o2=persona.saturacion_o2-persona.saturacion_o2*0.1
            persona.temperatura=persona.temperatura+2
        
        elif self.nombre=='meningitis_bacteriana':
            persona.frec_cardiaca=persona.frec_cardiaca+10
            persona.presion_sistolica=persona.presion_sistolica+10
            persona.presion_diastolica=persona.presion_diastolica+5
            persona.temperatura=persona.temperatura+2

        else :
            print('Enfermedad no encontrada')

class Medico:

    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

    def agregar_pacientes(self, persona, sistemaUCI):
        sistemaUCI.lista_pacientes.append(persona)

    def curar_pacientes(self, persona):

        while persona.presion_sistolica>=120 and persona.presion_diastolica>=80 and persona.frec_cardiaca>=75 and persona.saturacion_o2<=98 and persona.temperatura>=36.8:
            persona.frec_cardiaca = persona.frec_cardiaca - 5
            persona.presion_sistolica = persona.presion_sistolica - 10
            persona.presion_diastolica = persona.presion_diastolica - 5
            persona.temperatura = persona.temperatura - 2
            persona.saturacion_o2 = persona.saturacion_o2 + persona.saturacion_o2 * 0.1
        
        print('\nPaciente', persona.nombre, 'dado de alta por el/la Dr(a)', self.nombre)
        persona.enfermedad = None

class Sistema_UCI:

    def __init__(self, lista_pacientes):
        self.lista_pacientes = lista_pacientes
    
    def chequear_signos(self, persona):
        if persona.presion_sistolica>=180 or persona.presion_diastolica>=110 or persona.frec_cardiaca>=130 or persona.saturacion_o2<=85 or persona.temperatura>=39.2:
            print('\nALERTA Paciente', persona.nombre, 'en estado critico')
        


        