from sensores import sensor
from conexionarduino import conexionArduino
class Menu:
    def __init__(self):
        self.con = conexionArduino()
    
    def leerDatos(self,tipo,id):
        data = self.con.leerArduino()
        sensor1 = sensor(tipo,id,data)
        sensor1.sendMongo(sensor1)


    def Inicio(self):
        while True:
            print("Selecciona una opcion")
            print("1.- Sensor 1")
            print("2.- Sensor 2")
            print("3.- Sensor 3")
            print("4.- Sensor 4")
            print("5.- Sensor 5")
            print("6.- Sensor 6")
            print("7.- Cambiar tiempo de respuesta")
            print("8.- Salir")
            opcion = input("Opcion: ")
            if opcion == 1:
                self.leerDatos("Temperatura","TH1")
            elif opcion == 2:
                self.leerDatos("Humedad","HU1")
            elif opcion == 3:
                self.leerDatos("UltraSonico","US1")
            elif opcion == 4:
                self.leerDatos("Luz","LZ1")
            elif opcion == 5:
                self.leerDatos("Movimiento","MV1")
            elif opcion == 6:
                self.leerDatos("Sonido","SD1")
            elif opcion == 7:
                print("Todos los sensores")
            elif opcion == 9:
                print("Modificar tiempo de respuesta")
            elif opcion == 0:
                print("Salir")
                break


        