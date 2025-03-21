from objetos.ana import Ana
from objetos.pepe import Pepe
from seccion2.hogar_de_mascotas import HogarDeMascotas
from seccion2.gato import Gato
from objetos.semaforo import Semaforo
from objetos.trayecto import Trayecto
from objetos.conversor_de_unidades import ConversorDeUnidades




def main():
    PEPE = Pepe()
    ANA = Ana()
    HOGAR = HogarDeMascotas()
    SEMAFORO = Semaforo()
    GATO = Gato()
    TRAYECTO = Trayecto()
    CONVERSOR = ConversorDeUnidades()
    
    HOGAR.cuidar_mascota(GATO)

    PEPE.cobrar_sueldo()
    PEPE.cobrar_sueldo()
    PEPE.cobrar_sueldo()
    PEPE.cobrar_sueldo()
    PEPE.comprar_auto()

    print(PEPE.manejar(SEMAFORO))
    posicion = CONVERSOR.metros_a_kilometros(PEPE.mirar_posicion())
    print(TRAYECTO.mostrar_posicion(posicion))
    SEMAFORO.siguiente_color()

    print(PEPE.manejar(SEMAFORO))
    posicion = CONVERSOR.metros_a_kilometros(PEPE.mirar_posicion())
    print(TRAYECTO.mostrar_posicion(posicion))
    SEMAFORO.siguiente_color()

    print(PEPE.manejar(SEMAFORO))
    posicion = CONVERSOR.metros_a_kilometros(PEPE.mirar_posicion())
    print(TRAYECTO.mostrar_posicion(posicion))
    SEMAFORO.siguiente_color()

    PEPE.tener_acompanante(ANA)
    ANA.saludar()
    PEPE.saludar()

    print(PEPE.manejar(SEMAFORO))
    posicion = CONVERSOR.metros_a_kilometros(PEPE.mirar_posicion())
    print(TRAYECTO.mostrar_posicion(posicion))
    SEMAFORO.siguiente_color()

    print(PEPE.manejar(SEMAFORO))
    posicion = CONVERSOR.metros_a_kilometros(PEPE.mirar_posicion())
    print(TRAYECTO.mostrar_posicion(posicion))
    SEMAFORO.siguiente_color()

    print(PEPE.manejar(SEMAFORO))
    posicion = CONVERSOR.metros_a_kilometros(PEPE.mirar_posicion())
    print(TRAYECTO.mostrar_posicion(posicion))
    SEMAFORO.siguiente_color()

    print(PEPE.manejar(SEMAFORO))
    posicion = CONVERSOR.metros_a_kilometros(PEPE.mirar_posicion())
    print(TRAYECTO.mostrar_posicion(posicion))
    SEMAFORO.siguiente_color()

    print(PEPE.manejar(SEMAFORO))
    posicion = CONVERSOR.metros_a_kilometros(PEPE.mirar_posicion())
    print(TRAYECTO.mostrar_posicion(posicion))
    SEMAFORO.siguiente_color()

    print(PEPE.manejar(SEMAFORO))
    posicion = CONVERSOR.metros_a_kilometros(PEPE.mirar_posicion())
    print(TRAYECTO.mostrar_posicion(posicion))
    SEMAFORO.siguiente_color()

    print(PEPE.manejar(SEMAFORO))
    posicion = CONVERSOR.metros_a_kilometros(PEPE.mirar_posicion())
    print(TRAYECTO.mostrar_posicion(posicion))
    SEMAFORO.siguiente_color()

    print(PEPE.manejar(SEMAFORO))
    posicion = CONVERSOR.metros_a_kilometros(PEPE.mirar_posicion())
    print(TRAYECTO.mostrar_posicion(posicion))
    SEMAFORO.siguiente_color()

    HOGAR.dar_en_adopcion(ANA)
    print(GATO.hacer_sonido())

    print(PEPE.manejar(SEMAFORO))
    posicion = CONVERSOR.metros_a_kilometros(PEPE.mirar_posicion())
    print(TRAYECTO.mostrar_posicion(posicion))
    SEMAFORO.siguiente_color()

    print(PEPE.manejar(SEMAFORO))
    posicion = CONVERSOR.metros_a_kilometros(PEPE.mirar_posicion())
    print(TRAYECTO.mostrar_posicion(posicion))
    SEMAFORO.siguiente_color()

    print(PEPE.manejar(SEMAFORO))
    posicion = CONVERSOR.metros_a_kilometros(PEPE.mirar_posicion())
    print(TRAYECTO.mostrar_posicion(posicion))
    SEMAFORO.siguiente_color()

    print(PEPE.manejar(SEMAFORO))
    posicion = CONVERSOR.metros_a_kilometros(PEPE.mirar_posicion())
    print(TRAYECTO.mostrar_posicion(posicion))
    SEMAFORO.siguiente_color()

    print(PEPE.manejar(SEMAFORO))
    posicion = CONVERSOR.metros_a_kilometros(PEPE.mirar_posicion())
    print(TRAYECTO.mostrar_posicion(posicion))
    SEMAFORO.siguiente_color()

    print(PEPE.manejar(SEMAFORO))
    posicion = CONVERSOR.metros_a_kilometros(PEPE.mirar_posicion())
    print(TRAYECTO.mostrar_posicion(posicion))
    SEMAFORO.siguiente_color()

    print(GATO)

    print(PEPE.auto.combustible)

if __name__ == "__main__":
    main()