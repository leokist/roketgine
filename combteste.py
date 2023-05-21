
from combustao import *

razao_equiv="1"


comb2 = Combustao(comb=c2h8n2_L, oxid=ar_G)
comb2.reacao_combustao(float(razao_equiv))
print(comb2.reacao_estequiometrica_resultado)
print(comb2.reacao_dissociacao_resultado)