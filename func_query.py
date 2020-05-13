from mongo import registros_collection, registros_tipo_collection, users_collection
from bson.objectid import ObjectId

#USERS______________________________________
def query_usuarios():
    lista_users = users_collection.find().sort("user",1)
    return lista_users

def query_usuario_por_id(id_usuario):
    usuario = users_collection.find_one({"_id":ObjectId(id_usuario)})
    return usuario


#TIPO DE REGISTRO ___________________________
def query_tipos_registro():
    lista_tipos = registros_tipo_collection.find()
    return lista_tipos


  
#REGISTROS___________________________________
def query_registros():
    lista_registros = registros_collection.find().sort("comienzo_registro",-1)
    return lista_registros

#Funcion query datos_por_id_usuario    JOIN     _id_tipo_registro => tipo   para crear un campo nombre_tipo.
def query_registros_por_id_usuario(id_usuario):
    data = registros_collection.aggregate([
        {"$match":{"_id_usuario":ObjectId(id_usuario)}},
        {"$lookup":{"from":"registros_tipo","localField":"_id_tipo_registro","foreignField":"_id","as":"tipo"}},
        {"$sort": {"comienzo_registro":-1} }
    ])
    return data


def query_utlimo_registro_por_id_usuario(id_usuario):
    ultimo_registro = registros_collection.aggregate([
       {"$match":{"_id_usuario":ObjectId(id_usuario)}},
       {"$lookup":{"from":"registros_tipo","localField":"_id_tipo_registro","foreignField":"_id","as":"tipo"}},
       {"$sort": {"comienzo_registro":-1} },
       {"$limit":1}
    ])
    try:
        ultimo_registro = ultimo_registro.next()
    except:
        ultimo_registro = None
    return ultimo_registro

if __name__=="__main__":

    pass
        