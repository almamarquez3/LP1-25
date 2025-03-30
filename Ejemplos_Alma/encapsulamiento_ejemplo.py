
class cMedico:

    def __init__ (self, nombre, especialidad, matricula):
        self.nombre = nombre
        self.especialidad = especialidad
        self.__matricula=matricula
    
    
    def set_matricula(self, matricula):
        self.__matricula = matricula
    
    def get_matricula(self):
        return self.__matricula


Sheppard=cMedico("Derek", "Neurocirujano", "00000000")

Sheppard.set_matricula("147852369")

#print(Sheppard.get_matricula())

print(Sheppard.matricula)

# El encapsulamiento oculta los detalles internos de un objeto y solo permite 
# modificar sus atributos mediante métodos específicos, 
# asegurando que los datos sean controlados y protegidos.


