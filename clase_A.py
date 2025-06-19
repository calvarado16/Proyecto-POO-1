from dataclasses import asdict, dataclass
import os
from dataclasses import dataclass, asdict
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv



@dataclass
class cuenta_banco:
    
    nombre_propietario : str 
    banco: str
    numero_cuenta : int
    saldo: int
    tarjeta_id : str = ''
    
    def atributosA(self):
        print("Propietario: ", self.nombre_propietario)
        print("Banco: ", self.banco)
        print("Numero de Cuenta: ", self.numero_cuenta)
        print("Saldo disponible: ", f"L.{self.saldo}")
        print("Id tarjeta: ", self.tarjeta_id)
        
    def save(self, coll):
        return str( coll.insert_one( asdict(self) ).inserted_id  )


  


        
