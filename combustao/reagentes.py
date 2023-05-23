class Propelente:
    """
    Classe que cria um Propelente, Combustível ou Oxidante
    massa_molar: [kg/kmol] | entalpia_formacao: [kJ/kmol] | temperatura: [K] |
    """
    def __init__(self, tipo, nome, composicao, estado, massa_molar, entalpia_formacao, mols_c, mols_o, mols_h, mols_n, temperatura):
        self.tipo = tipo
        self.nome = nome
        self.composicao = composicao
        self.estado = estado
        self.massa_molar = massa_molar
        self.entalpia_formcao = entalpia_formacao
        self.mols_c = mols_c
        self.mols_o = mols_o
        self.mols_h = mols_h
        self.mols_n = mols_n
        self.temperatura = temperatura

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
o2_L = Propelente("Oxidante", "Oxigênio Líquido", "O2", "Líquido",31.99880, 0, 0, 2, 0, 0, 90.17)
ar_G = Propelente("Oxidante", "Ar", "(O2+3,76N2)", "Gás",28.96518, -125.53, 0, 2, 0, 7.52, 298.15)
h2o2_L = Propelente("Oxidante", "Peroxido de Hidrogênio", "H2O2", "Líquido",34.01468, -187780, 0, 2, 2, 0, 298.15)
hno3_L = Propelente("Oxidante", "Ácido Nítrico", "HNO3", "Líquido", 63.01288, -173013, 0, 3, 1, 1, 298.15)

# COMBUSTÍVEIS
c2h5oh_L = Propelente("Combustível", "Etanol", "C2H5OH", "Líquido", 46.06844, -277510.000, 2, 1, 6, 0, 298.15)
h2_L = Propelente("Combustível", "Hidrogênio", "H2", "Líquido", 2.01588, -9012.000, 0, 0, 2, 0, 20.27)
c8h18_L = Propelente("Combustível", "Gasolina", "C8H18", "Líquido", 114.22852, -250260.000, 8, 0, 18, 0, 298.15)
c3h8_L = Propelente("Combustível", "Propano", "C3H8", "Líquido", 44.09562, -128228.000, 3, 0, 8, 0, 231.08)
c2h8n2_L = Propelente("Combustível", "Dimetil-hidrazina Assimétrica", "C2H8N2", "Líquido", 60.09840, 48900.000, 2, 0, 8, 2, 298.15)
nh3_L = Propelente("Combustível", "Amônia", "NH3", "Líquido", 17.03056, -71555.000, 0, 0, 3, 1, 239.72)


