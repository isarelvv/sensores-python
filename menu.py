from sensores import sensor
from conexionarduino import conexionArduino
class Menu:
    def __init__(self):
        #INICIALIZAR LA CONEXION CON EL ARDUINO
        self.con = conexionArduino()

#METODO PARA PEDIR EL IDENTIFICADOR DEL SENSOR
    def pedirIdentificador(self):
        identificador = input("Identificador: ")
        return identificador
    
#METODO QUE REALIZAR EL LLAMADO DE LOS DEMAS METODOS
    def Sensor(self,tipo):
        print("Sensor")
        id = self.pedirIdentificador()
        self.escribirArduino(id)
        self.leerDatos(tipo,id)
                
#METODO PARA ESTRAER EL DATO DEL VALOR Y ENVIARLO A MONGO 
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
               # self.leerDatos("Temperatura","TH1")
                tipo = "Temperatura"
                self.Sensor(tipo)
            elif opcion == 2:
                #self.leerDatos("Humedad","HU1")
                tipo = "Humedad"
                self.Sensor(tipo)
            elif opcion == 3:
                #self.leerDatos("UltraSonico","US1")
                tipo = "UltraSonico"
                self.Sensor(tipo)

            elif opcion == 4:
                #self.leerDatos("Luz","LZ1")
                tipo = "Luz"
                self.Sensor(tipo)
            elif opcion == 5:
                #self.leerDatos("Movimiento","MV1")
                tipo = "Movimiento"
                self.Sensor(tipo)
            elif opcion == 6:
                #self.leerDatos("Sonido","SD1")
                tipo = "Sonido"
                self.Sensor(tipo)
            elif opcion == 7:
                print("Todos los sensores")
            elif opcion == 9:
                print("Modificar tiempo de respuesta")
            elif opcion == 0:
                print("Salir")
                break


        