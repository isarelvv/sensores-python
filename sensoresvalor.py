from lista import Lista
import mongodb
from sensores import sensor

class sensorValor(Lista):
    def __init__(self,sensor="N/A",valor="N/A",timestamp="N/A"):
        self.sensor = sensor
        self.valor = valor
        self.timestamp = timestamp
        super().__init__()

    def __str__(self):
        if self.tamanho >=1 :
            return f"Lista de sensores: {self.lista}"
        else:
            return f"Sensor de tipo: {self.sensor}, valor: {self.valor}, timestamp: {self.timestamp}"
    def getKeys(self):
        return self.id
    
    def get_dict2(self):
        if self.tamanho >=1 :
            arreglo = []
            for item in self.lista:
                arreglo.append(item)
            return arreglo
        else:
            key_list = ["sensor", "valor", "timestamp"]
            value_list = [self.sensor.get_dict(), self.valor, self.timestamp]
            diccionario = dict(zip(key_list, value_list))
            return diccionario
        
    def conversionlista(self):
        self = []
        li = self.leerjson('sensoresTemporales')
        for val in li:
            sensorvalor= sensorValor(val['sensor'], val['valor'],val['timestamp'])
            self.insere(sensorvalor)
        return self

    
    def sendMongo(self,sensor):
        mongoHelper = mongodb.conexionMongo("sensores")
        mongoHelper.insertarAMongo(sensor)
    


        