
from rocketgine_lib import *

#comb2 = Combustao(comb=C2H5OH_L, oxid=O2_L)


#comb2.reacao_estequiometrica()
#print(comb2.combustao_resultado)
#print(comb2.temperatura_adiabatica)
#comb2 = CamaraCombustao(500, 2, 15, 1)

comb = C2H5OH_L
#comb = H2_L
#comb = C8H18_L   
oxid = O2 
#oxid = Air_G
#oxid = H2O2_L
#oxid = HNO3_L

teste = Motor(comb=comb, oxid=oxid, razao_equiv=1, forca_empuxo=500, comprimento_caracteristico=2 ,pressao=15)
teste.reacao_estequiometrica()

teste.reacao_dissociacao()
print(teste.status_reacao)


#teste.escoamento_compressivel()
#teste.parametros_performance()
#teste.geometria()asdfasdf
#teste.reacao_dissociacao
#t=3215.005636
#a = reacao_2CO2_para_2CO_O2.kp(t)
#a = reacao_N2_para_2N.kp(5000)
#a = reacao_H2O_para_H2_05O2.kp(t)
#a = reacao_H2_para_2H.kp(4000)
#print(a)\

#H.funcao_gibbs(t)
#H2.funcao_gibbs(t)
#H2O.funcao_gibbs(t)
#O.funcao_gibbs(t)
#O2.funcao_gibbs(t)
#OH.funcao_gibbs(t)
#CO.funcao_gibbs(t)
#CO2.funcao_gibbs(t)



#print(( 4.937 - 2.79)/tan(15*pi/180) )
#print(teste.combustao_resultado)
#print(teste.temperatura_adiabatica)


#r1 = 4.938
#rg = 2.790

#teste_lg = r1 - rg / tan(15) 
#print(teste_lg, tan(15*pi/180), tan(15) )

