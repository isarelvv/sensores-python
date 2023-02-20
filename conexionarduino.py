import serial
import time
from constans import Constans
from sensores import sensor
import msvcrt
from mongodb import conexionMongo

class conexionArduino:
#INICILIAR LA CONEXION CON EL ARDUINO
    def __init__(self):
        self.arduino = serial.Serial("COM13",9600)
        self.mongo = conexionMongo("sensores")
        time.sleep(2)

#METODO PARA LEER LOS DATOS DEL ARDUINO
    def leerArduino(self):
        valores=self.arduino.readline()
        return valores.decode("utf-8").strip()

#METODO PARA ESCRIBIR EN EL ARDUINO
    def escribirArduino(self, mensaje):
        self.arduino.write(mensaje)

#METODO PARA CERRAR LA CONEXION CON EL ARDUINO
    def cerrarConexion(self):
        self.arduino.close()

    def llamarArduino(self):
        data = self.arduino.read_all()     
        while True:
            data = self.arduino.read_until()
            print(data.decode("utf-8").strip())
            return data.decode("utf-8").strip()
        
    def readBienvenida(self):
        data = self.arduino.read_until(b'Esperando...')
        print(data.decode("utf-8").strip())
        
    def readSensor(self,id,tipo,identificador):
        self.escribirArduino(id.encode("utf-8"))
        while True:
            data2 = self.arduino.read_until()
            if data2 == b'':
                break
            sensor1 = sensor(tipo, identificador, data2.decode("utf-8").strip())
            print(sensor1)
            self.mongo.insertarAMongo(sensor1)
            if msvcrt.kbhit():
                break
            

    

if __name__ == "__main__":
    conexion = conexionArduino()
    conexion.readBienvenida()
    data = "TH"


            
        


    
    #while True:
        #data = conexion.leerArduino()
        #print(data)
        #conexion.escribirArduino("TH")
        

        

