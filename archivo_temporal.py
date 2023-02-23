import time
import os
import threading    
from mongodb import conexionMongo
import sensores

class archivoTemporal:
    def __init__(self):
        self.stop_event = threading.Event()

    def crarArchivo(self):
            f = open("sensoresTemporales.json", "x")
            f.close()
    
    def detener(self):
        self.stop_event.set()

    def eliminar(self):
        while not self.stop_event.is_set(): 
            print("putos")
            time.sleep(15)
            conexionMongo().listatemporal = sensores.sensor()
            os.remove("sensoresTemporales.json")
            self.crarArchivo()
            time.sleep(2)
            self.eliminar()
            
    def metodoPrueba(self):
        while True:
            time.sleep(1)
            print("Esperando 10 segundos")

if __name__ == "_main_":
    archivo = archivoTemporal()
    archivo.crarArchivo()
    hilo1 = threading.Thread(target = archivo.metodoPrueba)
    hilo2 = threading.Thread(target = archivo.eliminar)
    while True:
        hilo1.start()
        hilo2.start()
        hilo1.join()
        hilo2.join()