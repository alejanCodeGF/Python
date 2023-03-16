# Gestionar la conexion a nuesta base de datos con mongodb

from pymongo import mongo_client # pip install pymongo

db_client = mongo_client() # Si no le pones nada, de base pone el localhost (que es este caso)

