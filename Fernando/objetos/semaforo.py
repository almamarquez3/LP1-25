from objetos.luz_roja import LuzRoja



class Semaforo:


    def __init__(self):
        self.luz = LuzRoja()
    
    def siguiente_color(self):
        self.luz = self.luz.siguiente_color()
    
    def se_puede_seguir(self):
        return not self.luz.debe_parar()

    def se_puede_cruzar(self):
        return self.luz.puede_cruzar()