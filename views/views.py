from flask import render_template, request
from app import app
from rocketgine_lib import *

@app.route('/')
def index():
    return render_template('principal.html', rota = "/")

@app.route('/resultado', methods=["POST",])
def resultado():
    
    """ Sem utilizar o WTForms:"""
    # request pega a informação da tag que contém o atributo nome definido
    raz_eq = request.form['raz_eq']
    comb = eval(request.form['comb'])
    oxid = eval(request.form['oxid'])
    pressao_camara = request.form['pressao_camara']
    pressao_ambiente = request.form['pressao_externa']
    comp_caract = request.form['comp_caract']
    forca_empuxo = request.form['forca_empuxo']

    #comb_temp = request.form['comb_temp']
    #oxid_temp = request.form['oxid_temp']
    
    #reacao = Combustao(eval(comb), eval(oxid))
    #reacao.reacao_estequiometrica()
    motor = Motor(comb, oxid, eval(raz_eq), eval(pressao_camara), eval(pressao_ambiente))
    motor.combustao_estequiometrica()
    motor.escoamento_compressivel()  

    if float(raz_eq) == 1:
        #motor = CamaraCombustao(forca_empuxo, comp_caract, pressao_camara, pressao_ambiente)
        
        return render_template('principal.html',
            rota = "/resultado",
            resultado_combustao = motor.combustao_resultado,
            resultado_comb_nome = comb.propelente_nome,
            resultado_comb_composicao = comb.propelente_composicao,
            resultado_comb_estado = comb.propelente_estado,
            resultado_comb_mols = motor.comb_mols,
            resultado_comb_massa_molar = comb.propelente_massa_molar,
            resultado_oxid_nome = oxid.propelente_nome,
            resultado_oxid_composicao = oxid.propelente_composicao,
            resultado_oxid_estado = oxid.propelente_estado,
            resultado_oxid_mols = motor.oxid_mols,
            resultado_oxid_massa_molar = oxid.propelente_massa_molar,

            len = len(motor.comb_produtos),
            produtos_elementos = motor.comb_produtos,

            resultado_razao_equiv = motor.razao_equiv,
            resultado_razao_mistura = motor.razao_mistura,


            resultado_t_1 = motor.temperatura_1,
            resultado_t_g = motor.temperatura_g,
            resultado_t_2 = motor.temperatura_2,
            resultado_p_1 = motor.pressao_1,
            resultado_p_g = motor.pressao_g,
            resultado_p_2 = motor.pressao_2,
            resultado_v_1 = motor.velocidade_1,
            resultado_v_g = motor.velocidade_g,
            resultado_v_2 = motor.velocidade_2,
            resultado_a_1 = motor.velocidade_som_1,
            resultado_a_g = motor.velocidade_som_g,
            resultado_a_2 = motor.velocidade_som_2,
            resultado_mach_1 = motor.num_mach_1,
            resultado_mach_g = motor.num_mach_g,
            resultado_mach_2 = motor.num_mach_2,
            resultado_vol_esp_1 = motor.volume_especifico_1,
            resultado_vol_esp_g = motor.volume_especifico_g,
            resultado_vol_esp_2 = motor.volume_especifico_2,
            resultado_massa_esp_1 = motor.massa_especifica_1,
            resultado_massa_esp_g = motor.massa_especifica_g,
            resultado_massa_esp_2 = motor.massa_especifica_2,
            #resultado_temperatura_adiabatica=reacao.temperatura_adiabatica,
            #resultado_razao_mistura=reacao.razao_mistura,
            #resultado_massa_molar_media=reacao.massa_molar_media,
            #resultado_cp_medio=reacao.cp_medio,
            #resultado_constante_gases=reacao.constante_gases,
            #resultado_cv_medio=reacao.cv_medio,
            #resultado_k=reacao.k,
            #resultado_entalpia_reag=reacao.entalpia_reagentes,
            #resultado_entalpia_prod=reacao.entalpia_produtos,
            #titulo="Rocketgine"
        )
    else:
        reacao.reacao_dissociacao(eval(raz_eq), eval(pressao_camara))
        return render_template('principal.html',
            resultado_combustao=reacao.combustao_resultado,
            resultado_temperatura_adiabatica=reacao.temperatura_adiabatica,
            resultado_razao_mistura=reacao.razao_mistura,
            resultado_entalpia_reag=reacao.entalpia_reagentes,
            resultado_entalpia_prod=reacao.entalpia_produtos,
            #titulo="Rocketgine"
        )
