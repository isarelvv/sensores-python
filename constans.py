
class Constans:

    __slots__ = ()
    #ARDUINO CONSTATNS
    PUERTO = 'COM7'
    NUMERO = 9600

    #MONGO CONSTANTS

    URI = 'mongodb+srv://admin:admin@class1.oh3xtlw.mongodb.net/?retryWrites=true&w=majority'
    MONGO_DATABASE = 'python'
    MONGO_COLECCION = 'sensores'

    #JSON CONSTANTS

    JSON_FILE = 'sensores'

    #TIEMPO DE RESPUESTA

    TIEMPO_CONEXION = (30)
    TIEMPO_SIN_CONEXION = (60)
    TIEMPO_LECTURA_ARDUINO = (3)
 