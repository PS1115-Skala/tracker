function edit() {
    document.getElementById("exampleInputEmail1").readOnly = false;
    document.getElementById("exampleInputPassword1").readOnly = false;    
    document.getElementById("button-gender").disabled = false;
    document.getElementById("button-save").hidden = false;
    document.getElementById("exampleInputDescription").readOnly = false;
    document.getElementById("id_image").disabled = false;
}

function save(){
    document.getElementById("exampleInputEmail1").readOnly = true;
    document.getElementById("exampleInputPassword1").readOnly = true;    
    document.getElementById("exampleInputDescription").readOnly = true;
    document.getElementById("button-gender").disabled = true;
    document.getElementById("button-save").hidden = true;
    document.getElementById("id_image").disabled = true;

}