from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from tqdm import tqdm
import time
import constans
from jsonclass import Conversion
import sensores
import os
import threading

class conexionMongo(Conversion):
    #INICIALIZAR LA CONEXION CON MONGODB
    def __init__(self,nombrecoleccion):
        self.listatemporal = sensores.sensor()
        self.listaoffline = sensores.sensor()
        self.URI = constans.Constans.URI
        self.stop_event = threading.Event()
        self.MONGO_DATABASE = constans.Constans.MONGO_DATABASE
        self.MONGO_COLECCION = constans.Constans.MONGO_COLECCION
        self.validarConexion = True
        try:
            #PROBAR LA CONEZION CON MONGODB
            connect = MongoClient(self.URI)
            basasedatos = connect[self.MONGO_DATABASE] 
            self.coleccion = basasedatos[self.MONGO_COLECCION]
            self.validarConexion = True
            with tqdm(total=100, desc="Conectando con MongoDb", unit="%") as pbar:
                for i in range(10):
                    time.sleep(0.1)
                    pbar.update(10)
            #self.segundoplano = threading.Thread(target=self.eliminarJSONTemporal)
            #self.segundoplano.start()
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

#METODO PARA INTENTAR GUARDAR EL SENSOR EN MONGODB
    def insertarAMongo(self,dict):
        if self.validarConexion==True:
            #VERIFICAR SI EL ARCHIVO SIN CONEXION TIENE CONTENIDO
            if os.path.exists('sensoresOffline.json'):
                docDesconectado = self.leerjson('sensoresOffline')
                #SI TIENE CONTENIDO, INTENTAR GUARDARLO EN MONGOD
                self.coleccion.insert_many(docDesconectado)
                #LIMPIAR EL ARCHIVO SIN CONEXION
                os.remove('sensoresOffline.json')
            self.guardarJSONTemporal(dict)
            #self.insertarDocumento(dict.get_dict())           
        else:
            print("No se logro conectar con MongoDB, guardando localmente")
            self.guardarEnLocal(dict)


#METODO PARA GUARDAR SIN CONEXION
    def guardarEnLocal(self,data):
        self.listaoffline.insere(data)
        self.guardarjson('sensoresOffline',self.listaoffline.get_dict())
        
    
    def guardarJSONTemporal(self,dict):
        self.listatemporal.insere(dict)
        self.guardarjson('sensoresTemporales',self.listatemporal.get_dict())

    def eliminarJSONTemporal(self):
        while True:
            self.listatemporal = sensores.sensor()
            os.remove('sensoresTemporales.json')

    def crarArchivo(self):
            f = open("sensoresTemporales.json", "x")
            f.close()
    
    def detener(self):
        self.stop_event.set()

    def eliminar(self):
        while not self.stop_event.is_set(): 
            print("putos")
            time.sleep(15)
            self.listatemporal = sensores.sensor()
            os.remove("sensoresTemporales.json")
            self.crarArchivo()
            time.sleep(2)
            self.eliminar()
    

        
        
        



#PROBANDO LA CLASE
if __name__ == "__main__":
    conexion = conexionMongo("sensores")
    print(len(conexion.leerjson('sensoresOffline')))
   # conexion.validarInsertar({"codigo": "2", "nombre": "Takis", "des": "Takis morados picantes", "precio": 18})