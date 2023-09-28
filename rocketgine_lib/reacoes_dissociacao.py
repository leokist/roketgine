from .produtos import *


class ReacaoDissociacao():
    """
    Classe que forma uma Reação de Dissociação \n
    n A + n B --> n C + n D \n
    Executa o cálculo de kp, e determina se uma reçaõa pode ou não ocorrer
    """
    def __init__(self, mols_a, reagente_a, mols_b, reagente_b, mols_c, produto_c, mols_d, produto_d):
        self.mols_a = mols_a
        self.reagente_a = reagente_a
        self.mols_b = mols_b
        self.reagente_b = reagente_b
        self.mols_c = mols_c
        self.produto_c = produto_c
        self.mols_d = mols_d
        self.produto_d = produto_d

    def reacao(self):
        reacao = ""
        if self.reagente_a != "none" and self.mols_a != "none":
            reacao += str(self.mols_a) + " " +  self.reagente_a.composicao
        if self.reagente_a != "none" and self.reagente_b != "none":
            reacao += " + "
        if self.reagente_b != "none" and self.mols_b != "none":
            reacao += str(self.mols_b) + " " +  self.reagente_b.composicao
        reacao += " --> "
        if self.produto_c != "none" and self.mols_c != "none":
            reacao += str(self.mols_c) + " " +  self.produto_c.composicao
        if self.produto_c != "none" and self.produto_d != "none":
            reacao += " + "
        if self.produto_d != "none" and self.mols_d != "none":
            reacao += str(self.mols_d) + " " +  self.produto_d.composicao
        return reacao

    def kp(self, temperatura):
        self.temp = temperatura
        """
        kp > 1000 : reação avança até a conclusão
        kp < 0,001 : reação não ocorre de forma alguma
        ou
        ln_kp > 7 : reação avança até a conclusão
        lm_kp < -7 : reação não ocorre de forma alguma
        """
        if self.reagente_a != "none" and self.mols_a != "none":
            gibbs_a = self.reagente_a.funcao_gibbs(self.temp)
        else:
            gibbs_a = 0
        if self.reagente_b != "none" and self.mols_b != "none":
            gibbs_b = self.reagente_b.funcao_gibbs(self.temp)
        else:
            gibbs_b = 0
        if self.produto_c != "none" and self.mols_c != "none":
            gibbs_c = self.produto_c.funcao_gibbs(self.temp)
        else:
            gibbs_c = 0
        if self.produto_d != "none" and self.mols_d != "none":
            gibbs_d = self.produto_d.funcao_gibbs(self.temp)
        else:
            gibbs_d = 0

        ln_kp = (-((self.mols_c*gibbs_c + self.mols_d*gibbs_d) - (self.mols_a*gibbs_a + self.mols_b*gibbs_b))/(Constantes.const_univ_gases()*self.temp))
        kp = e**ln_kp
        #kp = ln_kp
        #if kp < 0.001:
        #    kp = 0.0001
        return kp

# 2CO2 --> 2CO + O2
reacao_2CO2_para_2CO_O2 = ReacaoDissociacao(
    mols_a = 2,
    reagente_a = CO2,
    mols_b = 0,
    reagente_b = "none",
    mols_c = 2,
    produto_c = CO,
    mols_d = 1,
    produto_d = O2,
)

# CO2 --> CO + O
reacao_CO2_para_CO_O = ReacaoDissociacao(
    mols_a = 1,
    reagente_a = CO2,
    mols_b = 0,
    reagente_b = "none",
    mols_c = 1,
    produto_c = CO,
    mols_d = 1,
    produto_d = O,
)

# H2O --> H + OH
reacao_H2O_para_H_OH = ReacaoDissociacao(
    mols_a = 1,
    reagente_a = H2O,
    mols_b = 0,
    reagente_b = "none",
    mols_c = 1,
    produto_c = H,
    mols_d = 1,
    produto_d = OH,
)

# H2O --> OH + O
reacao_H2O_para_OH_O = ReacaoDissociacao(
    mols_a = 1,
    reagente_a = H2O,
    mols_b = 0,
    reagente_b = "none",
    mols_c = 1,
    produto_c = OH,
    mols_d = 1,
    produto_d = O,
)

# H2O --> H2 + 0,5O2
reacao_H2O_para_H2_05O2 = ReacaoDissociacao(
    mols_a = 1,
    reagente_a = H2O,
    mols_b = 0,
    reagente_b = "none",
    mols_c = 1,
    produto_c = H2,
    mols_d = 0.5,
    produto_d = O2,
)

# H2O --> 2H + O
reacao_H2O_para_2H_O = ReacaoDissociacao(
    mols_a = 1,
    reagente_a = H2O,
    mols_b = 0,
    reagente_b = "none",
    mols_c = 2,
    produto_c = H2,
    mols_d = 1,
    produto_d = O,
)

# 2H2O --> 2H2 + O2
reacao_2H2O_para_2H2_O2 = ReacaoDissociacao(
    mols_a = 2,
    reagente_a = H2O,
    mols_b = 0,
    reagente_b = "none",
    mols_c = 2,
    produto_c = H2,
    mols_d = 1,
    produto_d = O2,
)

# 2H2O --> H2 + 2OH
reacao_2H2O_para_H2_2OH = ReacaoDissociacao(
    mols_a = 2,
    reagente_a = H2O,
    mols_b = 0,
    reagente_b = "none",
    mols_c = 1,
    produto_c = H2,
    mols_d = 2,
    produto_d = OH,
)

# OH --> H + O
reacao_OH_para_H_O = ReacaoDissociacao(
    mols_a = 1,
    reagente_a = OH,
    mols_b = 0,
    reagente_b = "none",
    mols_c = 1,
    produto_c = H,
    mols_d = 1,
    produto_d = O,
)

# H2 --> 2H
reacao_H2_para_2H = ReacaoDissociacao(
    mols_a = 1,
    reagente_a = H2,
    mols_b = 0,
    reagente_b = "none",
    mols_c = 2,
    produto_c = H,
    mols_d = 0,
    produto_d = "none",
)

# O2 --> 2O
reacao_O2_para_2O = ReacaoDissociacao(
    mols_a = 1,
    reagente_a = O2,
    mols_b = 0,
    reagente_b = "none",
    mols_c = 2,
    produto_c = O,
    mols_d = 0,
    produto_d = "none",
)

# N2 --> 2N
reacao_N2_para_2N = ReacaoDissociacao(
    mols_a = 1,
    reagente_a = N2,
    mols_b = 0,
    reagente_b = "none",
    mols_c = 2,
    produto_c = N,
    mols_d = 0,
    produto_d = "none",
)


