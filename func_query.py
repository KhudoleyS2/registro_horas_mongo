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

def query_registros_por_id_usuario(id_usuario):
    lista_registros = registros_collection.find({"_id_usuario":ObjectId(id_usuario)}).sort("comienzo_registro",-1)
    return lista_registros

def query_utlimo_registro_por_id_usuario(id_usuario):
    ultimo_registro = registros_collection.find({"_id_usuario":ObjectId(id_usuario)}).sort("comienzo_registro",-1).limit(1)
    try:
        return ultimo_registro[0]
    except:
        return None



if __name__=="__main__":

    for i in query_registros_por_id_usuario("5ebbcf73b2f328ec8c533e2f"):
        print (i)
    pass
        