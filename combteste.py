
from combustao import *

razao_equiv="1"

#comb2 = Combustao(comb=c2h5oh_L, oxid=o2_L) #OK RE=1 | RE=?
#comb2 = Combustao(comb=c2h5oh_L, oxid=ar_G) #OK RE=1 | RE=?
#comb2 = Combustao(comb=c2h5oh_L, oxid=h2o2_L) #OK RE=1 | RE=?
#comb2 = Combustao(comb=c2h5oh_L, oxid=hno3_L) #OK RE=1 | RE=?

#comb2 = Combustao(comb=h2_L, oxid=o2_L) #OK RE=1 | RE=?
#comb2 = Combustao(comb=h2_L, oxid=ar_G) #OK RE=1 | RE=?
#comb2 = Combustao(comb=h2_L, oxid=h2o2_L) #OK RE=1 | RE=?
#comb2 = Combustao(comb=h2_L, oxid=hno3_L) #OK RE=1 | RE=?

#comb2 = Combustao(comb=c8h18_L, oxid=o2_L) #OK RE=1 | RE=?
#comb2 = Combustao(comb=c8h18_L, oxid=ar_G) #OK RE=1 | RE=?
#comb2 = Combustao(comb=c8h18_L, oxid=h2o2_L) #OK RE=1 | RE=?
#comb2 = Combustao(comb=c8h18_L, oxid=hno3_L) #OK RE=1 | RE=?
 
#comb2 = Combustao(comb=c3h8_L, oxid=o2_L) #OK RE=1 | RE=?
comb2 = Combustao(comb=c3h8_L, oxid=ar_G) #OK RE=1 | RE=?
#comb2 = Combustao(comb=c3h8_L, oxid=h2o2_L) #OK RE=1 | RE=?
#comb2 = Combustao(comb=c3h8_L, oxid=hno3_L) #OK RE=1 | RE=?

#comb2 = Combustao(comb=c2h8n2_L, oxid=o2_L) #OK RE=1 | RE=?
#comb2 = Combustao(comb=c2h8n2_L, oxid=ar_G) #OK RE=1 | RE=?
#comb2 = Combustao(comb=c2h8n2_L, oxid=h2o2_L) #OK RE=1 | RE=?
#comb2 = Combustao(comb=c2h8n2_L, oxid=hno3_L) #OK RE=1 | RE=?

#comb2 = Combustao(comb=nh3_L, oxid=o2_L) #OK RE=1 | RE=?
#comb2 = Combustao(comb=nh3_L, oxid=ar_G) #OK RE=1 | RE=?
#comb2 = Combustao(comb=nh3_L, oxid=h2o2_L) #OK RE=1 | RE=?
#comb2 = Combustao(comb=nh3_L, oxid=hno3_L)  #OK RE=1 | RE=?

comb2.reacao_combustao(float(razao_equiv))
print(comb2.reacao_estequiometrica_resultado)
print(comb2.reacao_dissociacao_resultado)
