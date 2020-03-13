var fechaVieja;
var intervalId;
var tiempoFinal;

function startStatus() {
    $('#start-button').click(function(){
    if($('#actividadInput').val() == ''){
      alert('Input can not be left blank');
    }
    else{
      startTime();
    }
    });
}

function startTime(){
      document.getElementById("start-button").hidden = true;
      document.getElementById("finish-button").hidden = false;
      fechaVieja = new Date();
      intervalId = setInterval(muestraReloj, 1000);
}

function finishStatus() {
    document.getElementById("start-button").hidden = false;
    document.getElementById("finish-button").hidden = true;
    stopTime();
}

function muestraReloj() {
    var fechaActual = new Date();
    var diferencia = fechaActual-fechaVieja;
    var diferenciaSeg = Math.floor(diferencia / 1000);
    var segundos = diferenciaSeg % 60;
    var minutos = Math.floor(diferenciaSeg / 60) % 60;
    var horas = Math.floor(diferenciaSeg / 3600);
  
    if(horas < 10) { horas = '0' + horas; }
    if(minutos < 10) { minutos = '0' + minutos; }
    if(segundos < 10) { segundos = '0' + segundos; }
  
    tiempoFinal = horas+':'+minutos+':'+segundos;
    document.getElementById("reloj").innerHTML = tiempoFinal;
  }

  function stopTime(){
    var saveTime = tiempoFinal;
    tiempoFinal = '00:00:00';
    document.getElementById("reloj").innerHTML = '00:00:00';
    clearInterval(intervalId);
  }