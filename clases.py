class cPersona:
    def __init__(self, nombre):
        self.__nombre = nombre

    def saludar(self):
        return f"Hola, soy {self.__nombre}"
    def yo_soy(self):
        return f"{self.__nombre}"
    
class cSemaforo:
    def __init__(self, color:str):
        self.__color = color
    def debe_parar(self)->bool:
        if self.__color == "rojo":
            return True
        if self.__color == "amarillo":
            return False
        if self.__color == "verde":
            return False
        else: return False
    def puede_cruzar(self)->bool:
        if self.__color == "rojo":
            return False
        if self.__color == "amarillo":
            return False
        if self.__color == "verde":
            return True
        else: return False
    def siguiente_color(self)->str:
        if self.__color == "rojo":
            self.__color = "verde"
            return "Luz_verde"
        if self.__color == "amarillo":
            self.__color = "rojo"
            return "Luz_roja"
        if self.__color == "verde":
            self.__color = "amarillo"
            return "Luz_amarilla"
        else: return "Color_invalido"
class cDibujador:
    def dibujo_perro():
        print("   ^..^      /")
        print("  /_/\\\\_____/")
        print("     /\\\\   /\\\\")
        print("    /  \\\\ /  \\\\")
    def dibujo_gato():
        print("                       _")
        print("                      | |")
        print("                      | |")
        print("                      | |")
        print(" |\\                   | |")
        print(" /, ~\\                / /")
        print("X     `-.....-------./ /")
        print(" ~-. ~  ~              |")
        print("    \\             /    |")
        print("     \\  /_     ___\\   /")
        print("     | /\\ ~~~~~   \\ |")
        print("     | | \\        || |")
        print("     | |\\ \\       || )")
        print("    (_/ (_/      ((_/")
    def dibujo_pez():
        print("     /`·.¸")
        print("    /¸...¸`:·")
        print(" ¸.·´  ¸   `·.¸.·´)")
        print(": © ):´;      ¸  {")
        print(" `·.¸ `·  ¸.·´\\`·¸)")
        print("     `\\´´\\¸.·")
    def se_dibujarlo(animal:str):
        if animal == "perro":
            print("Puedo dibujarlo")
        if animal == "gato":
            print("Puedo dibujarlo")
        if animal == "pez":
            print("Puedo dibujarlo")
        else: print("No puedo dibujarlo")
class cTrayecto():
        def mostrar_posicion(km:int)->str:
            if km >=0 and km <=1:
                print("Casa de pepe")
            if km == 2:
                print("Casa de Ana")
            if km == 3:
                print("Casa de Miguel")
            if km == 4:
                print("Avenida")
            if km == 5:
                print("Refugio de mascotas")
            if km == 6:
                print("Avenida")
            if km == 7:
                print("Casa del novio de Ana")
class cPerro():
    
    def __init__(self,duenio:None):
        pass
    def ser_adoptado(self,duenio:any):
        self.duenio = duenio
oliver=cPerro("Juan")
oliver.ser_adoptado("Juancc")
print(oliver.duenio)
