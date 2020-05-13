// Datetime string formato python.
var datetime_python = document.getElementById('date_inicio_registro').innerHTML;

// Moment js crear objeto moment.
var date_inicio = moment(datetime_python).format("YYYY-MM-DD HH:mm:ss");

// TD contenedor de la duracion.
var td_duracion = document.getElementById('timedelta_duracion');
var td_duracion_registro= document.getElementById('time_delta_registro');

//Ejecutar la funcion para pintar la duracion nada mas cargar la pagina.
str_timedelta()


// Funcion para ecnontrar el elemento con id = timedelta_duracion y pintar el timedelta actual.
function str_timedelta(){

    // Moment js objeto moment now.
    var date_now = moment();


    //Duracion timedelta
    var duration = moment.duration(date_now.diff(date_inicio))
    
    //Obj Momentjs creado a partir del timedelta y dado el formato
    var duration_formated = moment.utc(duration.asMilliseconds()).format("H:mm:ss")

    // Pintar dentro del <td> la duracion resultante.
    td_duracion.innerHTML = duration_formated + " h"
    td_duracion_registro.innerHTML = duration_formated

}

//Timeinterval para ejecutar la funcion str_timedelta 1000 milisegundos despues de ser ejecutado.
window.setInterval(str_timedelta,1000)