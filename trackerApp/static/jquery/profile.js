function edit() {

    document.getElementById("exampleInputEmail1").readOnly = false;
    document.getElementById("exampleInputPassword1").readOnly = false;
    document.getElementById("exampleInputPassword2").readOnly = false;
    document.getElementById("button-gender").disabled = false;
    document.getElementById("button-save").hidden = false;
}

function save(){
    document.getElementById("exampleInputEmail1").readOnly = true;
    document.getElementById("exampleInputPassword1").readOnly = true;
    document.getElementById("exampleInputPassword2").readOnly = true;
    document.getElementById("button-gender").disabled = true;
    document.getElementById("button-save").hidden = true;

    
}