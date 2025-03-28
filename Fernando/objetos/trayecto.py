class Trayecto:


    def mostrar_posicion(self, km: int) -> str:
        if km <=1:
            return "Casa de pepe"
        elif km <= 2:
            return "Casa de Ana"
        elif km <= 3:
            return "Casa de Miguel"
        elif km <= 4:
            return "Avenida"
        elif km <= 5:
            return "Refugio de mascotas"
        elif km <= 6:
            return "Avenida"
        elif km <= 7:
            return "Casa del novio de Ana"