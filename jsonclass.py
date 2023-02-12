import json

class Conversion:
    def guardarjson(self,nombre,listas):
        nombrec=nombre+".json"
        jsondum = json.dumps(listas,indent=4)
        f=open(nombrec,"w")
        f.write(jsondum)
        f.close()
    
    def leerjson(self,nombre):
        nombrec=nombre+".json"
        f=open(nombrec,"r")
        jsondum = json.load(f)
        f.close()
        return jsondum 