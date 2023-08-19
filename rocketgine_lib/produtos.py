from .constantes import *
from math import log, e

class Gas():
    """Cria um objeto Gás com suas propriedades
    massa_molar: [kg/mol] | entalpia_formacao: [J/mol] | entalpia_t_referência [J/mol]
    """
    def __init__(self, nome, composicao, entalpia_formacao, entalpia_t_referencia, massa_molar, mols_c, mols_o, mols_h, mols_n):
        self.nome = nome
        self.composicao = composicao
        self.entalpia_formacao = entalpia_formacao
        self.entalpia_t_referencia = entalpia_t_referencia
        self.massa_molar = massa_molar
        self.mols_c = mols_c
        self.mols_o = mols_o
        self.mols_h = mols_h
        self.mols_n = mols_n
    
    def __repr__(self):
        return f"{self.composicao}"
        
    def coeficientes_200_1000(self, temp_max, temp_min, a1, a2, a3, a4, a5, a6, a7, b1, b2):
        """Define os coeficientes de um gás entre as temperaturas de 200°C a 1000°C"""
        self.temp_max = temp_max
        self.temp_min = temp_min
        self.__a1_temp_200_1000 = a1
        self.__a2_temp_200_1000 = a2
        self.__a3_temp_200_1000 = a3
        self.__a4_temp_200_1000 = a4
        self.__a5_temp_200_1000 = a5
        self.__a6_temp_200_1000 = a6
        self.__a7_temp_200_1000 = a7
        self.__b1_temp_200_1000 = b1
        self.__b2_temp_200_1000 = b2
    
    def coeficientes_1000_6000(self, temp_max, temp_min, a1, a2, a3, a4, a5, a6, a7, b1, b2):
        """Define os coeficientes de um gás entre as temperaturas de 1000°C a 6000°C"""
        self.temp_max = temp_max
        self.temp_min = temp_min
        self.__a1_temp_1000_6000 = a1
        self.__a2_temp_1000_6000 = a2
        self.__a3_temp_1000_6000 = a3
        self.__a4_temp_1000_6000 = a4
        self.__a5_temp_1000_6000 = a5
        self.__a6_temp_1000_6000 = a6
        self.__a7_temp_1000_6000 = a7
        self.__b1_temp_1000_6000 = b1
        self.__b2_temp_1000_6000 = b2
    
    #def coeficientes_6000_20000(self, temp_max, temp_min, a1, a2, a3, a4, a5, a6, a7, b1, b2):
    #    """Define os coeficientes de um gás entre as temperaturas de 1000°C a 6000°C"""
    #    self.temp_max = temp_max
    #    self.temp_min = temp_min
    #    self.__a1_temp_6000_20000 = a1
    #    self.__a2_temp_6000_20000 = a2
    #    self.__a3_temp_6000_20000 = a3
    #    self.__a4_temp_6000_20000 = a4
    #    self.__a5_temp_6000_20000 = a5
    #    self.__a6_temp_6000_20000 = a6
    #    self.__a7_temp_6000_20000 = a7
    #    self.__b1_temp_6000_20000 = b1
    #    self.__b2_temp_6000_20000 = b2

    def __coeficiente(self, temperatura):
        """Define qual coeficiente será utilizado com base no valor da temperatura informada"""
        self.temperatura = temperatura
        t = self.temperatura
        if t >= 200 and t <= 1000:
            self.a1 = self.__a1_temp_200_1000
            self.a2 = self.__a2_temp_200_1000
            self.a3 = self.__a3_temp_200_1000
            self.a4 = self.__a4_temp_200_1000
            self.a5 = self.__a5_temp_200_1000
            self.a6 = self.__a6_temp_200_1000
            self.a7 = self.__a7_temp_200_1000
            self.b1 = self.__b1_temp_200_1000
            self.b2 = self.__b2_temp_200_1000
        elif t >= 1000 and t <= 6000:
            self.a1 = self.__a1_temp_1000_6000
            self.a2 = self.__a2_temp_1000_6000
            self.a3 = self.__a3_temp_1000_6000
            self.a4 = self.__a4_temp_1000_6000
            self.a5 = self.__a5_temp_1000_6000
            self.a6 = self.__a6_temp_1000_6000
            self.a7 = self.__a7_temp_1000_6000
            self.b1 = self.__b1_temp_1000_6000
            self.b2 = self.__b2_temp_1000_6000

        #elif t >= 6000 and t <= 20000:
        #    self.a1 = self.__a1_temp_6000_20000
        #    self.a2 = self.__a2_temp_6000_20000
        #    self.a3 = self.__a3_temp_6000_20000
        #    self.a4 = self.__a4_temp_6000_20000
        #    self.a5 = self.__a5_temp_6000_20000
        #    self.a6 = self.__a6_temp_6000_20000
        #    self.a7 = self.__a7_temp_6000_20000
        #    self.b1 = self.__b1_temp_6000_20000
        #    self.b2 = self.__b2_temp_6000_20000

    def entropia(self, temperatura):
        """Executa o cálculo da Entropia gás a uma determinada temperatura [J/molK]"""
        self.temperatura = temperatura
        t = self.temperatura
        self.__coeficiente(t)
        self.s = Constantes.const_univ_gases()*(-(self.a1/(2*t**2))-(self.a2/t)+(self.a3*log(t))+(self.a4*t)+((self.a5*t**2)/2)+((self.a6*t**3)/3)+((self.a7*t**4)/4)+(self.b2))
        #print(f"entropia: { self.composicao} {self.s}")
        return self.s

    def entalpia(self, temperatura):
        """Executa o cálculo da Entalpia do gás a uma determinada temperatura [J/mol]"""
        self.temperatura = temperatura
        t = self.temperatura
        self.__coeficiente(t)
        self.h = Constantes.const_univ_gases()*t*((-self.a1/(t**2))+(self.a2*log(t)/t)+self.a3+(self.a4*t/2)+(self.a5*(t**2)/3)+(self.a6*(t**3)/4)+(self.a7*(t**4)/5)+(self.b1/t))
        #print(f"entalpia: { self.composicao} {self.h}")
        return self.h

    def calor_especifico(self, temperatura):
        """Executa o cálculo do Calor Específico do gás a uma determinada temperatura [J/molK]"""
        self.temperatura = temperatura
        t = self.temperatura
        self.__coeficiente(t)
        #self.cp = ((self.a1*(t**-2))+(self.a2*(t**-1))+self.a3+(self.a4*t)+(self.a5*(t**2))+(self.a6*(t**3))+(self.a7*(t**4))*Constantes.const_univ_gases())
        self.cp = ((self.a1/(t**2))+(self.a2/t)+self.a3+(self.a4*t)+(self.a5*(t**2))+(self.a6*(t**3))+(self.a7*(t**4)))*Constantes.const_univ_gases()
        #print(f"cp: { self.composicao} {self.cp}")
        return self.cp
    
    def funcao_gibbs(self, temperatura):
        """Executa o cálculo da Função de Gibbs [J/mol]"""
        self.temperatura = temperatura
        t = temperatura
        hf = self.entalpia_formacao
        href = self.entalpia_t_referencia
        h = self.entalpia(t)
        s = self.entropia(t)
        self.gibbs = hf + h - href - (t * s)
        #print(f"{self.composicao} href:{href}, hf:{hf}, h:{h}, s:{s}, gibbs:{self.gibbs}")
        return self.gibbs

