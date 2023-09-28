"""from ..constantes import *
from ..reacao import *

class CamaraCombustao(Combustao):
    """Cria um objeto Gás com suas propriedades
    massa_molar: [kg/mol] | entalpia_formacao: [J/mol] | entalpia_t_referência [J/mol]
    """
    def __init__(self, forca_empuxo, comp_caracteristico, pressao, pressao_ambiente):
        self.forca_empuxo = forca_empuxo
        self.comp_caracteristico = comp_caracteristico
        self.temp = Combustao, "temperatura_adiabatica"
        self.pressao = pressao
        self.pressao_ambiente = pressao_ambiente
    
    def escoamento_compressivel(self):
        #Ponto 1 - Camara de Combustão
        self.v_1 = 0                #Velocidade no ponto 1 [m/s]
        self.t_1 = self.temp        #Temperatura no ponto 1 [K]
        self.p_1 = self.pressao     #Pressao no ponto 1 [Pa]
        self.a_1 = (Combustao.k * Combustao.constante_gases * self.t_1)**(1/2)  #Velocidade do Som no ponto 1 [m/s]
        self.mach_1 = self.v_1 / self.a_1                                          #Número de Mach no ponto 1
        self.vol_esp_1 = Combustao.constante_gases * self.t_1 / self.p_1        #Volume Específico no ponto 1
        self.rho_1 = 1 / self.vol_esp_1                                         #Massa Específica no ponto 1

        #Propriedades de Estagnação
        #Como Mach em 1 é 0, as Propriedades de Estagnação serão iguais ao ponto 1
        self.t_0 = self.t_1         #Temperatura de Estagnação [K]
        self.p_0 = self.p_1         #Pressão de Estagnação [Pa]
        self.rho_0 = self.rho_1     #Massa Específica de estagnação

        #Ponto g - Garganta da Camara de Combustao
        self.mach_g = 1        #Número de Mach na garganta
        self.p_g = self.p_0 / ((1 + (((Combustao.k - 1) / 2) * self.mach_g ** 2)) ** (Combustao.k / (Combustao.k -1)))       #Pressão na garganta [Pa]
        self.t_g = self.t_0 / (1 + (((Combustao.k - 1) / 2) * self.mach_g ** 2))                                             #Temperatura na garganta [K]
        self.rho_g = self.rho_0 / ((1 + (((Combustao.k - 1) / 2) * self.mach_g ** 2)) ** (1 / (Combustao.k -1)))             #Pressão na garganta [Pa]
        self.vol_esp_g = 1 / self.rho_g                                                                                      #Volume Específico na garganta
        self.a_g = (Combustao.k * Combustao.constante_gases * self.t_g)**(1/2)                                               #Velocidade do Som na garganta [m/s]
        self.v_g = self.a_g * self.mach_g                                                                                    #Velocidade na garganta [m/s]

        #Ponto 2 - Saída do Bocal
        #Condição otima de expansão p2 = p3
        self.p_3 = self.pressao_ambiente                                                                                            #Pressao ambiente [Pa]
        self.p_2 = self.p_3                                                                                                         #Pressao no ponto 2 [Pa]
        self.mach_2 = ((((self.p_0 / self.p_2)**((Combustao.k - 1) / Combustao.k)) - 1) / ((Combustao.k - 1) / 2)) ** (1 / 2)       #Numero de Mach no ponto 2
        self.t_2 = self.t_0 / (1 + (((Combustao.k - 1) / 2) * self.mach_2 ** 2))                                         #Temperatura no ponto 2
        self.a_2 = (Combustao.k * Combustao.constante_gases * self.t_2) ** (1 / 2)                                       #Velocidade do som no ponto 2
        self.v_2 = self.a_2 * self.mach_2                                                                                #Velocidade no ponto 2
        self.vol_esp_2 = (Combustao.constante_gases * self.t_2) / self.p_2                                               #Volume especifico no ponto 2
        self.rho_2 = self.rho_0 / ((1 + (((Combustao.k - 1) / 2) * self.mach_2 ** 2)) ** (1 / (Combustao.k - 1)))        #Massa especifica no ponto 2

    @property
    def t_1(self):
        t_1 = self.t_1
        return t_1
    
    @property
    def t_g(self):
        t_g = self.t_g
        return t_g
    
    @property
    def t_2(self):
        t_2 = self.t_2
        return t_2"""