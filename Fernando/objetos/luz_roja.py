class LuzRoja:


    def debe_parar(self):
        return True
    
    def puede_cruzar(self):
        return False
    
    def siguiente_color(self):
        # Como se importan circularmente
        # esta solución es la mas simple
        # pero no la mas feliz
        # debe quedar claro que se escribe
        # por tener importaciones circulares
        from objetos.luz_verde import LuzVerde
        LUZ_VERDE = LuzVerde()
        return LUZ_VERDE