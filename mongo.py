from pymongo import MongoClient
from bson.objectid import ObjectId

#Mongo conexion
client = MongoClient("mongodb+srv://KhudoleyS2:Uhkolcv1-@q2-1uvle.mongodb.net/test?retryWrites=true&w=majority")

#Usar db mongo.
db = client['registro_horas']

#Colecciones de la db.
registros_collection = db['registros']
registros_tipo_collection = db['registros_tipo']
users_collection = db['usuarios']

