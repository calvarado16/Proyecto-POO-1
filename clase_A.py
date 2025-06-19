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
    
    
    def save(self, coll):
        return str( coll.insert_one( asdict(self) ).inserted_id  )


  


        
