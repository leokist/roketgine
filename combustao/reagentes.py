class Propelente:
    """
    Classe que cria um Propelente, Combustível ou Oxidante
    massa_molar: [kg/kmol] | entalpia_formacao: [kJ/kmol] | entalpia_t_referência [kJ/kmol] | temperatura: [K] |
    """
    def __init__(self, tipo, nome, composicao, estado, massa_molar, entalpia_formacao, entalpia_t_referencia, mols_c, mols_o, mols_h, mols_n, temperatura_referencia):
        self.tipo = tipo
        self.nome = nome
        self.composicao = composicao
        self.estado = estado
        self.massa_molar = massa_molar
        self.entalpia_formacao = entalpia_formacao
        self.entalpia_t_referencia = entalpia_t_referencia
        self.mols_c = mols_c
        self.mols_o = mols_o
        self.mols_h = mols_h
        self.mols_n = mols_n
        self.temperatura = temperatura_referencia

    def __repr__(self):
        return self.composicao

"""
Dados obtidos de:
NASA Glenn coefficients for calculating thermodynamic properties of individual species.
GORDON, S.; MCBRIDE, B. J.; ZEHE M. J.
Glenn Research Center, 2002.

Apendice B, Tabela B3
Apendice D (para entalpia_formacao)
"""

# OXIDANTES
O2_L = Propelente(
    tipo="Oxidante",
    nome="Oxigênio Líquido",
    composicao="O2",
    estado="Líquido",
    massa_molar = 31.99880,
    entalpia_formacao= 0,
    entalpia_t_referencia= -12979,
    mols_c = 0,
    mols_o = 2,
    mols_h = 0,
    mols_n = 0,
    temperatura_referencia = 90.17
)
Air_G = Propelente(
    tipo ="Oxidante",
    nome = "Ar",
    composicao = "(O2+3,76N2)",
    estado = "Gás",
    massa_molar = 28.96518,
    entalpia_formacao = -125.53,
    entalpia_t_referencia = -126,
    mols_c = 0,
    mols_o = 2,
    mols_h = 0,
    mols_n = 7.52,
    temperatura_referencia = 298.15
)
H2O2_L = Propelente(
    tipo = "Oxidante",
    nome = "Peroxido de Hidrogênio",
    composicao = "H2O2",
    estado = "Líquido",
    massa_molar = 34.01468,
    entalpia_formacao = -187780,
    entalpia_t_referencia = -187780,
    mols_c = 0,
    mols_o = 2,
    mols_h = 2,
    mols_n = 0,
    temperatura_referencia = 298.15
)
HNO3_L = Propelente(
    tipo = "Oxidante",
    nome = "Ácido Nítrico",
    composicao = "HNO3",
    estado = "Líquido",
    massa_molar = 63.01288,
    entalpia_formacao = -173013,
    entalpia_t_referencia = -173013,
    mols_c = 0,
    mols_o = 3,
    mols_h = 1,
    mols_n = 1,
    temperatura_referencia = 298.15
)
 
# COMBUSTÍVEIS
C2H5OH_L = Propelente(
    tipo = "Combustível",
    nome = "Etanol",
    composicao = "C2H5OH",
    estado = "Líquido",
    massa_molar = 46.06844,
    entalpia_formacao = -277510.000,
    entalpia_t_referencia = -277510,
    mols_c = 2,
    mols_o = 1,
    mols_h = 6,
    mols_n = 0,
    temperatura_referencia = 298.15
)
H2_L = Propelente(
    tipo = "Combustível", 
    nome = "Hidrogênio",
    composicao = "H2", 
    estado = "Líquido",
    massa_molar = 2.01588,
    entalpia_formacao = 0,
    entalpia_t_referencia =  -9012,
    mols_c = 0,
    mols_o = 0,
    mols_h = 2,
    mols_n = 0,
    temperatura_referencia = 20.27
)
C8H18_L = Propelente(
    tipo = "Combustível",
    nome = "Gasolina",
    composicao = "C8H18",
    estado = "Líquido",
    massa_molar = 114.22852,
    entalpia_formacao = -250260.000,
    entalpia_t_referencia = -250260,
    mols_c = 8,
    mols_o = 0,
    mols_h = 18,
    mols_n = 0,
    temperatura_referencia = 298.15
)
C3H8_L = Propelente(
    tipo = "Combustível",
    nome = "Propano",
    composicao = "C3H8",
    estado = "Líquido",
    massa_molar = 44.09562,
    entalpia_formacao = -104680,
    entalpia_t_referencia = -128228,
    mols_c = 3,
    mols_o =  0,
    mols_h = 8,
    mols_n = 0,
    temperatura_referencia = 231.08
)
C2H8N2_L = Propelente(
    tipo = "Combustível",
    nome = "Dimetil-hidrazina Assimétrica",
    composicao = "C2H8N2",
    estado = "Líquido",
    massa_molar = 60.09840,
    entalpia_formacao = 48900.000,
    entalpia_t_referencia = 48900,
    mols_c = 2,
    mols_o = 0,
    mols_h = 8,
    mols_n = 2,
    temperatura_referencia = 298.15
)
NH3_L = Propelente(
    tipo = "Combustível",
    nome = "Amônia",
    composicao = "NH3",
    estado = "Líquido",
    massa_molar = 17.03056,
    entalpia_formacao = -45940,
    entalpia_t_referencia = -71555,
    mols_c = 0,
    mols_o= 0,
    mols_h = 3,
    mols_n = 1,
    temperatura_referencia = 239.72
)


