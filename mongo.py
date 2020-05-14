from pymongo import MongoClient
from bson.objectid import ObjectId
from login_data import login_data

#Mongo conexion
client = MongoClient("mongodb+srv://{}:{}@q2-1uvle.mongodb.net/test?retryWrites=true&w=majority".format(login_data['user'],login_data['password']))

#Usar db mongo.
db = client['registro_horas']

#Colecciones de la db.
registros_collection = db['registros']
registros_tipo_collection = db['registros_tipo']
users_collection = db['usuarios']

