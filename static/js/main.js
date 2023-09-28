function msgRazEq() {
    alert("Re = 1 : Reação Estequiométrica\n" +
          "Re > 1 : Reação Rica em Combustivel\n" +
          "Re < 1 : Reação Pobre em Combustível");
}

/*
window.onload = function () {
    const mainForm = document.getElementById("formDadosEntrada")
    const resultado = document.getElementById("div_resultado")
    mainForm.onsubmit = function(event) {
        event.preventDefault();
        fetch("/resultado", {
            method: "POST"
        })
/*

/*
window.onload = function () {
    const mainForm = document.getElementById("formDadosEntrada")
    const resultado = document.getElementById("div_resultado")
    mainForm.onsubmit = function(event) {
        event.preventDefault();
        fetch("/resultado", {
            method: "POST"
        })
        .then(Response => {
            //do something with fil
        })
        .then(() => {
            fetch("/resultado", {
                method: "POST"
           })
            .then(response => {
                return response.text();
           })
            .then(html => {
                resultado.innerHTML = html;
            })
        })
    }
}
*/
/*
Document.ready( function() {
    const botao_calcular = document.getElementById("botao_calcular")
    const div_resultado = document.getElementById("div_resultado")
    botao_calcular.click(function() {
        ajax.document('resultado').done(function(reply) {
            div_resultado.html(reply);
        //ajax("{{ url_for("resultado") }}").done(function(reply) {
        //   div_resultado.html(reply);
        })
    })
})
*/

/*
$(document).ready( function() {
   $('#next').click(function() {
       $.ajax("{{ url_for('yourroute') }}").done(function (reply) {
          $('#container').html(reply);
       });
    });
});
*/