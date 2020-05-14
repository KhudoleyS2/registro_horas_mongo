//Elementos
var dropdown = document.getElementById('dropdown');
var dropdown_content = document.getElementById('dropdown-content');


//funcion para poner display:block al dropdown_content
function display_dropdown_content(){
    dropdown_content.style.display = "block";
}
//funcion para poner display:none.
function hide_dropdown_content(){
    dropdown_content.style.display = "none";
}

//Agregar event click al boton dropdown.
//dropdown.addEventListener("click",display_dropdown_content);
window.addEventListener("click",function(e){
    if (dropdown.contains(e.target)){
        display_dropdown_content()
    }
    else{
        hide_dropdown_content()
    }
})