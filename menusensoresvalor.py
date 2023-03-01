from sensoresvalor import sensorValor
from sensores import sensor
from mongodb import conexionMongo
import time


class menuSensoresValor(sensorValor):
    def __init__(self):
        self.listasensor = sensor().conversionlista()
        self.conexion = conexionMongo("valores")

    def mostraSensores(self):
        for s in self.listasensor:
            print(s)
    
    def nuevoSensorValor(self):
        print("Ingrese el identificador del sensor: ")
        identificador = input()
        sensorx = sensor().buscar(identificador)
        print("Ingrese el valor del sensor: ")
        valor = input()
        timestamp = time.time()
        sensorvalor = sensorValor("1", sensorx, valor, timestamp)
        self.conexion.insertarAMongo(sensorvalor.get_dict())
        print("Sensor agregado con exito")
    
if __name__ == "__main__":
    menu = menuSensoresValor()
    menu.mostraSensores()
    menu.nuevoSensorValor()