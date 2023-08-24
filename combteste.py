
from rocketgine_lib import *

#comb2 = Combustao(comb=C2H5OH_L, oxid=O2_L)


#comb2.reacao_estequiometrica()
#print(comb2.combustao_resultado)
#print(comb2.temperatura_adiabatica)
#comb2 = CamaraCombustao(500, 2, 15, 1)

comb = C2H5OH_L


teste = Motor(comb=comb, oxid=O2_L, razao_equiv=1, pressao=15)
teste.combustao_estequiometrica()

print(teste.combustao_resultado)
print(teste.temperatura_adiabatica)