"""
Dados obtidos de:
NASA Glenn coefficients for calculating thermodynamic properties of individual species.
GORDON, S.; MCBRIDE, B. J.; ZEHE M. J.
Glenn Research Center, 2002.
"""

H = Gas(
    nome = "Hidrogênio",
    composicao = "H",
    entalpia_formacao = 217998.828,
    entalpia_t_referencia = 6197,
    massa_molar = 1.00794,
    mols_c = 0,
    mols_o = 0,
    mols_h = 1,
    mols_n = 0
)
H2 = Gas(
    nome = "",
    composicao = "H2",
    entalpia_formacao = 0.000,
    entalpia_t_referencia = 8468,
    massa_molar = 2.01588,
    mols_c = 0,
    mols_o = 0,
    mols_h = 1,
    mols_n = 0
)
H2O = Gas(
    nome = "aguá",
    composicao = "H2O",
    entalpia_formacao = -241826.000,
    entalpia_t_referencia = 9904,
    massa_molar = 18.01528,
    mols_c = 0,
    mols_o = 1,
    mols_h = 2,
    mols_n = 0
)
O = Gas(
    nome = "",
    composicao = "O",
    entalpia_formacao = 249175.003,
    entalpia_t_referencia = 6725,
    massa_molar = 15.99940,
    mols_c = 0,
    mols_o = 1,
    mols_h = 0,
    mols_n = 0
)
O2 = Gas(
    nome = "",
    composicao = "O2",
    entalpia_formacao = 0.000,
    entalpia_t_referencia = 8680,
    massa_molar = 31.99880,
    mols_c = 0,
    mols_o = 2,
    mols_h = 0,
    mols_n = 0
)
OH = Gas(
    nome ="",
    composicao = "OH",
    entalpia_formacao = 37278.206,
    entalpia_t_referencia = 8813,
    massa_molar = 17.00734,
    mols_c = 0,
    mols_o = 1,
    mols_h = 1,
    mols_n = 0
)
CO = Gas(
    nome = "",
    composicao = "CO",
    entalpia_formacao = -110535.196,
    entalpia_t_referencia = 8671,
    massa_molar = 28.01010,
    mols_c = 1,
    mols_o = 1,
    mols_h = 0,
    mols_n = 0
)
CO2 = Gas(
    nome = "",
    composicao = "CO2",
    entalpia_formacao = -393510.000,
    entalpia_t_referencia = 9365,
    massa_molar = 44.00950,
    mols_c = 1,
    mols_o = 2,
    mols_h = 0,
    mols_n = 0
)
N2 = Gas(
    nome = "",
    composicao = "N2",
    entalpia_formacao = 0,
    entalpia_t_referencia = 8670,
    massa_molar = 28.0134,
    mols_c = 0,
    mols_o = 0,
    mols_h = 0,
    mols_n = 2
)
N = Gas(
    nome = "",
    composicao = "N",
    entalpia_formacao = 472680,
    entalpia_t_referencia = 6197,
    massa_molar = 14.0067,
    mols_c = 0,
    mols_o = 0,
    mols_h = 0,
    mols_n = 1
)
NO = Gas(
    nome = "",
    composicao = "NO",
    entalpia_formacao = 91271,
    entalpia_t_referencia = 9179,
    massa_molar = 30.00610,
    mols_c = 0,
    mols_o = 1,
    mols_h = 0,
    mols_n = 1,
)

