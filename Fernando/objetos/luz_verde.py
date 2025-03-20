class LuzVerde:


    def debe_parar(self):
        return False
    
    def puede_cruzar(self):
        return True
    
    def siguiente_color(self):
        # Como se importan circularmente
        # esta solución es la mas simple
        # pero no la mas feliz
        # debe quedar claro que se escribe
        # por tener importaciones circulares
        from objetos.luz_amarilla import LuzAmarilla
        LUZ_AMARILLA = LuzAmarilla()
        return LUZ_AMARILLA