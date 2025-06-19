import unittest
import os
from bson import ObjectId
from pymongo.mongo_client import MongoClient
from clase_A import cuenta_banco
from clase_B import tarjeta_credito
from app import get_collection, actualizar_documento

class TestSistemaBancario(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.uri = "mongodb+srv://calvarado04:ferrera504@cluster0.etwaeya.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
        cls.client = MongoClient(cls.uri)
        cls.db = cls.client["demo_db"]
        cls.coll = cls.db["Cuenta Bancaria"]
        
        # Limpiar datos de pruebas anteriores
        cls.coll.delete_many({"nombre_propietario": {"$regex": "^TEST-"}})
        

    def test_clases(self):
        
        
        #Crear instancias con datos de prueba
        cuenta = cuenta_banco("TEST-Clase_A", "Banco de A", 111222333, 50000)
        tarjeta = tarjeta_credito("TEST Clase_B", 2030, 999888777, 123)
        
        # Guardar cuenta y obtener ID
        cuenta_id = cuenta.save(self.coll)
        
        
        # Asignar cuenta_id a tarjeta y guardar
        tarjeta.cuenta_id = cuenta_id
        tarjeta_id = tarjeta.save(self.coll)
        
        
        # Actualizar relación en la cuenta
        resultado = actualizar_documento(cuenta_id, tarjeta_id, self.coll)
        self.assertEqual(resultado.matched_count, 1, "Debería haber actualizado 1 documento")
        
        # Verificar datos en MongoDB
        cuenta_db = self.coll.find_one({"_id": ObjectId(cuenta_id)})
        tarjeta_db = self.coll.find_one({"_id": ObjectId(tarjeta_id)})
        
        
        # Verificaciones importantes
        self.assertTrue(ObjectId.is_valid(cuenta_id))
        self.assertTrue(ObjectId.is_valid(tarjeta_id))
        self.assertEqual(str(cuenta_db["tarjeta_id"]), tarjeta_id)
        self.assertEqual(str(tarjeta_db["cuenta_id"]), cuenta_id)
    

    @classmethod
    def tearDownClass(cls):
        cls.client.close()

if __name__ == '__main__':
    unittest.main() 