H.coeficientes_200_1000(1000, 200, 0.00000000E+00, 0.00000000E+00, 2.50000000E+00, 0.00000000E+00, 0.00000000E+00, 0.00000000E+00, 0.00000000E+00, 2.54737080E+04, -4.466828530E-01)
H2.coeficientes_200_1000(1000, 200,	4.07832321E+04, -8.00918604E+02, 8.21470201E+00, -1.26971446E-02, 1.75360508E-05, -1.20286027E-08, 3.36809349E-12, 2.68248467E+03, -3.043788844E+01)
H2O.coeficientes_200_1000(1000, 200, -3.9479608E+04, 5.75573102E+02, 9.31782653E-01, 7.22271286E-03, -7.34255737E-06, 4.95504349E-09, -1.33693325E-12, -3.30397431E+04, 1.724205775E+01)
O.coeficientes_200_1000(1000, 200, -7.95361130E+03, 1.60717779E+02, 1.96622644E+00, 1.01367031E-03, -1.11041542E-06, 6.51750750E-10, -1.58477925E-13, 2.84036244E+04, 8.404241820E+00)
O2.coeficientes_200_1000(1000, 200,	-3.42556342E+04, 4.84700097E+02, 1.11901096E+00, 4.29388924E-03, -6.83630052E-07, -2.02337270E-09, 1.03904002E-12, -3.39145487E+03, 1.849699470E+01)
OH.coeficientes_200_1000(1000, 200,	-1.99885899E+03, 9.30013616E+01, 3.05085423E+00, 1.52952929E-03, -3.15789100E-06, 3.31544618E-09, -1.13876268E-12, 2.99121424E+03, 4.674110790E+00)
CO.coeficientes_200_1000(1000, 200,	1.48904533E+04, -2.92228594E+02, 5.72452717E+00, -8.17623503E-03, 1.45690347E-05, -1.08774630E-08, 3.02794183E-12, -1.30313188E+04, -7.859241350E+00)
CO2.coeficientes_200_1000(1000, 200, 4.94365054E+04, -6.26411601E+02, 5.30172524E+00, 2.50381382E-03, -2.12730873E-07, -7.68998878E-10, 2.84967780E-13, -4.52819846E+04, -7.048279440E+00)
N2.coeficientes_200_1000(1000, 200, 2.210371497E+04, -3.818461820E+02, 6.082738360E+00, -8.530914410E-03, 1.384646189E-05, -9.625793620E-09, 2.519705809E-12, 7.108460860E+02, -1.076003744E+01)
N.coeficientes_200_1000(1000, 200, 0.000000000E+00, 0.000000000E+00, 2.500000000E+00, 0.000000000E+00, 0.000000000E+00, 0.000000000E+00, 0.000000000E+00, 5.610463780E+04, 4.193905036E+00)
NO.coeficientes_200_1000(1000, 200, -1.143916503E+04, 1.536467592E+02, 3.431468730E+00, -2.668592368E-03, 8.481399120E-06, -7.685111050E-09, 2.386797655E-12, 9.098214410E+03, 6.728725490E+00)


