from pymongo import MongoClient
from bson.objectid import ObjectId
from login_data import login_data

#Mongo conexion
client = MongoClient('mongodb://localhost')

#Usar db mongo.
db = client['registro_horas']

#Colecciones de la db.
registros_collection = db['registros']
registros_tipo_collection = db['registros_tipo']
users_collection = db['usuarios']

