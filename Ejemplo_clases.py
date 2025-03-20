from clases import cAuto
class cPersona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad

    @property
    def nombre(self):
        return self.__nombre

    @property
    def edad(self):
        return self.__edad

    def __str__(self):
        return f"Nombre: {self.__nombre}, Edad: {self.__edad}"
    def batatonica(self):
        return "Batatonica"
    
class cEmpleado(cPersona):
    def __init__(self, nombre, edad, salario):
        super().__init__(nombre, edad)
        self.__salario = salario

    @property
    def salario(self):
        return self.__salario

    def __str__(self):
        return f"{super().__str__()}, Salario: {self.__salario}"
    def batatonica(self):
        return "Batatonica2"

# Crear un objeto de la clase cEmpleado
# empleado = cEmpleado("Juan", 30, 1000)
# var=empleado.batatonica()
# print(empleado)
autito = cAuto("Ford", "Fiesta", 2019)
print(autito)
