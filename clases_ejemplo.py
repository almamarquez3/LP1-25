
class cPersona:

    def __init__(self, nombre, apellido, edad):  # siempre se ejecuta cuando se inicia la clase.
                                                 # se usa para asignar valores a propiedades de los objetos u otras operaciones que se hacen a la hora de crear una clase
        self.nombre = nombre
        self.apellido=apellido
        self.edad = edad                        # self es una referencia a la instancia de la clase

    def presentacion(self):
        return f'hola, mi nombre es {self.nombre} {self.apellido} y tengo {self.edad} años' 

class cPerro:
    def __init__(self, nombre, raza, edad):
        self.nombre = nombre
        self.raza = raza
        self.edad = edad
    
    def ladrar(self):
        return "guau guau"


taylor= cPersona("Taylor", "Swift", 35)  # instanciar una clase

apolo= cPerro("Apolo", "Bulldog Frances", 5)

print(taylor.presentacion()) # se llama a la funcion presentacion de la clase cPersona

print(apolo.ladrar())