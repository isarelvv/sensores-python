import json 
from jsonclass import Conversion

class Lista(Conversion):
    #INICIALIZAR LOS VALORES DE LA CLASE
    def __init__(self):
        self.lista = []  
        self.tamanho = 0
        super().__init__()
#INSERTAR LOS ELEMENTOS EN LA LISTA
    def insere(self, elemento):
        self.lista.append(elemento)
        self.tamanho += 1
        
    def remover(self, elemento):
        self.lista.remove(self.buscar(elemento))
        self.tamanho -= 1
        
    def mostrar(self):
        for item in self.lista:
            print(item)

#BUSCAR UN ELEMENTO EN LA LISTA          
    def buscar(self, elemento):
        for item in self.lista:
            print
            if item.getKeys() == elemento:
                return item
               
        #return key
    def editar(self, elemento, posicion):
        self.lista[posicion] = elemento
    

        

        

       
    