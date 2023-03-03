from sensoresvalor import sensorValor
from sensores import sensor
from mongodb import conexionMongo
import time
import msvcrt
from conexionarduino import conexionArduino


class menuSensoresValor(sensorValor):
    def __init__(self):
        self.listasensor = sensor().conversionlista()
        self.conexion = conexionMongo("valores")
        self.arduinos = conexionArduino()


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
                sensornuevo = sensorValor(s,"12",time.time())
                print(sensornuevo)
                self.conexion.insertarAMongo(sensornuevo)
                print("Sensor agregado con exito")
                time.sleep(2)

    def llamarTipoSensor(self,tipo,identificador):
        lista = self.seleccionarSensor(tipo)
        self.arduinos.escribirArduino(identificador.encode("utf-8"))
        while True:
            for s in lista:
                data = self.arduinos.arduino.read_until()
                sensornuevo = sensorValor("1",s,data.decode("utf-8").strip,time.time())
                print(sensornuevo)
                self.conexion.insertarAMongo(sensornuevo)
                print("Sensor agregado con exito")
            if msvcrt.kbhit():
                    break
  
    def lecturaSensor(self,tipo):
        lista = self.seleccionarSensor(tipo)
        for s in lista:
            ##SE LEE EL VALOR DEL ARDUINO
            valor = self.arduinos.read()
            sensornuevo = sensorValor("1",s,valor,time.time())
            print(sensornuevo)
            self.conexion.insertarAMongo(sensornuevo)
            print("Sensor agregado con exito")
        print("Saliendo")
            
    def llamarTodosLosSensores(self):
        while True:
            data2 = self.arduino.read_until()
            datadecoded = data2.decode("utf-8").strip()
            if "T" in datadecoded:
                self.lecturaSensor("Temperatura")
            elif "D" in datadecoded:
                self.lecturaSensor("UltraSonico")
            elif "lluvia" in datadecoded:
                self.lecturaSensor("Lluvia")
            elif "Nivel" in datadecoded:
                self.lecturaSensor("Agua")
            elif "Recipiente" in datadecoded:
                self.lecturaSensor("InfraRojo")
            elif "Foco" in datadecoded:
                self.lecturaSensor("Iluminacion")
            if msvcrt.kbhit():
                    break
            
                
            
            
            
            
    
if __name__ == "__main__":
    menu = menuSensoresValor()
    menu.mostraSensores()
    #menu.nuevoSensorValor()
    menu.arduinos.arduino.write("TH".encode("utf-8"))
    data= menu.arduinos.arduino.read_until()
    decoded = data.decode("utf-8").strip()
    print(decoded)
   
    #menu.llamarTipoSensor("Temperatura","TH")
   # menu.llamarTipoSensor("Temperatura","TH")