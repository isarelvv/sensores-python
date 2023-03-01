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
        #self.conexion.insertarAMongo(sensorvalor)
        print("Sensor agregado con exito")

    def seleccionarSensor(self,tipo):
        lista = []
        for s in self.listasensor:
            if s.tipo == tipo:
                lista.append(s)
        return lista
    
    def simularEntrada(self):
        lista = self.seleccionarSensor("Temperatura")
        while True:
            for s in lista:
                sensornuevo = sensorValor("1",s,"12",time.time())
                print(sensornuevo)
                #self.conexion.insertarAMongo(sensorvalor)
                print("Sensor agregado con exito")
                time.sleep(2)
            time.sleep(2)

    def llamarTipoSensor(self,tipo):
        lista = self.seleccionarSensor(tipo)
        while True:
            for s in lista:
               ##SE LEE EL VALOR DEL ARDUINO
                #valor = arduino.read()
                #sensornuevo = sensorValor("1",s,valor,time.time())
                #print(sensornuevo)
                #self.conexion.insertarAMongo(sensorvalor)
                print("Sensor agregado con exito")
                time.sleep(2)

    def llamarTodosLosSensores(self):
        while True:
            pass
            
                
            
            
            
            
    
if __name__ == "__main__":
    menu = menuSensoresValor()
    menu.mostraSensores()
    menu.nuevoSensorValor()
    menu.simularEntrada()