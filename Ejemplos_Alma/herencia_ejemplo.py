
class cPersona:

    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def saludo(self):
        print("Hola, mi nombre es", self.nombre, self.apellido)


class cEstudiante(cPersona):
    
    def __init__(self, nombre, apellido, edad, carrera):
        super().__init__(nombre, apellido, edad) # Llamamos al constructor de cPersona
        self.carrera = carrera

    def que_estudia(self):
        print("soy estudiante de", self.carrera)


Juancito=cEstudiante("Juancito", "Fulanito", 20, "Ingenieria Biomedica")

Juancito.saludo()           #uso el metodo heredado de cPersona
Juancito.que_estudia()      #uso el metodo propio de cEstudiante