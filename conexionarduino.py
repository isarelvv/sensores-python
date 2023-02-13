import serial
import time
import constants


class conexionArduino:
    def __init__(self):
        arduino = serial.Serial(constants.PUERTO, constants.NUMERO)
        time.sleep(2)
        raw = arduino.readline()
        print(raw)
        arduino.close()

if __name__ == "__main__":
    conexion = conexionArduino()