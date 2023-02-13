import json 
from jsonclass import Conversion

class Lista(Conversion):
    def __init__(self):
        self.lista = []
        self.tamanho = 0
        super().__init__()

    def insere(self, elemento):
        self.lista.append(elemento)
        self.tamanho += 1

    def remover(self, elemento):
        self.lista.remove(self.buscar(elemento))
        self.tamanho -= 1

    def mostrar(self):
        for item in self.lista:
            print(item)
            
    def buscar(self, elemento):
        for item in self.lista:
            if item.getKey() == elemento:
                return item
            else:
                return "No se encontro el elemento"
        #return key
        
    def editar(self, elemento, posicion):
        self.lista[posicion] = elemento
    

        

        

       
    