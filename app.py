from flask import Flask, render_template, redirect, url_for

import datetime

import func_query , func_registro

app = Flask(__name__)

#JINJA2 Filtros _____________________________________________
@app.template_filter('remover_milisegundos')
def timedelta_remove_milliseconds(timedelta):
	str_timedelta = str(timedelta).split(".")[0]
	return str_timedelta



@app.route('/')
@app.route('/<_id_usuario>')
def index(_id_usuario=None):

	#Datos para crear los selects.
	datos_usuario = func_query.query_usuarios()
	datos_tipo_registro = func_query.query_tipos_registro()

	

	#Si se ha seleccionado un usuario.
	if _id_usuario is not None:
		usuario = func_query.query_usuario_por_id(_id_usuario)
		datos_registros_usuario = func_query.query_registros_por_id_usuario(_id_usuario)

		return render_template(
			'index.html',
			_id_usuario=_id_usuario,
			datos_usuario=datos_usuario,
			datos_tipo_registro=datos_tipo_registro,
			usuario=usuario,
			datos_registros_usuario=datos_registros_usuario,
			)
	else:

		return render_template(
			'index.html',
			_id_usuario=_id_usuario,
			datos_usuario=datos_usuario,
			datos_tipo_registro=datos_tipo_registro,
			)



@app.route('/crear_registro/<id_usuario>/<_id_tipo_registro>')
def crear_registro(id_usuario,_id_tipo_registro):
	func_registro.comenzar_registro(id_usuario,_id_tipo_registro)
	return redirect (url_for('index',id_usuario=id_usuario))





if __name__=="__main__":
    app.run(debug=True)