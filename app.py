import os
from bson import ObjectId
from clase_A import cuenta_banco
from clase_B import tarjeta_credito
from dataclasses import dataclass, asdict
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

load_dotenv()

URI = os.getenv("URI") # URI:identificaor uniforme de recursos
       
def get_collection(uri, db="demo_db", col="Cuenta Bancaria"): #Para establecer la conexion como mongodb y recolectar la coleccion
    client = MongoClient (
        uri
        , Server_api = ServerApi("1")
        , tls = True #protocolo de seguridad
        , tlsAllowInvalidCertificates = True #conectar sin validar certificados (no necesario)
    )


    
    client.admin.command("ping") #se utiliza para verificar si la conexión sigue activa
    
    return client[db][col] #retorna la coleccion específica 

def actualizar_documento(documento_id, id_relacion, coll):
    
    filtro = {"_id": ObjectId(documento_id)} 
    nuevos_valores = {"$set": {"tarjeta_id": ObjectId(id_relacion)}} 
    resultado = coll.update_one(filtro, nuevos_valores) 
    if resultado.matched_count > 0:
        print("Documento encontrado y actualizado correctamente.")
    else:
        print("No se encontró ningún documento con ese ID.")
    return resultado

def main() : #definir que esto se ejecute primero
    
    
    uri = "mongodb+srv://calvarado04:ferrera504@cluster0.etwaeya.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    coll = get_collection(uri) #recolecta la coleccion
    tarjeta_credito1 = tarjeta_credito("Andres Ferrera", 2029, 78652132015, 589)  
    cuenta_banco1 = cuenta_banco("Andres Ferrera", "Lafise", 769821325, 1000000)
    
    id_cuenta = cuenta_banco1.save(coll)
    tarjeta_credito1.cuenta_id = id_cuenta
    id_tarjeta1 = tarjeta_credito1.save(coll)
    
    actualizar_documento(id_cuenta, id_tarjeta1, coll)
    
    
        
    
if __name__ == "__main__" : #ejecutar el main primero
    main()
