class HogarDeMascotas:


    def __init__(self):
        self.mascota_en_transito = None
    
    def cuidar_mascota(self, mascota):
        if self.mascota_en_transito is None:
            self.mascota_en_transito = mascota
    
    def dar_en_adopcion(self, dueno):
        self.mascota_en_transito.ser_adoptado(dueno)
        self.mascota_en_transito = None