import serial
import time
from constans import Constans
from sensores import sensor
import msvcrt
from mongodb import conexionMongo
import pickle
from sensoresvalor import sensorValor


class conexionArduino(sensorValor):
#INICILIAR LA CONEXION CON EL ARDUINO
    def __init__(self):
        self.arduino = serial.Serial("COM3",9600)
        self.listasensor = sensor().conversionlista()
        self.listatemp = []
        self.listaultra = []
        self.listalluvia = []
        self.listainfrarojo = []
        self.listaagua = []
        self.listailuminacion = []
        self.cargarUbicaciones()
        self.mongo = conexionMongo("valores")
        
        
    def guardarUbicaciones(self):
        todas_las_ubicaciones = [self.listatemp,self.listaultra,self.listalluvia,self.listainfrarojo,self.listaagua,self.listailuminacion]
        with open("ubicaciones.txt","wb") as archivo:
            pickle.dump(todas_las_ubicaciones,archivo)

    def cargarUbicaciones(self):
        with open("ubicaciones.txt","rb") as archivo:
            todas_las_ubicaciones = pickle.load(archivo)
            self.listatemp,self.listaultra,self.listalluvia,self.listainfrarojo,self.listaagua,self.listailuminacion = todas_las_ubicaciones
    def seleccionarSensor(self,tipo):
        lista = []
        for s in self.listasensor:
            if s.tipo == tipo:
                lista.append(s)
        return lista
    
    def llamarTipoSensor(self,tipo,identificador):
        lista = self.seleccionarSensor(tipo)
        self.escribirArduino(identificador.encode("utf-8"))
        while True:
            for s in lista:
                data = self.arduino.read_until()
                sensornuevo = sensorValor(s,data.decode("utf-8").strip(),time.time())
                print(sensornuevo)
                self.mongo.insertarAMongo(sensornuevo.get_dict2())
                print("Sensor agregado con exito")
            if msvcrt.kbhit():
                    break
    def lecturaSensor(self,tipo):
        lista = self.seleccionarSensor(tipo)
        for s in lista:
            ##SE LEE EL VALOR DEL ARDUINO
            valor = self.arduino.read_until()
            sensornuevo = sensorValor(s,valor.decode("utf-8").strip(),time.time())
            print(sensornuevo)
            self.mongo.insertarAMongo(sensornuevo)
            print("Sensor agregado con exito")
        print("Saliendo")
            
    def llamarTodosLosSensores(self,identificador):
        self.escribirArduino(identificador.encode("utf-8"))
        while True:
            data2 = self.arduino.read_until()
            datadecoded = data2.decode("utf-8").strip()
            if "T" in datadecoded:
                self.lecturaSensor("Temperatura")
            elif "D" in datadecoded:
                self.lecturaSensor("Ultrasonico")
            elif "Recipiente" in datadecoded:
                self.lecturaSensor("Infrarojo")
            elif "Foco" in datadecoded:
                self.lecturaSensor("Luz")
            elif "Lluvia" in datadecoded:
                self.lecturaSensor("Lluvia")
            elif "Nivel" in datadecoded:
                self.lecturaSensor("Agua")
            if msvcrt.kbhit():
                    break
            
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
                #self.mongo.insertarAMongo(sensor1)
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
    data2 = conexion.readSensor("TH","Temperatura","T",1)
    print("hola")
    print(data2)


            
        


    
    #while True:
        #data = conexion.leerArduino()
            #print(data)
        #conexion.escribirArduino("TH")
        

        
        #conexion.escribirArduino("1")
