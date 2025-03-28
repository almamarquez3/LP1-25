from cSistemaUCI import *

if __name__ == '__main__':

    tuberculosis=Enfermedad('tuberculosis')
    neumonia_viral=Enfermedad('neumonia_viral')
    meningitis_bacteriana=Enfermedad('meningitis_bacteriana')

    paciente1=Persona('Juan', 'Rodriguez', 90, 85, 21, 85, 39.2, tuberculosis)
    paciente2=Persona('Maria', 'Gomez', 180, 110, 130, 85, 39.2, neumonia_viral)
    paciente3=Persona('Pedro', 'Lopez', 180, 110, 170, 109, 39.2, meningitis_bacteriana)
    paciente4=Persona('Ana', 'Martinez', 180, 110, 130, 85, 39.2)

    paciente1.contagiar(paciente4)

    Dr_felipe=Medico('Felipe', 'Gonzalez')
    Dra_lara=Medico('Lara', 'Gutierrez')
    Dr_strange=Medico('Stephen', 'Strange')

    sistemaUCI=Sistema_UCI([paciente1, paciente2])
    Dr_felipe.agregar_pacientes(paciente3, sistemaUCI)
    Dra_lara.agregar_pacientes(paciente4, sistemaUCI)

    sistemaUCI.chequear_signos(paciente1)
    sistemaUCI.chequear_signos(paciente2)
    sistemaUCI.chequear_signos(paciente3)

    Dr_felipe.curar_pacientes(paciente1)
    Dra_lara.curar_pacientes(paciente2)

    meningitis_bacteriana.enfermar_pacientes(paciente3)

    sistemaUCI.chequear_signos(paciente3)

    Dr_strange.curar_pacientes(paciente3)
    
    Dra_lara.curar_pacientes(paciente4)