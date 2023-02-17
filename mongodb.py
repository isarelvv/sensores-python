from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from tqdm import tqdm
import time
import constans
from jsonclass import Conversion
import sensores
import os

class conexionMongo(Conversion):
    #INICIALIZAR LA CONEXION CON MONGODB
    def __init__(self,nombrecoleccion):
        self.lista = sensores.sensor()
        self.MONGO_DATABASE = constans.Constans.MONGO_DATABASE
        self.MONGO_COLECCION = constans.Constans.MONGO_COLECCION
        self.validarConexion = True
        try:
            #PROBAR LA CONEZION CON MONGODB
            uri = constans.URI
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

#METODO PARA INTENTAR GUARDAR EL SENSOR EN MONGODB
    def insertarAMongo(self,dict):
        if self.validarConexion==True:
            #VERIFICAR SI EL ARCHIVO SIN CONEXION TIENE CONTENIDO
            docDesconectado = self.leerjson('sensoresOffline')
            if len(docDesconectado) > 0:
                #SI TIENE CONTENIDO, INTENTAR GUARDARLO EN MONGOD
                self.coleccion.insert_many(docDesconectado)
                #LIMPIAR EL ARCHIVO SIN CONEXION
                os.remove('sensoresOffline.json')
            self.insertarDocumento(dict.get_dict())           
        else:
            print("No se logro conectar con MongoDB, guardando localmente")
            self.guardarEnLocal(dict)


#METODO PARA GUARDAR SIN CONEXION
    def guardarEnLocal(self,data):
        try:
            lista = self.lista.conversionlista()
            print(lista)
            lista.insere(data)
            os.remove('sensoresOffline.json')
            self.agregarContenido('sensoresOffline',lista.get_dict())
        except:
            self.lista.insere(data)
            self.agregarContenido('sensoresOffline',self.lista.get_dict())
        



#PROBANDO LA CLASE
if __name__ == "__main__":
    conexion = conexionMongo("productos")
    #conexion.insertarDocumento()
   # conexion.validarInsertar({"codigo": "2", "nombre": "Takis", "des": "Takis morados picantes", "precio": 18})