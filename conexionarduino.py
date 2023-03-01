import serial
import time
from constans import Constans
from sensores import sensor
import msvcrt
from mongodb import conexionMongo
import pickle


class conexionArduino:
#INICILIAR LA CONEXION CON EL ARDUINO
    def __init__(self):
        self.arduino = serial.Serial("COM4",9600)
        self.mongo = conexionMongo("sensores")
        self.sensores= [{"tipo": "Temperatura","Id" : "T1"},{"tipo": "UltraSonico","Id" : "US"},
                        {"tipo": "Iluminacios","Id" : "LUZ1"},{"tipo": "Infrrarojo","Id" : "IR1"},
                        {"tipo": "Lluvia","Id" : "LL1"},{"tipo": "Agua","Id" : "A1"}]
        self.listaultra = ["cocina","baño"]
        self.listatemp= ["sala"]
        self.listalluvia = ["exterior"]
        self.listainfrarojo = ["puerta"]
        self.listaagua = ["recamara"]
        self.listailuminacion = ["recamara"]
        
    def guardarUbicaciones(self):
        todas_las_ubicaciones = [self.listatemp,self.listaultra,self.listalluvia,self.listainfrarojo,self.listaagua,self.listailuminacion]
        with open("ubicaciones.txt","wb") as archivo:
            pickle.dump(todas_las_ubicaciones,archivo)

    def cargarUbicaciones(self):
        with open("ubicaciones.txt","rb") as archivo:
            todas_las_ubicaciones = pickle.load(archivo)
            self.listatemp,self.listaultra,self.listalluvia,self.listainfrarojo,self.listaagua,self.listailuminacion = todas_las_ubicaciones

#METODO PARA LEER LOS DATOS DEL ARDUINO
    def leerArduino(self):
        while(True):
            valores=self.arduino.readline()
            return valores.decode("utf-8")

#METODO PARA ESCRIBIR EN EL ARDUINO
    def escribirArduino(self, mensaje):
        self.arduino.write(mensaje)

#METODO PARA CERRAR LA CONEXION CON EL ARDUINO
    def cerrarConexion(self):
        self.arduino.close()

    def llamarArduino(self):
        while True:
            data = self.arduino.read_all()
            if data ==b'Esperando...':
                print("skip")
                break

        while True:
            data = self.arduino.read_until()
            print(data.decode("utf-8").strip())
            return data.decode("utf-8").strip()
        
    def readBienvenida(self):
        data = self.arduino.read_until(b'Esperando...')
        print(data.decode("utf-8").strip())
        
    def readSensor(self,id,tipo,identificador,contador):
        self.escribirArduino(id.encode("utf-8"))
        lista = self.seleccionarLista(id)
        while True:
            j = 0
            while (j < contador):
                tiposensor = tipo +" "+ lista [j]
                j += 1
                identificadorsensor = identificador + str(j)
                data2 = self.arduino.read_until()
                sensor1 = sensor(tiposensor, identificadorsensor, data2.decode("utf-8").strip())
                print(sensor1)
                self.mongo.insertarAMongo(sensor1)
            if msvcrt.kbhit():
                        break

    def readTiempo(self,respuesa,tiempo):
        tiempoconversion = tiempo
        self.escribirArduino("TIEMPO".encode("utf-8"))
        self.escribirArduino(tiempoconversion.encode("utf-8"))

            
    def readAllSensores(self):
        self.escribirArduino("TODOS".encode("utf-8"))
        while True:
            data2 = self.arduino.read_until()
            datadecoded = data2.decode("utf-8").strip()
            if "T" in datadecoded:
                sensor1 = sensor("Temperatura", "T1", datadecoded)
                print(sensor1)
                self.mongo.insertarAMongo(sensor1)
            elif "D" in datadecoded:
                sensor2 = sensor("UltraSonico", "US", datadecoded)
                print(sensor2)
                self.mongo.insertarAMongo(sensor2)
            elif "lluvia" in datadecoded:
                sensor3 = sensor("Lluvia", "LL1", datadecoded)
                print(sensor3)
                self.mongo.insertarAMongo(sensor3)
            elif "Nivel" in datadecoded:
                sensor4 = sensor("Agua", "A1", datadecoded)
                print(sensor4)
                self.mongo.insertarAMongo(sensor4)
            elif "Recipiente" in datadecoded:
                sensor5 = sensor("Infrrarojo", "IR1", datadecoded)
                print(sensor5)
                self.mongo.insertarAMongo(sensor5)
            elif "Foco" in datadecoded:
                sensor6 = sensor("Iluminacios", "LUZ1", datadecoded)
                print(sensor6)
                self.mongo.insertarAMongo(sensor6)
            if msvcrt.kbhit():
                    break

    def seleccionarLista(self,id):
        if id == "TH":
            return self.listatemp
        elif id == "US":
            return self.listaultra
        elif id == "LLUVIA":
            return self.listalluvia
        elif id == "AGUA":
            return self.listaagua
        elif id == "INFRA":
            return self.listainfrarojo
        elif id == "LUZ":
            return self.listailuminacion


if __name__ == "__main__":
    conexion = conexionArduino()
    conexion.guardarUbicaciones()
    conexion.cargarUbicaciones()


            
        


    
    #while True:
        #data = conexion.leerArduino()
            #print(data)
        #conexion.escribirArduino("TH")
        

        
        #conexion.escribirArduino("1")
