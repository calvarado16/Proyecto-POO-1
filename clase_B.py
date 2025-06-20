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
           
    def save(self, coll):
        return str( coll.insert_one( asdict(self) ).inserted_id  )

      
