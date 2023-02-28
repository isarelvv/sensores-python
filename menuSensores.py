from sensores import sensor

class MenuSensores(sensor):

    def __init__(self):
        self.listasensores = sensor()
        try:
            self.listasensores.conversionlista("listadesensores",self.listasensores)
        except:
            print("No hay sensores registrados")
        
    def nuevoSensor(self):
        print("Ingrese el tipo de sensor: ")
        tipo = input()
        print("Ingrese el identificador del sensor: ")
        identificador = input()
        print("Ingrese la descripcion del sensor: ")
        descripcion = input()
        sensorx = sensor(tipo, identificador, None, descripcion)
        self.listasensores.insere(sensorx)
        print(sensorx)
        self.listasensores.cargarSensores(self.listasensores)
        print("Sensor agregado con exito")

    def verSensores(self):
        self.listasensores.mostrar()

    def cambiarInfoSensor(self):
        identificador = input("Ingrese el identificador del sensor: ")
        sensorx = self.listasensores.buscar(identificador)
        print(sensorx)
        y=1
        while y==1:
            print("1. Cambiar tipo")
            print("2. Cambiar identificador")
            print("3. Cambiar descripcion")
            print("4. Salir")
            opcion = int(input())
            if opcion == 1:
                print("Ingrese el nuevo tipo de sensor: ")
                tipo = input()
                sensorx.tipo = tipo
            elif opcion == 2:
                print("Ingrese el nuevo identificador del sensor: ")
                identificador = input()
                sensorx.identificador = identificador
            elif opcion == 3:
                print("Ingrese la nueva descripcion del sensor: ")
                descripcion = input()
                sensorx.descripcion = descripcion
            elif opcion == 4:
                y=0
            else:
                print("Opcion invalida")
        self.listasensores.cargarSensores(self.listasensores)

    def menuSensores(self):
        x=1
        while x==1:
            print("1. Agregar un sensor")
            print("2. Ver sensores")
            print("3. Cambiar informacion de un sensor")
            print("4. Salir")
            opcion = int(input())
            if opcion == 1:
                self.nuevoSensor()
            elif opcion == 2:
                self.verSensores()
            elif opcion == 3:
                self.cambiarInfoSensor()
            elif opcion == 4:
                x=0
            else:
                print("Opcion invalida")

if __name__ == "__main__":
    menu = MenuSensores()
    menu.menuSensores()
