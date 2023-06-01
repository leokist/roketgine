
from combustao import *

comb2 = Combustao(comb=C2H5OH_L, oxid=O2_L) #OK RE=1 | RE=?
#comb2 = Combustao(comb=C2H5OH_L, oxid=Air_G) #OK RE=1 | RE=?
#comb2 = Combustao(comb=C2H5OH_L, oxid=H2O2_L) #OK RE=1 | RE=?
#comb2 = Combustao(comb=C2H5OH_L, oxid=HNO3_L) #OK RE=1 | RE=?

#comb2 = Combustao(comb=H2_L, oxid=O2_L) #OK RE=1 | RE=?
#comb2 = Combustao(comb=h2_L, oxid=ar_G) #OK RE=1 | RE=?
#comb2 = Combustao(comb=h2_L, oxid=h2o2_L) #OK RE=1 | RE=?
#comb2 = Combustao(comb=h2_L, oxid=hno3_L) #OK RE=1 | RE=?

#comb2 = Combustao(comb=C8H18_L, oxid=o2_L) #OK RE=1 | RE=?
#comb2 = Combustao(comb=C8H18_L, oxid=Air_G) #OK RE=1 | RE=?
#comb2 = Combustao(comb=C8H18_L, oxid=h2o2_L) #OK RE=1 | RE=?
#comb2 = Combustao(comb=C8H18_L, oxid=hno3_L) #OK RE=1 | RE=?

#comb2 = Combustao(comb=c3h8_L, oxid=o2_L) #OK RE=1 | RE=?
#comb2 = Combustao(comb=c3h8_L, oxid=ar_G) #OK RE=1 | RE=?
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


comb2.reacao_estequiometrica()
print(comb2.reacao_estequiometrica_resultado)
#print(comb2.reacao_dissociacao_resultado)

comb2.temp_adiabatica()
comb2.reacao_dissociacao(1.5, 15)

print(reacao_N2_para_2N.reacao())
print(reacao_N2_para_2N.kp(423))


