from lista import Lista
import mongodb

# Description: Clase sensor
class sensor(Lista):
    #INICIALIZAR LOS VALORES DE LA CLASE
    def __init__(self, tipo="N/A", identificador="N/A", valor="N/A"):
        self.tipo = tipo
        self.identificador = identificador
        self.valor = valor
        super().__init__()


    #IDENTIFICAR SI ES SOLO UN OBJETO O ES TODA UNA LISTA
    def __str__(self):
        if self.tamanho >=1 :
            return f"Lista de sensores: {self.lista}"
        else:
            return f"Sensor de tipo: {self.tipo}, identificador: {self.identificador}, valor: {self.valor}"

#FUNCION PARA CONVERTIR UNAS LISTA A DICCIONARIO
    def get_dict(self):
        if self.tamanho >=1 :
            arreglo = []
            for item in self.lista:
                arreglo.append(item.get_dict())
            return arreglo
        else:
            key_list = ["tipo", "identificador", "valor"]
            value_list = [self.tipo, self.identificador, self.valor]
            diccionario = dict(zip(key_list, value_list))
            return diccionario

#FUNCION PARA CONVERTIR UN UN JSON A UN LISTA
    def conversionlista(self,arch,list):
        li = self.leerjson(arch)
        for val in li:
            sensorx = sensor(val['tipo'], val['identificador'], val['valor'])
            list.insere(sensorx)

    def construirUltrasonico(self,lista_ultra):
        ultrasonico = lista_ultra
        for s in ultrasonico:
            print(s)
        
#FUNCION PARA SACAR LA LLAVE DE BUSQUEDA EN LA BASE DE DATOS 
    def getKeys(self):
        return self.identificador

#FUNCION PARA MANDAR EL SENSOR A MONGO
    def sendMongo(self,sensor):
        mongoHelper = mongodb.conexionMongo("sensores")
        mongoHelper.insertarAMongo(sensor)


if __name__ == "__main__":
    sensor1 = sensor("temperatura", "T5", "30")
    sensor2 = sensor("temperatura", "T5", "30") 
    #print(sensor1)
    lista = [sensor1,sensor2]
    sensor1.construirUltrasonico(lista)

        
