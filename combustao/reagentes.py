class Propelente:
    def __init__(self, tipo, nome, composicao, massa_molar, entalpia_formacao, mols_c, mols_o, mols_h, mols_n):
        self.tipo = tipo
        self.nome = nome
        self.composicao = composicao
        self.massa_molar = massa_molar
        self.entalpia_formcao = entalpia_formacao
        self.mols_c = mols_c
        self.mols_o = mols_o
        self.mols_h = mols_h
        self.mols_n = mols_n

    def __repr__(self):
        return self.composicao

o2_L = Propelente("Oxidante", "Oxigênio Líquido", "O2", 31.99880, -12979, 0, 2, 0, 0)
ar_G = Propelente("Oxidante", "Ar", "(O2+3,76N2)", 28.9651159, -125.53, 0, 2, 0, 7.52)
h2o2_L = Propelente("Oxidante", "Peroxido de Hidrogênio", "H2O2", 0, 0, 0, 2, 2, 0)
hno3_L = Propelente("Oxidante", "Ácido Nítrico", "HNO3", 0, 0, 0, 3, 1, 1)
#f_L = Propelente("Oxidante", "Flúor", "F", 0, 0, mols_c, mols_o, mols_h, mols_n)

c2h5oh_L = Propelente("Combustível", "Etanol", "C2H5OH", 46.06844, -277510, 2, 1, 6, 0)
h2_L = Propelente("Combustível", "Hidrogênio", "H2", 15, -100000, 0, 0, 2, 0)
c8h18_L = Propelente("Combustível", "Gasolina", "C8H18", 114.22852, -250260, 8, 0, 18, 0)
c3h8_L = Propelente("Combustível", "Propano", "C3H8", 0, 0, 3, 0, 8, 0)
c2h8n2_L = Propelente("Combustível", "Dimetil-hidrazina Assimétrica", "C2H8N2", 0, 0, 2, 0, 8, 2)
c42h72o14_L = Propelente("Combustível", "RG1 - Ginsenosido", "C42H72O14", 0, 0, 42, 14, 72, 0)
nh3_L = Propelente("Combustível", "Amônia", "NH3", 0, 0, 0, 0, 3, 1)
cho_teste = Propelente("Combustível", "Teste", "Teste", 114.22852, -250260, 21.7262, 41.4525, 43.4525, 0)

