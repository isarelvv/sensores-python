import json

class Conversion:
    #CONVERTIR UNA LISTA A JSON
    def guardarjson(self,nombre,listas):
        nombrec=nombre+".json"
        jsondum = json.dumps(listas,indent=4)
        f=open(nombrec,"w")
        f.write(jsondum)
        f.close()
    #LEER UN JSON Y CONVERTIRLO A LISTA
    def leerjson(self,nombre):
        nombrec=nombre+".json"
        f=open(nombrec,"r")
        jsondum = json.load(f)
        f.close()
        return jsondum 
    
    def agregarContenido(self,nombre,contenido):
        nombrec=nombre+".json"
        data = json.dumps(contenido,indent=4)
        f=open(nombrec,"a")
        f.write(data)
        f.close()

if __name__ == "__main__":
    json1 =  Conversion()
    print(json1.leerjson("sensoresOffline"))