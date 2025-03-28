from objetos.dibujador import Dibujador



class Gato:


    def __init__(self):
        self.dueno = None
        self.intentos_adopcion = 0
        self.dibujador = Dibujador()
    
    def ser_adoptado(self, dueno):
        if self.dueno is None:
            self.dueno = dueno
        else:
            self.intentos_adopcion += 1
            if self.intentos_adopcion == 3:
                self.dueno = None
    
    def hacer_sonido(self):
        return "miau"
    
    def __str__(self):
        return self.dibujador.dibujo_gato()