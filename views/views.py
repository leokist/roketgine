from flask import render_template, request
from app import app
from combustao import *

@app.route('/')
def index():
    return render_template('principal.html', titulo="Rocketgine")

@app.route('/resultado', methods=["POST",])
def resultado():

    """ Sem utilizar o WTForms:"""
    # request pega a informação da tag que contém o atributo nome definido
    raz_eq = request.form['raz_eq']
    comb = request.form['comb']
    oxid = request.form['oxid']
    #comb_temp = request.form['comb_temp']
    #oxid_temp = request.form['oxid_temp']
    
    reacao = Combustao(eval(comb), eval(oxid))
    reacao.reacao_estequiometrica()

    #return render_template('principal.html',
    #    resultado_estequiometrico=reacao.reacao_estequiometrica_resultado,
    #    titulo="Rocketgine"
    #)

 
    if float(raz_eq) == 1:
        return render_template('principal.html',
            resultado_estequiometrico=reacao.reacao_estequiometrica_resultado,
            resultado_temperatura_adiabatica=reacao.temp_adiabatica(),
            titulo="Rocketgine"
        )
    else:
        return render_template('principal.html',
            resultado_estequiometrico=reacao.reacao_estequiometrica_resultado,
            resultado_dissociacao=reacao.reacao_dissociacao_resultado,
            titulo="Rocketgine"
        )
