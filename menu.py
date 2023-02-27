from sensores import sensor
from conexionarduino import conexionArduino
from archivo_temporal import archivoTemporal
import threading
import time
import os

class Menu:
    def __init__(self):
        self.stop_event = threading.Event()
        #INICIALIZAR LA CONEXION CON EL ARDUINO
        self.con = conexionArduino()
        self.archivo = archivoTemporal()
        hilo1 = threading.Thread (target = self.con.mongo.eliminar)
        hilo1.start()
        if (os.path.exists("ubicaciones.txt")==False):
            self.con.guardarUbicaciones()
        self.con.cargarUbicaciones()
        
    def Inicio(self):
        x = 1
        while x == 1:
            print("Selecciona una opcion")
            print("1.- Sensor Temperatura")
            print("2.- Sensor Ultrasonico")
            print("3.- Sensor Infrarojo")
            print("4.- Sensor Iluminacion ")
            print("5.- Sensor Lluvia")
            print("6.- Sensor Agua")
            print("7.- Todos los sensores")
            print("8.- Cambiar tiempo de respuesta")
            print("9.- Cambiar ubicacion de sensores")
            print("10.- Salir")
            opcion = input("Opcion:")
            return opcion
        
    def menuUbicacion(self):
        x = 1
        while x ==1:
            print("Modificar ubicacion de sensores")
            print("Selecciona una opcion")
            print("1.- Sensor Temperatura")
            print("2.- Sensor Ultrasonico")
            print("3.- Sensor Infrarojo")
            print("4.- Sensor Iluminacion ")
            print("5.- Sensor Lluvia")
            print("6.- Sensor Agua")
            print("7.- Salir")
            opcion = int(input("Opcion:"))
            x = self.cambiarUbicacionSensor(opcion,x)

    def modificarUbicacionSensor(self,lista):
        contador = 1
        print("Ubicacion temeperatura")
        for item in lista:
            contadorstr = str(contador)
            print(contadorstr+"-." " "+"U"+contadorstr + " " +item)
            contador += 1
        print("Selecciona el sensor a modificar")
        opcion = int(input("Opcion:"))
        print("Ingresa la nueva ubicacion")
        ubicacion = input("Ubicacion:")
        lista[opcion-1] = ubicacion
           
    def cambiarUbicacionSensor(self,opcion,x):
        if(opcion==1):
            self.modificarUbicacionSensor(self.con.listatemp)
        elif(opcion==2):
            self.modificarUbicacionSensor(self.con.listaultra)
        elif(opcion==3):
            self.modificarUbicacionSensor(self.con.listainfrarojo)
        elif(opcion==4):
            self.modificarUbicacionSensor(self.con.listailuminacion)
        elif(opcion==5):
            self.modificarUbicacionSensor(self.con.listalluvia)
        elif(opcion==6):
            self.modificarUbicacionSensor(self.con.listaagua)
        elif(opcion==7):
            print("Salir")
            x = 0
            return x
    
    def menuTiemp(self):
        print("Modificar tiempo de respuesta o actualizacion de archivo temporal")
        x=1 
        while x == 1:
            print("1.- Tiempo de respuesta")
            print("2.- Tiempo de actualizacion")
            print("3.- Salir")
            opcion = input("Opcion:")
            if opcion == "1":
                print("Cuanto tiempo desea que sea se envien los datos?")
                tiempo = input("Tiempo:")
                print(tiempo)
                self.con.readTiempo("tiempo",tiempo)
            elif opcion == "2":
                print("Cuanto tiempo desea que sea se actulice el archivo temporal?")
                tiempo = input("Tiempo:")
                self.con.mongo.cambiarTiempo(tiempo)
            elif opcion == "3":
                x = 0
            else:
                print("Opcion no valida")


if __name__ == "__main__":
    menu = Menu()
    x = 1
    while x == 1:
        opcion = menu.Inicio()
        if opcion == "1":
            data = menu.con.readSensor("TH","Temperatura","T",1)
        elif opcion == "2":
            menu.con.readSensor("US","UltraSonico","U",2)
        elif opcion == "3":
            menu.con.readSensor("INFRA","Infrarrojo","I",)
        elif opcion == "4":
            menu.con.readSensor("LUZ","Iluminacion","L",1)
        elif opcion == "5":
            menu.con.readSensor("LLUVIA","Lluvia","LL",1)
        elif opcion == "6":
            menu.con.readSensor("AGUA","Agua","A",1)
        elif opcion == "7":
            menu.con.readAllSensores()
        elif opcion == "8":
            menu.menuTiemp()
        elif opcion == "9":
            menu.menuUbicacion()
        elif opcion == "10":
            print("Salir")
            menu.con.cerrarConexion()
            menu.con.mongo.detener()
            menu.con.guardarUbicaciones()
            x = 0