H.coeficientes_1000_6000(6000, 1000, 6.07877425E+01, -1.81935442E-01, 2.50021182E+00, -1.22651286E-07, 3.73287633E-11, -5.68774456E-15, 3.41021020E-19, 2.54748640E+04, -4.481917770E-01)
H2.coeficientes_1000_6000(6000, 1000, 5.60812801E+05, -8.37150474E+02, 2.97536453E+00, 1.25224912E-03, -3.74071619E-07, 5.93662520E-11, -3.60699410E-15, 5.33982441E+03, -2.202774769E+00)
H2O.coeficientes_1000_6000(6000, 1000, 1.03497210E+06, -2.41269856E+03, 4.64611078E+00, 2.29199831E-03, -6.83683048E-07, 9.42646893E-11, -4.82238053E-15, -1.38428651E+04, -7.978148510E+00)
O.coeficientes_1000_6000(6000, 1000, 2.61902026E+05, -7.29872203E+02, 3.31717727E+00, -4.28133436E-04, 1.03610459E-07, -9.43830433E-12, 2.72503830E-16, 3.39242806E+04, -6.679585350E-01)
O2.coeficientes_1000_6000(6000, 1000, -1.03793902E+06, 2.34483028E+03, 1.81973204E+00, 1.26784758E-03, -2.18806799E-07, 2.05371957E-11, -8.19346705E-16, -1.68901093E+04, 1.738716506E+01)
OH.coeficientes_1000_6000(6000, 1000, 1.01739338E+06, -2.50995728E+03, 5.11654786E+00, 1.30529993E-04, -8.28432226E-08, 2.00647594E-11, -1.55699366E-15, 2.01964021E+04, -1.101282337E+01)
CO.coeficientes_1000_6000(6000, 1000, 4.61919725E+05, -1.94470486E+03, 5.91671418E+00, -5.66428283E-04, 1.39881454E-07, -1.78768036E-11, 9.62093557E-16, -2.46626108E+03, -1.387413108E+01)
CO2.coeficientes_1000_6000(6000, 1000, 1.17696242E+05, -1.78879148E+03, 8.29152319E+00, -9.22315678E-05, 4.86367688E-09, -1.89105331E-12, 6.33003659E-16, -3.90835059E+04, -2.652669281E+01)
N2.coeficientes_1000_6000(6000, 1000, 5.877124060E+05, -2.239249073E+03, 6.066949220E+00, -6.139685500E-04, 1.491806679E-07, -1.923105485E-11, 1.061954386E-15, 1.283210415E+04, -1.586640027E+01)
N.coeficientes_1000_6000(6000, 1000, 8.876501380E+04, -1.071231500E+02, 2.362188287E+00, 2.916720081E-04, -1.729515100E-07, 4.012657880E-11, -2.677227571E-15, 5.697351330E+04, 4.865231506E+00)
NO.coeficientes_1000_6000(6000, 1000, 2.239018716E+05, -1.289651623E+03, 5.433936030E+00, -3.656034900E-04, 9.880966450E-08, -1.416076856E-11, 9.380184620E-16, 1.750317656E+04, -8.501669090E+00)              

#H.coeficientes_6000_20000(20000, 6000, )
#H2.coeficientes_6000_20000(20000, 6000, )
#H2O.coeficientes_6000_20000(20000, 6000, )
#O.coeficientes_6000_20000(20000, 6000, )
#O2.coeficientes_6000_20000(20000, 6000, )
#OH.coeficientes_6000_20000(20000, 6000, )
#CO.coeficientes_6000_20000(20000, 6000, 8.868662960E+08, -7.500377840E+05, 2.495474979E+02, -3.956351100E-02, 3.297772080E-06,-1.318409933E-10, 1.998937948E-15, 5.701421130E+06, -2.060704786E+03)
#CO2.coeficientes_6000_20000(20000, 6000, -1.544423287E+09, 1.016847056E+06, -2.561405230E+02, 3.369401080E-02, -2.181184337E-06, 6.991420840E-11, -8.842351500E-16, -8.043214510E+06, 2.254177493E+03)
#N2.coeficientes_6000_20000(20000, 6000, )
#N.coeficientes_6000_20000(20000, 6000, )
#NO.coeficientes_6000_20000(20000, 6000, )              
