from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from tqdm import tqdm
import time
import constants


class conexionMongo:
    #INICIALIZAR LA CONEXION CON MONGODB
    def __init__(self,nombrecoleccion):
        self.MONGO_DATABASE = 'tienda'
        self.MONGO_COLECCION = nombrecoleccion
        self.validarConexion = True
        try:
            #PROBAR LA CONEZION CON MONGODB
            uri = constants.URI
            connect = MongoClient(uri)
            basasedatos = connect[self.MONGO_DATABASE] 
            self.coleccion = basasedatos[self.MONGO_COLECCION]
            self.validarConexion = True
            with tqdm(total=100, desc="Conectando con MongoDb", unit="%") as pbar:
                for i in range(10):
                    time.sleep(0.1)
                    pbar.update(10)
        except:
            #SI NO SE PUEDE CONECTAR CON MONGODB
            print("No se logro conectar con MongoDB")
            self.validarConexion = False
    
#METODO PARA INSERTAR UN DOCUMENTO EN MONGODB
    def insertarDocumento(self,documento):
        self.coleccion.insert_one(documento)
        print("Documento insertado")

#METODO PARA ELIMINAR EL DOCUMENTO DE UNA COLECICON(NO USAR)
    def eliminarDocumento(self,key,value):
        documento = self.coleccion.find_one({key : value})
        self.coleccion.delete_one(documento)
        print("Documento Eliminado")

#METODO PARA ACTUALIZAR UN DOCUMENTO DE UNA COLECCION
    def actualizarDocumento(self,key,value,documento):
        self.coleccion.update_one({key : value},{"$set":documento})
        print("Documento Actualizado")

#METODO PARA VALIDAR SI EL DOCUMENTO YA EXISTE
    def validarInsertar(self,documento):
        if self.coleccion.find_one({"identificador": documento["identificador"]}) == None:
            self.insertarDocumento(documento)
        else:
            print("El codigo ya existe")


#PROBANDO LA CLASE
if __name__ == "__main__":
    conexion = conexionMongo("productos")
    #conexion.insertarDocumento()
   # conexion.validarInsertar({"codigo": "2", "nombre": "Takis", "des": "Takis morados picantes", "precio": 18})