from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from tqdm import tqdm
import time


class conexionMongo:
    def __init__(self,nombrecoleccion):
        self.MONGO_DATABASE = 'tienda'
        self.MONGO_COLECCION = nombrecoleccion
        self.validarConexion = True
        try:
            uri = 'mongodb+srv://admin:admin@class1.oh3xtlw.mongodb.net/?retryWrites=true&w=majority'
            connect = MongoClient(uri)
            basasedatos = connect[self.MONGO_DATABASE] 
            self.coleccion = basasedatos[self.MONGO_COLECCION]
            self.validarConexion = True
            with tqdm(total=100, desc="Conectando con MongoDb", unit="%") as pbar:
                for i in range(10):
                    time.sleep(0.1)
                    pbar.update(10)
        except:
            print("No se logro conectar con MongoDB")
            self.validarConexion = False
            
    def insertarDocumento(self,documento):
        self.coleccion.insert_one(documento)
        print("Documento insertado")

    def eliminarDocumento(self,key,value):
        documento = self.coleccion.find_one({key : value})
        self.coleccion.delete_one(documento)
        print("Documento Eliminado")

    def validarInsertarProductos(self,documento):
        if self.coleccion.find_one({"codigo": documento["codigo"]}) == None:
            self.insertarDocumento(documento)
        else:
            print("El codigo ya existe")
    def validarInsertarClientes(self,documento):
        if self.coleccion.find_one({"rfc": documento["rfc"]}) == None:
            self.insertarDocumento(documento)
        else:
            print("El codigo ya existe")
    def validarInsertarVentas(self,documento):
        if self.coleccion.find_one({"folio": documento["folio"]}) == None:
            self.insertarDocumento(documento)
        else:
            print("El codigo ya existe")

             # for item in self.coleccion.find():
            #    print(item["codigo"]+item["nombre"]+ item["des"] +str(item["precio"]))
            #print("Conexion con MongoDB exitosa")

    
        

    

if __name__ == "__main__":
    conexion = conexionMongo("productos")
    #conexion.insertarDocumento()
   # conexion.validarInsertar({"codigo": "2", "nombre": "Takis", "des": "Takis morados picantes", "precio": 18})