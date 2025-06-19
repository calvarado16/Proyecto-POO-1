from dataclasses import asdict, dataclass
import os

from dataclasses import dataclass, asdict
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from dotenv import load_dotenv

@dataclass

class tarjeta_credito:
    
    nombre_propietario : str
    año_vencimiento : int
    numero_tarjeta : int 
    CVV : int
    cuenta_id: str = ""

    def atributosB(self):
        print("Propietario: ", self.nombre_propietario)
        print("Año de vencimiento: ", self.año_vencimiento)
        print("Numero de tarjeta: ", self.numero_tarjeta)
        print("Card Verification Value: ", self.CVV)
        print("ID cuenta: ", self.cuenta_id) 
           
    def save(self, coll):
        return str( coll.insert_one( asdict(self) ).inserted_id  )

      
