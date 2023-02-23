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
        
       

    def loopBorrar(self):
        while not self.stop_event.is_set():
            time.sleep(15)
            os.remove("sensoresTemporales.json")
            
        
    def Inicio(self):
        x = 1
        while x == 1:
            print("Selecciona una opcion")
            print("1.- Sensor 1")
            print("2.- Sensor 2")
            print("3.- Sensor 3")
            print("4.- Sensor 4")
            print("5.- Sensor 5")
            print("6.- Sensor 6")
            print("7.- Todos los sensores")
            print("8.- Cambiar tiempo de respuesta")
            print("9.- Salir")
            opcion = input("Opcion:")
            return opcion


if __name__ == "__main__":
    menu = Menu()
    
    #my_thread = threading.Thread(target=menu.loopBorrar())
    #my_thread.start()
    x = 1
    while x == 1:
        opcion = menu.Inicio()
        if opcion == "1":
            data = menu.con.readSensor("TH","Temperatura","T1")
        elif opcion == "2":
            menu.con.readSensor("US","UltraSonico","U1")
        elif opcion == "3":
            menu.con.readSensor("INFRA","Infrarrojo","I1")
        elif opcion == "4":
            menu.con.readSensor("LUZ","Iluminacion","L1")
        elif opcion == "5":
            menu.con.readSensor("LLUVIA","Lluvia","LL1")
        elif opcion == "6":
            menu.con.readSensor("AGUA","Agua","A1")
        elif opcion == "7":
            print("Todos los sensores")
        elif opcion == "8":
            print("Modificar tiempo de respuesta")
        elif opcion == "9":
            print("Salir")
            menu.con.cerrarConexion()
            menu.temporal.detener()
            x = 0
