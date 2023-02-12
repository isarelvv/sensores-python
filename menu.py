class Menu:

    def __init__(self):
        pass

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
                print("Sensor 1")
            elif opcion == 2:
                print("Sensor 2")
            elif opcion == 3:
                print("Sensor 3")
            elif opcion == 4:
                print("Sensor 4")
            elif opcion == 5:
                print("Sensor 5")
            elif opcion == 6:
                print("Sensor 6")
            elif opcion == 7:
                print("Cambiar tiempo de respuesta")
            elif opcion == 8:
                print("Saliendo...")
                break


        