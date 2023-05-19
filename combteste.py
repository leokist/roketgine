
from combustao import *



comb2 = Combustao(comb=c2h5oh_L, oxid=o2_L)
comb2.reacao_combustao(razao_equiv=1.1)
print(comb2.reacao_combustao_resultado)