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
    tipo_bocal = request.form['tipo_bocal']

    #comb_temp = request.form['comb_temp']
    #oxid_temp = request.form['oxid_temp']
    
    #reacao = Combustao(eval(comb), eval(oxid))
    #reacao.reacao_estequiometrica()
    motor = Motor(comb, oxid, eval(raz_eq), eval(forca_empuxo), eval(comp_caract), eval(pressao_camara), eval(pressao_ambiente))
    motor.combustao_estequiometrica()
    motor.escoamento_compressivel()  
    motor.parametros_performance()
    motor.geometria()

    if float(raz_eq) == 1:
        #motor = CamaraCombustao(forca_empuxo, comp_caract, pressao_camara, pressao_ambiente)
        
        return render_template('principal.html',
            rota = "/resultado",
            tipo_bocal = tipo_bocal,
            # Tabela Propelentes da Combustao
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

            resultado_razao_equiv = motor.razao_equiv,
            resultado_razao_mistura = motor.razao_mistura,

            # Tabela Produtos da Combustao
            len = len(motor.comb_produtos),
            produtos_elementos = motor.comb_produtos,

            # Tabela Propriedades Termodinâmicas / Escoamento Compressível
            resultado_t_1 = motor.t_1,
            resultado_t_g = motor.t_g,
            resultado_t_2 = motor.t_2,
            resultado_p_1 = motor.p_1,
            resultado_p_g = motor.p_g,
            resultado_p_2 = motor.p_2,
            resultado_v_1 = motor.v_1,
            resultado_v_g = motor.v_g,
            resultado_v_2 = motor.v_2,
            resultado_a_1 = motor.a_1,
            resultado_a_g = motor.a_g,
            resultado_a_2 = motor.a_2,
            resultado_mach_1 = motor.mach_1,
            resultado_mach_g = motor.mach_g,
            resultado_mach_2 = motor.mach_2,
            resultado_vol_esp_1 = motor.vol_esp_1,
            resultado_vol_esp_g = motor.vol_esp_g,
            resultado_vol_esp_2 = motor.vol_esp_2,
            resultado_massa_esp_1 = motor.rho_1,
            resultado_massa_esp_g = motor.rho_g,
            resultado_massa_esp_2 = motor.rho_2,

            # Tabela Parâmetros de Performance
            resultado_razao_expansao = motor.razao_expansao,
            resultado_coeficiente_empuxo = motor.coeficiente_empuxo,
            resultado_razao_contracao = motor.razao_contracao,
            resultado_vazao_massica_total_propelentes = motor.vazao_massica_total_propelente,
            resultado_impulso_especifico = motor.impulso_especifico,
            resultado_velocidade_efetiva_exaustao = motor.v_efetiva_exaustao,
            resultado_velocidade_caracteristica = motor.v_caracteristica,

            # Tabela Geometria
            resultado_l_estrela = comp_caract,
            resultado_volume_total = motor.vol_total,
            resultado_lc = motor.lc,
            resultado_lg = motor.lg,
            resultado_l = motor.l,
            resultado_l_60 = motor.l_60,
            resultado_l_80 = motor.l_80,
            resultado_r1 = motor.r_1,
            resultado_rg = motor.r_g,
            resultado_r2 = motor.r_2,
            resultado_r3 = motor.r_3,
            resultado_r4 = motor.r_4,
            resultado_r5 = motor.r_5,

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
