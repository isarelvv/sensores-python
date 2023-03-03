from lista import Lista

# Description: Clase sensor
class sensor(Lista):
    #INICIALIZAR LOS VALORES DE LA CLASE
    def __init__(self, tipo="N/A", identificador="N/A", descripcion="N/A"):
        self.tipo = tipo
        self.identificador = identificador
        self.descripcion = descripcion
        super().__init__()


    #IDENTIFICAR SI ES SOLO UN OBJETO O ES TODA UNA LISTA
    def __str__(self):
        if self.tamanho >=1 :
            return f"Lista de sensores: {self.lista}"
        else:
            return f"Sensor de tipo: {self.tipo}, identificador: {self.identificador}, descripcion: {self.descripcion}"

#FUNCION PARA CONVERTIR UNAS LISTA A DICCIONARIO
    def get_dict(self):
        if self.tamanho >=1 :
            arreglo = []
            for item in self.lista:
                arreglo.append(item)
            return arreglo
        else:
            return {'tipo': self.tipo,'tdentificador': self.identificador,'descripcion': self.descripcion}

#FUNCION PARA CONVERTIR UN UN JSON A UN LISTA
    def conversionlista(self):
        self.lista = []
        li = self.leerjson('listadesensores')
        for val in li:
            sensor1= sensor(val['tipo'], val['identificador'],val['descripcion'])
            self.insere(sensor1)
        return self.lista


    def construirUltrasonico(self,lista_ultra):
        ultrasonico = lista_ultra
        for s in ultrasonico:
            print(s)
        
#FUNCION PARA SACAR LA LLAVE DE BUSQUEDA EN LA BASE DE DATOS 
    def getKeys(self):
        return self.identificador
        
#FUNCION PARA MANDAR EL SENSOR A MONGO
    def sendMongo(self,sensor):
        #mongoHelper = mongodb.conexionMongo("sensores")
        #mongoHelper.insertarAMongo(sensor)
        pass

    def cargarSensores(self,lista,nombre="listadesensores"):
        self.guardarjson(nombre,lista.get_dict())

    def convertirListaAObjeto(self,lista):
        listasensores = sensor()
        for val in lista:
            sensor1= sensor(val['tipo'], val['identificador'],val['descripcion'])
            listasensores.insere(sensor1)
        return listasensores


if __name__ == "__main__":
    sensor1 = sensor("temperatura", "T5", "30")
    sensor2 = sensor("temperatura", "T5", "30") 
    #print(sensor1)
    lista = [sensor1,sensor2]
    sensor1.construirUltrasonico(lista)

        
