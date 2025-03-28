from objetos.dibujador import Dibujador



class Pez:

    
    def __init__(self):
        self.dueno = None
    
    def ser_adoptado(self, dueno):
        if self.dueno is None:
            self.dueno = dueno
    
    def hacer_sonido(self):
        return "glu glu"
    
    def __str__(self):
        return self.dibujador.dibujo_pez()