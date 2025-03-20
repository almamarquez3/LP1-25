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
    def hacer_sonido(self)->str:
        return "Guau"
class cGato:
    def __init__(self,duenio:None):
        pass

    def ser_adoptado(self,duenio:any):
        self.duenio = duenio

    def hacer_sonido(self)->str:
        return "Miau"
class cPez:
    def __init__(self,duenio:None):
        pass

    def ser_adoptado(self,duenio:any):
        self.duenio = duenio

    def hacer_sonido(self)->str:
        return "Glu Glu"
class cHogar_mascotas():
    def __init__(self, mascota:None):
        pass

    def cuidar_mascota(self, mascota:cPerro|cGato|cPez):
        if self.mascota == None:
            self.mascota = mascota

    def dar_en_adopcion(self,duenio:any)->bool:
        if self.mascota != None:
            print(f"Se ha dado en adopcion a {duenio}")
            self.mascota = None
            return True
        else: 
            print("No hay mascota para dar en adopcion")
            return False
class cCuenta_bancaria:
    def __init__(self):
        self.saldo = 0
    def depositar(self, monto:int)->bool:
        if monto > 0:
            self.saldo += monto
            return True
    def debitar(self, monto:int)->bool:
        if monto > 0 and monto <= self.saldo:
            self.saldo -= monto
            print("Debito exitoso")
            return True
        else:
            print("Debito fallido")
            return False
        
class cAuto:
    def __init__(self):
        self.tanque=50
        self.posicion=0
    def moverse(self):
        if self.tanque >= 5:
            self.tanque -= 5
            self.posicion += 600
            print("Movimiento exitoso")
            return True
        else:
            print("Movimiento fallido")
            return False
    def cargar_combustible(self,litros:int)->int:
        if(self.tanque + litros > 60):
            self.tanque=60
            return self.tanque+litros-60
        if(self.tanque + litros < 60):
            self.tanque+=litros
            return 0
    def mostrar_posicion(self)->int:
        return self.posicion
class cPepe:
    def __init__(self,nombre:str,cuenta:cCuenta_bancaria):
        self.nombre=nombre
        self.cuenta=cuenta
        self.auto=None
        self.acompaniante=None
    def comprar_auto(self,auto:cAuto)->bool:
        if self.cuenta.saldo >= 7000000:
            self.auto=auto
            self.cuenta.debitar(7000000)
            return True
        else:
            return False
    def manejar(self,semaforo:cSemaforo)->bool:
        if semaforo.debe_parar()==False and self.auto.moverse()==True:
            print("Puede viajar")
            return True
        if semaforo.debe_parar()==True:
            print("Ahora no puedo")
            return False
    def tener_acompaniante(self,acompaniante:any):
        if(self.auto!=None and self.acompaniante==None):
            self.acompaniante=acompaniante
            return True
        else: print("No puede tener nuevo acompaniante")
        
            
        
    
        
