import serial
import time
from constans import Constans

class conexionArduino:
#INICILIAR LA CONEXION CON EL ARDUINO
    def __init__(self):
        self.arduino = serial.Serial(Constans.PUERTO,Constans.NUMERO)
        time.sleep(2)

#METODO PARA LEER LOS DATOS DEL ARDUINO
    def leerArduino(self):
        valores=self.arduino.readline()
        return valores.decode("utf-8")

#METODO PARA ESCRIBIR EN EL IDENTIFICADOR DEL ARDUINO
    def escribirArduino(self, valor):
        self.arduino.write(valor.encode())
        time.sleep(1)

#METODO PARA CERRAR LA CONEXION CON EL ARDUINO
    def cerrarConexion(self):
        self.arduino.close()
    
    

if __name__ == "__main__":
    conexion = conexionArduino()
    while(True):
        imprimir = conexion.leerArduino()
        print(imprimir)
        conexion.escribirArduino("1")
