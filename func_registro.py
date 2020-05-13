from mongo import registros_collection, registros_tipo_collection, users_collection
import func_query
from bson.objectid import ObjectId
import datetime


#Funcion insertar registro en DB.___________________________________________________________________________________________________
def insertar_registro(id_usuario,_id_tipo_registro):
    registros_collection.insert_one(
        {
            "_id_usuario":ObjectId(id_usuario),
            "_id_tipo_registro":ObjectId(_id_tipo_registro),
            "comienzo_registro":datetime.datetime.now(),
            "final_registro":None
        }
    )





#Comenzar un nuevo registro________________________________________________________________________________________________________
def comenzar_registro(id_usuario,_id_tipo_registro):

    #Primero comprobar el ultmo registro del usuario.
    ultimo_registro = func_query.query_utlimo_registro_por_id_usuario(id_usuario)
    
    #Comprobar si existe el ultmio registro (puede ser el primero y no existir ninguno todavia).
    if ultimo_registro is not None:
        
        #Si existe un registro comprobar si el final_registro es None. Para saber si esta todavia abierto o cerrado.
        if ultimo_registro['final_registro'] is not None:
            
            insertar_registro(id_usuario,_id_tipo_registro)

        else:
            #Feedback en cosola del error.
            print('El registro ya esta cerrado. Existe un final de joranada ya asignado.')

    #Si no existe nigun registro. Crear el primero.
    else:
        
        insertar_registro(id_usuario,_id_tipo_registro)
