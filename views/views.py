from flask import render_template, request
from app import app
from rocketgine_lib import *

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
    pressao_camara = request.form['pressao_camara']
    comp_caract = request.form['comp_caract']
    forca_empuxo = request.form['forca_empuxo']

    #comb_temp = request.form['comb_temp']
    #oxid_temp = request.form['oxid_temp']
    
    reacao = Combustao(eval(comb), eval(oxid))
    reacao.reacao_estequiometrica()
 
    if float(raz_eq) == 1:
        return render_template('principal.html',
            resultado_combustao=reacao.combustao_resultado,
            resultado_temperatura_adiabatica=reacao.temperatura_adiabatica,
            resultado_razao_mistura=reacao.razao_mistura,
            resultado_entalpia_reag=reacao.entalpia_reagentes,
            resultado_entalpia_prod=reacao.entalpia_produtos,
            titulo="Rocketgine"
        )
    else:
        reacao.reacao_dissociacao(eval(raz_eq), eval(pressao_camara))
        return render_template('principal.html',
            resultado_combustao=reacao.combustao_resultado,
            resultado_temperatura_adiabatica=reacao.temperatura_adiabatica,
            resultado_razao_mistura=reacao.razao_mistura,
            resultado_entalpia_reag=reacao.entalpia_reagentes,
            resultado_entalpia_prod=reacao.entalpia_produtos,
            titulo="Rocketgine"
        )
