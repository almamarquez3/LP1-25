from seccion2.cuenta_bancaria import CuentaBancaria
from seccion2.auto import Auto



class Pepe:


    def __init__(self):
        self.cuenta = CuentaBancaria()
        self.auto = None
        self.companero = None
    
    def saludar(self):
        print("Hola soy Pèpe")
    
    def yo_soy(self):
        return "Pepe"
    
    def comprar_auto(self):
        pudo_comprar = False
        if self.auto is None:
            pudo_comprar = self.cuenta.debitar(7000000)
            if pudo_comprar:
                self.auto = Auto()
        return pudo_comprar
    
    def cobrar_sueldo(self):
        self.cuenta.depositar(2000000)
    
    def manejar(self, semaforo):
        # Esta quizas es la solucion mas concisa
        # lo mas probable es que las respuestas sean
        # mas complejas. Lo importante es que no usen
        # el moverse si el semaforo estaba en rojo
        if semaforo.se_puede_seguir() and self.auto.moverse():
            return "Pude viajar"
        return "Ahora no puedo"
    
    def tener_acompanante(self, acompanante):
        if self.companero is None and not self.auto is None:
            self.companero = acompanante