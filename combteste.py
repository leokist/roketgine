
from rocketgine_lib import *

#comb2 = Combustao(comb=C2H5OH_L, oxid=O2_L)


#comb2.reacao_estequiometrica()
#print(comb2.combustao_resultado)
#print(comb2.temperatura_adiabatica)
#comb2 = CamaraCombustao(500, 2, 15, 1)

comb = C2H5OH_L


teste = Motor(comb=comb, oxid=O2_L, razao_equiv=1, forca_empuxo=500, comprimento_caracteristico=2 ,pressao=15)
teste.combustao_estequiometrica()
teste.escoamento_compressivel()
teste.parametros_performance()
teste.geometria()

print(( 4.937 - 2.79)/tan(15*pi/180) )
#print(teste.combustao_resultado)
#print(teste.temperatura_adiabatica)


#r1 = 4.938
#rg = 2.790

#teste_lg = r1 - rg / tan(15) 
#print(teste_lg, tan(15*pi/180), tan(15) )

