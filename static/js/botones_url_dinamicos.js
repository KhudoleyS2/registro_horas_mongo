//Inicio
var boton_comenzar = document.getElementById('boton_comenzar');
//Guardar la url que se va a modificar.
var url_link_usuario = boton_comenzar.href;



//Funcino para poner el url con el id del primer elemento del select para que salga por default.
function boton_default_set_url(){
    var select = document.getElementById("select_tipo_registro");
    var id_tipo_registro = select[0].value;

    boton_comenzar.href = url_link_usuario+id_tipo_registro


}    

//iniciar la funcion para rellenar la ulr nada mas cargar la pagina.
boton_default_set_url();