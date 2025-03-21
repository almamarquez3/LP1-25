class Auto:


    def __init__(self):
        self.combustible = 55
        self.posicion = 0
    
    def moverse(self):
        # esto podria ser un if tranquilamente
        puede_moverse = self.combustible >= 5
        if puede_moverse:
            self.combustible -= 5
            self.posicion += 600
        return puede_moverse
    
    def cargar_combustible(self, litros):
        # se podria hacer en mas lineas usando ifs
        total = self.combustible + litros
        sobrante = max(0, total - 60)
        self.combustible = min(60, total)
        return sobrante

    def obtener_posicion(self):
        return self.posicion