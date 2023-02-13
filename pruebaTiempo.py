import os
import time
import keyboard

class PruebaTiempo:
    def __init__(self):
        pass

    def prueba(self):
        """current_time = time.strftime("%H:%M:%S")
        print("Esperando 5 segundos")
        time.sleep(5)
        print("Listo")
        print(time.localtime().tm_year)"""

        lista = []

        while True:
            time.sleep(2) #Esperar 10 segundos

            if keyboard.is_pressed("q"):
                break

            try:
                os.remove("prueba.json")
                print("Archivo eliminado")

            except:
                print("Error al eliminar el archivo")

if __name__ == "__main__":
    prueba = PruebaTiempo()
    prueba.prueba()