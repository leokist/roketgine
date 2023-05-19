"a*COMB + b+OXID ---> c*H2O + d*CO2 + e*N2 + f*CO + g*H2 + h*O2 + i*OH + j*O + k*H"

from .produtos import *
from .constantes import *

class Combustao():
    """Define os reagentes da combustão"""
    def __init__(self, comb, oxid):
        self.comb = comb
        self.oxid = oxid
        self.propelentes = [comb, oxid]

    """
             b                      c             d                      a
    [self.oxid.mols_o, - prod1.mols_o, - prod2.mols_o, - self.comb.mols_o],
    [self.oxid.mols_h, - prod1.mols_h, - prod2.mols_h, - self.comb.mols_h],
    [self.oxid.mols_c, - prod1.mols_c, - prod2.mols_c, - self.comb.mols_c],
    """
    def reacao_combustao(self, razao_equiv=1):
        """
        Executa o cálculo da reação de combustão a uma determinada tazão de mistura.
        Se nada for informado, será considerado uma reação estequiométrica, com razão de mistura igual a 1.
        """
        self.razao_equiv = razao_equiv
        self.produtos_estequiometrico = []
        self.produtos_dissociacao = []
        self.matriz_estequiometrica = []
      
        # Define os produtos de uma reação estequiométrica
        "a*COMB + b+OXID ---> c*H2O + d*CO2 + e*N2"
        if razao_equiv != 0 and (self.comb.mols_o > 0 or self.oxid.mols_o > 0) and (self.comb.mols_h > 0 or self.oxid.mols_h > 0):
            self.produtos_estequiometrico.append(h2o)
        if razao_equiv != 0 and (self.comb.mols_c > 0 or self.oxid.mols_c > 0) and (self.comb.mols_o > 0 or self.oxid.mols_o > 0):
            self.produtos_estequiometrico.append(co2)
        if razao_equiv != 0 and (self.comb.mols_n > 0 or self.oxid.mols_n > 0):
            self.produtos_estequiometrico.append(n2)
              
        print(self.produtos_estequiometrico)

        # Obtém a quantidade total de produtos da reação
        n_produtos = len(self.produtos_estequiometrico)

        # Obtem a quantidade total de reagentes da reação
        n_propelentes = len(self.propelentes)

        # Obtém a quantidade total de elementos
        if self.comb.mols_o != 0 or self.oxid.mols_o != 0:
            n_elementos = 1
        if self.comb.mols_h != 0 or self.oxid.mols_h != 0:
            n_elementos += 1
        if self.comb.mols_c != 0 or self.oxid.mols_c != 0:
            n_elementos += 1
        if self.comb.mols_n != 0 or self.oxid.mols_n != 0:
            n_elementos += 1
            
        # Gera uma matriz de template com as linhas necessárias
        
        matriz = [] #self.matriz
        lin = 0
        while lin < n_elementos:
            matriz.append([])
            lin += 1

        # Adiciona o numero de mols de cada espécie na matriz
        n_especies = n_produtos + n_propelentes
        lin = 0
        col = 0
        while lin < n_elementos:
            while col != (n_especies - 1):
                if lin == 0:
                    if col == 0:
                        matriz[lin].insert(col,self.propelentes[1].mols_o)
                    if col != 0:
                        matriz[lin].insert(col, -1 * self.produtos_estequiometrico[col-1].mols_o)
                    if col == (n_produtos - 1):
                        matriz[lin].insert(col+1, -1 * self.propelentes[0].mols_o)
                elif lin == 1:
                    if col == 0:
                        matriz[lin].insert(col,self.propelentes[1].mols_h)
                    if col != 0:
                        matriz[lin].insert(col, -1 * self.produtos_estequiometrico[col-1].mols_h)
                    if col == (n_produtos - 1):
                        matriz[lin].insert(col+1, -1 * self.propelentes[0].mols_h)
                elif lin == 2:
                    if col == 0:
                        matriz[lin].insert(col,self.propelentes[1].mols_c)
                    if col != 0:
                        matriz[lin].insert(col, -1 * self.produtos_estequiometrico[col-1].mols_c)
                    if col == (n_produtos - 1):
                        matriz[lin].insert(col+1, -1 * self.propelentes[0].mols_c)
                elif lin == 3:
                    if col == 0:
                        matriz[lin].insert(col,self.propelentes[1].mols_n)
                    if col != 0:
                        matriz[lin].insert(col, -1 * self.produtos_estequiometrico[col-1].mols_n)
                    if col == (n_produtos - 1):
                        matriz[lin].insert(col+1, - 1 * self.propelentes[0].mols_n)
                col += 1
            col = 0
            lin += 1

        """
        # Cálculo do numero de mol de cada produto e reagente
        # Cálculo efetuado pelo método de Eliminação de Gauss
        """
        # Zera os elementos abaixo da diagonal da matriz
        col = 0
        pivo_x = 0
        lin = pivo_x + 1
        while lin < n_elementos:
            if matriz[lin][col] == 0:
                lin += 1
            else:
                pivo = matriz[pivo_x][pivo_x]
                multp = matriz[lin][col] / pivo
                x = 0
                for i in matriz[lin]:                  
                    matriz[lin][x] = i - multp * matriz[pivo_x][x]
                    x += 1
                lin += 1
            if lin == len(matriz):
                pivo_x += 1
                lin = pivo_x + 1
                col += 1
            
        # Zera os elementos acima da diagonal da matriz
        pivo_x = n_elementos - 1
        col = pivo_x
        lin = pivo_x - 1
        while lin >= 0:
            if matriz[lin][col] == 0:
                lin -= 1
            else:
                pivo = matriz[pivo_x][pivo_x]
                multp = matriz[lin][col] / pivo
                x = 0
                for i in matriz[lin]:
                    matriz[lin][x] = i - multp * matriz[pivo_x][x]
                    x += 1
                lin -= 1
            if lin == -1:
                pivo_x -= 1
                col = pivo_x
                lin = pivo_x - 1
        
        # Obtem a solução
        pivo_x = 0
        lin = 0
        col = 0
        while lin < n_elementos:
            pivo = matriz[lin][col]
            x = 0
            for i in matriz[lin]:
                matriz[lin][x] = matriz[lin][x] / pivo
                x += 1
            lin += 1
            col += 1

        self.matriz_estequiometrica = matriz
        razao_mistura_estequiometrica = (self.matriz_estequiometrica[0][-1]*self.oxid.massa_molar)/(1*self.comb.massa_molar)
        razao_mistura = razao_mistura_estequiometrica / self.razao_equiv
        print(f"rme: {razao_mistura_estequiometrica}")
        print(f"rm: {razao_mistura}")

        """
        CÁLCULO DA REAÇÃO DE COMBUSTÃO COM DISSOCIAÇÃO
        """
        if razao_equiv != 1:
            temp_adiab = 3234.87
            # Número de mols dos Propelentes
            n_comb = (self.matriz_estequiometrica[0][-1] * self.oxid.massa_molar) / (razao_mistura * self.comb.massa_molar)
            n_oxid = self.matriz_estequiometrica[0][-1]
            print(f"n_comb: {n_comb}")
            print(f"n_oxid: {n_oxid}")

            # Número de mols dos elementos
            if self.comb.mols_c > 0 or self.oxid.mols_c > 0:
                n_c = n_comb*self.comb.mols_c + n_oxid*self.oxid.mols_c
                n_total = n_c
                print(f"Nc:{n_c}")
            if self.comb.mols_o > 0 or self.oxid.mols_o > 0:
                n_o = n_comb*self.comb.mols_o + n_oxid*self.oxid.mols_o
                n_total += n_o
                print(f"No:{n_o}")
            if self.comb.mols_h > 0 or self.oxid.mols_h > 0:
                n_h = n_comb*self.comb.mols_h + n_oxid*self.oxid.mols_h
                n_total += n_h
                print(f"Nh:{n_h}")
            if self.comb.mols_n > 0 or self.oxid.mols_n > 0:
                n_n = n_comb*self.comb.mols_n + n_oxid*self.oxid.mols_n
                n_total += n_n
                print(f"Nn:{n_n}")
            print(f"Nc:{n_c/n_total} No:{n_o/n_total} Nh:{n_h/n_total}")

            # Define os produtos de uma reação com dissociação
            "a*COMB + b+OXID ---> c*CO2 + d*CO + e*H2O + f*OH + g*H2 + h*H + i*O2 + j*O + k*N2 + l*N"
            if (self.comb.mols_c > 0 or self.oxid.mols_c > 0) and (self.comb.mols_o > 0 or self.oxid.mols_o > 0):
                self.produtos_dissociacao.append(co2)
                self.produtos_dissociacao.append(co)
            if (self.comb.mols_o > 0 or self.oxid.mols_o > 0) and (self.comb.mols_h > 0 or self.oxid.mols_h > 0):
                self.produtos_dissociacao.append(h2o)
                self.produtos_dissociacao.append(oh)
            if (self.comb.mols_h > 0 or self.oxid.mols_h > 0):
                self.produtos_dissociacao.append(h2)
                self.produtos_dissociacao.append(h)
            if (self.comb.mols_o > 0 or self.oxid.mols_o > 0):
                self.produtos_dissociacao.append(o2)
                self.produtos_dissociacao.append(o)
            if (self.comb.mols_n > 0 or self.oxid.mols_n > 0):
                self.produtos_dissociacao.append(n2)
                self.produtos_dissociacao.append(n)

            # Calcula as funções de gibbs
            if (self.comb.mols_c > 0 or self.oxid.mols_c > 0) and (self.comb.mols_o > 0 or self.oxid.mols_o > 0):
                gibbs_co2 = co2.funcao_gibbs(temp_adiab)
                gibbs_co = co.funcao_gibbs(temp_adiab)
            if (self.comb.mols_o > 0 or self.oxid.mols_o > 0) and (self.comb.mols_h > 0 or self.oxid.mols_h > 0):
                gibbs_h2o = h2o.funcao_gibbs(temp_adiab)
                gibbs_oh = oh.funcao_gibbs(temp_adiab)
            if (self.comb.mols_h > 0 or self.oxid.mols_h > 0):
                gibbs_h2 = h2.funcao_gibbs(temp_adiab)
                gibbs_h = h.funcao_gibbs(temp_adiab)
            if (self.comb.mols_o > 0 or self.oxid.mols_o > 0):
                gibbs_o2 = o2.funcao_gibbs(temp_adiab)
                gibbs_o = o.funcao_gibbs(temp_adiab)
            if (self.comb.mols_n > 0 or self.oxid.mols_n > 0):
                gibbs_n2 = n2.funcao_gibbs(temp_adiab)
                gibbs_n = n.funcao_gibbs(temp_adiab)

            # Calcula as constantes de dissociação
            if (self.comb.mols_o > 0 or self.oxid.mols_o > 0) and (self.comb.mols_c > 0 or self.oxid.mols_c > 0):
                # CO2 --> CO + O
                kp1 = e**(-(1*gibbs_co + 1*gibbs_o - 1*gibbs_co2)/(Constantes.const_univ_gases()*temp_adiab))
                print(f"kp1: {kp1}")
                if kp1 < 0.001:
                    print(f"kp1={kp1}<0.001, a dissociação CO2 --> CO + O não irá ocorrer a esta temperatura")
            if (self.comb.mols_o > 0 or self.oxid.mols_o > 0) and (self.comb.mols_h > 0 or self.oxid.mols_h > 0):
                # H2O --> 2H + O
                kp2 = e**(-(2*gibbs_h + 1*gibbs_o - 1*gibbs_h2o)/(Constantes.const_univ_gases()*temp_adiab))
                # OH --> H + O
                kp3 = e**(-(1*gibbs_h + 1*gibbs_o - 1*gibbs_oh)/(Constantes.const_univ_gases()*temp_adiab))
                # H2O --> OH + O
                kp7 = e**(-(1*gibbs_oh + 1*gibbs_o - 1*gibbs_h2o)/(Constantes.const_univ_gases()*temp_adiab))
                print(f"kp2: {kp2}")
                print(f"kp3: {kp3}")
                print(f"kp7: {kp7}")
                if kp2 < 0.001:
                    print(f"kp2={kp2}<0.001, a dissociação H2O --> 2H + O não irá ocorrer a esta temperatura")
                if kp3 < 0.001:
                    print(f"kp3={kp3}<0.001, a dissociação OH --> H + O não irá ocorrer a esta temperatura")
                if kp7 < 0.001:
                    print(f"kp7={kp7}<0.001, a dissociação H2O --> OH + O não irá ocorrer a esta temperatura")
            if (self.comb.mols_h > 0 or self.oxid.mols_h > 0):
                # H2 --> 2 H
                kp4 = e**(-(2*gibbs_h - 1*gibbs_h2)/(Constantes.const_univ_gases()*temp_adiab))
                if kp4 < 0.001:
                    print(f"kp4={kp4}<0.001, a dissociação H2 --> 2 H não irá ocorrer a esta temperatura")
                print(f"kp4: {kp4}")
            if (self.comb.mols_o > 0 or self.oxid.mols_o > 0):
                # O2 --> 2 O
                kp5 = e**(-(2*gibbs_o - 1*gibbs_o2)/(Constantes.const_univ_gases()*temp_adiab))
                if kp5 < 0.001:
                    print(f"kp5={kp5}<0.001, a dissociação H2 --> 2 H não irá ocorrer a esta temperatura")
                print(f"kp5: {kp5}")
            if (self.comb.mols_n > 0 or self.oxid.mols_n > 0):
                # N2 --> 2 N 
                kp6 = e**(-(2*gibbs_n - 1*gibbs_n2)/(Constantes.const_univ_gases()*temp_adiab))
                if kp6 < 0.001:
                    print(f"kp1={kp6}<0.001, a dissociação H2 --> 2 H não irá ocorrer a esta temperatura")
                print(f"kp6: {kp6}")
            
            
            y = 0.4422
            p = 15
            n_total = p/y
            n_total_calc = n_total*2
            N_o2 = 0.75
            N_o2_sup = 1
            N_o2_inf = 0
            n_o_calc = 0.1
            # print(erro)
            i=0
            erro_anterior = 99
            N_o2_anterior = "?"
            tentativa = 1
            while i < 30:
                
                N_o = (kp5*N_o2/y)**0.5

                if self.comb.mols_c > 0 or self.oxid.mols_c > 0:
                    N_co2 = (n_c*kp5)/((kp1*N_o)+kp5)
                    N_co = n_c-N_co2
                else:
                    N_co = 0
                    N_co2 = 0

                N_h2o = (n_o-(2*N_co2)-N_co-(2*N_o2)-N_o)/(((N_o*kp7)/(N_o2*kp5))+1)
                N_oh = n_o-N_h2o-2*N_co2-N_co-2*N_o2-N_o
                N_h = (N_o*N_oh*kp3)/(N_o2*kp5)
                N_h2 = (n_h-2*N_h2o-N_oh-N_h)/2

                if self.comb.mols_n > 0 or self.oxid.mols_n > 0:
                    N_n_a = (2*N_o2*kp5)/(kp6*N_o**2)
                    N_n_b = 1
                    N_n_c = -n_n
                    N_n = (-N_n_b+((N_n_b**2 - 4*N_n_a*N_n_c)**0.5))/(2*N_n_a)

                    N_n2 = ((N_o2*kp5)/(kp6*N_o**2))*N_n**2
                else:
                    N_n = 0
                    N_n2 = 0

                n_total_calc = N_o2+N_o+N_co2+N_co+N_h+N_h2+N_oh+N_h2o+N_n+N_n2
                n_o_calc = 2*N_o2+N_o+2*N_co2+N_co+N_oh+N_h2o
                
                erro = n_o/n_o_calc
                print("tent: {:.2f} No_t:{:.4f}, No_t_c:{:.4f}, er: {:.4f}, No2_inf: {:.3f} No2: {:.3f} No2_sup: {:.3f}".format(tentativa, n_o, n_o_calc, erro, N_o2_inf, N_o2, N_o2_sup))            
                if tentativa == 1:
                    erro_1 = erro
                    erro_2 = 0
                    N_o2_anterior = N_o2
                    if N_o2 == 0.75:
                        N_o2 = 0.25
                    else:
                        N_o2 = N_o2_inf+((N_o2_sup-N_o2_inf)/4)
                    tentativa+=1
                elif tentativa == 2:
                    erro_2 = erro
                    if erro_1 < erro_2:
                        N_o2_sup = N_o2_sup
                        N_o2_inf = (N_o2_anterior+N_o2)/2
                        N_o2 = N_o2_sup-((N_o2_sup-N_o2_inf)/4)
                        tentativa = 1
                    else:
                        N_o2_sup = (N_o2_sup+N_o2_inf)/2
                        N_o2_inf = N_o2_inf
                        N_o2 = N_o2_sup-((N_o2_sup-N_o2_inf)/4)
                        tentativa = 1
                i+=1
                
                
                #print(f"n:{n_total}, N:{n_total_calc}, {(erro)}")
                #print(f"o2: {N_o2/N_total}, o: {N_o/N_total}, co2: {N_co2/N_total}, co: {N_co/N_total}, h: {N_h/N_total}, h2: {N_h2/N_total}, oh: {N_oh/N_total}, h2o: {N_h2o/N_total}, n: {N_n/N_total}, n2: {N_n2/N_total} razao_mist: {razao_mistura}")
            print(f"o2: {N_o2/n_total_calc}, o: {N_o/n_total_calc}, co2: {N_co2/n_total_calc}, co: {N_co/n_total_calc}, h: {N_h/n_total_calc}, h2: {N_h2/n_total_calc}, oh: {N_oh/n_total_calc}, h2o: {N_h2o/n_total_calc}, n: {N_n/n_total_calc}, n2: {N_n2/n_total_calc} razao_mist: {razao_mistura}")
                
                #print(f"RME: {razao_mistura_estequiometrica}")
                #print(f"RE: {razao_equiv}")
                #print(f"RE: {razao_mistura}")
            
    @property
    def reacao_combustao_resultado(self):
        """Exibe o resultado da reação de combustão com o número de mols de cada elemento"""
        a = 1
        matriz = self.matriz_estequiometrica

        reacao = f"{a} {self.propelentes[0]} + {matriz[0][-1]} {self.propelentes[1]} -->"

        x = 0
        for i in self.produtos_estequiometrico:
            reacao += f" {matriz[x+1][-1]} {i}"
            if i is not self.produtos_estequiometrico[-1]:
                reacao += " + "
            x += 1
        return reacao

    @property
    def a(self):
        """Retorna o número de mols do Combustível"""
        a = 1.0
        return a

    @property
    def b(self):
        """Retorna o número de mols do oxid"""
        l=len(self.matriz)
        b = self.matriz[0][l]
        return b
    
    @property
    def c(self):
        """Retorna o número de mols do produto da combustão"""
        l=len(self.matriz)
        c = self.matriz[1][l]
        return c
    
    @property
    def d(self):
        """Retorna o número de mols do produto da combustão"""
        l=len(self.matriz)
        if l >= 3:
            d = self.matriz[2][l]
        else:
            d = "Elemento inexistente"
        return d
    
    @property
    def e(self):
        """Retorna o número de mols do produto da combustão"""
        l=len(self.matriz)
        if l >= 4:
            e = self.matriz[3][l]
        else:
            e = "Elemento inexistente"
        return e

    #@property
    #def razao_mistura_estequiometrica(self):
    #    return razao_mistura_estequiometrica

    #@property
    #def razao_mistura(self):
    #    return razao_mistura

    #@property
    #def razao_equivalencia(self):
    #    return self.razao_equivalencia
