"a*COMB + b+OXID ---> c*H2O + d*CO2 + e*N2 + f*CO + g*H2 + h*O2 + i*OH + j*O + k*H"

from .produtos import *
from .constantes import *
from .reacoes_dissociacao import *

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
    def reacao_estequiometrica(self):
        """
        Executa o cálculo da reação de combustão estequiométrica.
        """
        self.razao_equiv = 1
        self.produtos_estequiometrico = []
        self.produtos_dissociacao = []
        self.matriz_estequiometrica = []
        self.n_comb = 1
                
        # Define os produtos de uma reação estequiométrica
        "a*COMB + b+OXID ---> c*H2O + d*CO2 + e*N2"
        if self.razao_equiv != 0 and (self.comb.mols_o > 0 or self.oxid.mols_o > 0) and (self.comb.mols_h > 0 or self.oxid.mols_h > 0):
            self.produtos_estequiometrico.append([H2O, 0])
        if self.razao_equiv != 0 and (self.comb.mols_c > 0 or self.oxid.mols_c > 0) and (self.comb.mols_o > 0 or self.oxid.mols_o > 0):
            self.produtos_estequiometrico.append([CO2, 0])
        if self.razao_equiv != 0 and (self.comb.mols_n > 0 or self.oxid.mols_n > 0):
            self.produtos_estequiometrico.append([N2, 0])
                
        print("Prod Esteq: ", self.produtos_estequiometrico)
        print("Item: ", self.produtos_estequiometrico[0][0])

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
        contador = 0
        while lin < n_elementos:
            if contador == 0:
                if self.comb.mols_o == 0 and self.oxid.mols_o == 0:
                    lin = 0
                else:
                    while col != (n_especies - 1):
                        if col == 0:
                            matriz[lin].insert(col,self.propelentes[1].mols_o)
                        if col != 0:
                            matriz[lin].insert(col, -1 * self.produtos_estequiometrico[col-1][0].mols_o)
                        if col == (n_produtos - 1):
                            matriz[lin].insert(col+1, -1 * self.propelentes[0].mols_o)
                        col += 1
                    lin += 1
                    col = 0
            elif contador == 1:
                if self.comb.mols_h == 0 and self.oxid.mols_h == 0:
                    lin = 1
                else:
                    while col != (n_especies - 1):
                        if col == 0:
                            matriz[lin].insert(col,self.propelentes[1].mols_h)
                        if col != 0:
                            matriz[lin].insert(col, -1 * self.produtos_estequiometrico[col-1][0].mols_h)
                        if col == (n_produtos - 1):
                            matriz[lin].insert(col+1, -1 * self.propelentes[0].mols_h)
                        col += 1 
                    lin += 1
                    col = 0
            elif contador == 2:
                if self.comb.mols_c == 0 and self.oxid.mols_c == 0:
                    lin = 2
                else:
                    while col != (n_especies - 1):
                        if col == 0:
                            matriz[lin].insert(col,self.propelentes[1].mols_c)
                        if col != 0:
                            matriz[lin].insert(col, -1 * self.produtos_estequiometrico[col-1][0].mols_c)
                        if col == (n_produtos - 1):
                            matriz[lin].insert(col+1, -1 * self.propelentes[0].mols_c)
                        col += 1 
                    lin += 1
                    col = 0
            elif contador == 3:
                if self.comb.mols_n != 0 or self.oxid.mols_n != 0:
                    while col != (n_especies - 1):
                        if col == 0:
                            matriz[lin].insert(col,self.propelentes[1].mols_n)
                        if col != 0:
                            matriz[lin].insert(col, -1 * self.produtos_estequiometrico[col-1][0].mols_n)
                        if col == (n_produtos - 1):
                            matriz[lin].insert(col+1, - 1 * self.propelentes[0].mols_n)
                        col += 1
                    lin += 1
                    col = 0
            contador += 1

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
        y = 0
        while lin < n_elementos:
            pivo = matriz[lin][col]
            x = 0
            for i in matriz[lin]:
                matriz[lin][x] = matriz[lin][x] / pivo
                x += 1
            lin += 1
            col += 1

        # Mapeamento dos resultados
        y = 0
        print(matriz)
        while y < len(matriz)-1:
            self.produtos_estequiometrico[y][1] = matriz[y+1][len(matriz)]
            y += 1
            lin += 1
        print(self.produtos_estequiometrico)

        self.n_oxid = matriz[0][-1]
                                  
        self.razao_mistura_estequiometrica = (self.n_oxid*self.oxid.massa_molar)/(self.n_comb*self.comb.massa_molar)
        

    def temp_adiabatica(self, tipo="estequiometrico"):
        """
        Temperatura adiabática de chama
        """

        self.tipo = tipo

        if self.tipo == "estequiometrico" and self.razao_equiv == 1:
            produtos = self.produtos_estequiometrico
        elif self.tipo == "dissociacao":
            produtos = self.produtos_dissociacao

        # CALCULO ENTALPIA DOS REAGENTES
        # Como a temperatura do reagente utilizada para o cálculo da combustão
        # será igual a temperatura de referência, teremos:
        # Hr = n_comb (hf + h - h(ref)) + n_oxid (hf + h - h(ref))
        # Hr = n_comb * hf + n_oxid * hf 
        self.entalpia_reagentes = self.n_comb * self.comb.entalpia_formacao + self.n_oxid * self.oxid.entalpia_formacao
        #self.entalpia_reagentes = self.n_comb * (self.comb.entalpia_formacao + self.comb.entalpia(self.comb.temperatura_referencia) - self.comb.entalpia_referencia) + self.n_oxid * (self.oxid.entalpia_formacao + self.oxid.entalpia(self.oxid.temperatura_referencia) - self.oxid.entalpia_referencia)

        #if self.razao_equiv == 1:
        self.entalpia_produtos = 0
        x = 0
        y = 0
        temp_min = 200
        temp_max = 6000
        temp = 3100
        print("iniciando")
        while y < 30:
            while x < len(produtos):
                prod = produtos[x][0]
                prod_mols = produtos[x][1]
                self.entalpia_produtos += prod_mols * (prod.entalpia_formacao + prod.entalpia(temp) - prod.entalpia_t_referencia)
                x += 1
            print(self.entalpia_produtos, self.entalpia_reagentes)
            #erro = 100*((abs(self.entalpia_produtos)-abs(self.entalpia_reagentes))/abs(self.entalpia_reagentes))
            erro = 100*((abs(self.entalpia_reagentes)-abs(self.entalpia_produtos))/abs(self.entalpia_produtos))
            #print("Hr:", self.entalpia_reagentes,"Hp:", self.entalpia_produtos, "Temp_Max:", temp_max,"Temp:", temp, "Temp_Min:", temp_min, "Erro:", erro)
            print("Hr:", self.entalpia_reagentes,"Hp:", self.entalpia_produtos, "Temp:", temp, erro)
            if abs(erro) < 0.001:
                print("------- Cálculo concluído -------")
                print("Hr:", self.entalpia_reagentes,"Hp:", self.entalpia_produtos, "Erro:", erro, "Iterações:", y)
                print("Temperatura Adiabática:", temp)
                break
            elif self.entalpia_reagentes < self.entalpia_produtos:
                temp_max = temp
                temp = ((temp + temp_min) / 2)
                self.entalpia_produtos = 0
            elif self.entalpia_reagentes > self.entalpia_produtos:
                temp_min = temp
                temp = ((temp + temp_max) / 2)
                self.entalpia_produtos = 0
            if y == 29:
                print("não encontrado")
            x = 0
            y += 1
        print("concluido")
        self.temperatura_adiabatica = temp
        return self.temperatura_adiabatica

    def reacao_dissociacao(self, razao_equiv, pressao):
        """
        REACAO COM DISSOCIACAO
        """        
        self.pressao = pressao
        self.razao_equiv = razao_equiv
        self.razao_mistura = self.razao_mistura_estequiometrica / self.razao_equiv
        self.n_comb = (self.n_oxid * self.oxid.massa_molar) / (self.razao_mistura * self.comb.massa_molar)

        print("RME:",self.razao_mistura_estequiometrica,"RM:", self.razao_mistura, "n_comb:", self.n_comb)

        # Define os produtos de uma reação com dissociação
        "a*COMB + b+OXID ---> c*CO2 + d*CO + e*H2O + f*OH + g*H2 + h*H + i*O2 + j*O + k*N2 + l*N"
        if (self.comb.mols_c > 0 or self.oxid.mols_c > 0) and (self.comb.mols_o > 0 or self.oxid.mols_o > 0):
            self.produtos_dissociacao.append([CO2, 0])
            self.produtos_dissociacao.append([CO, 0])
        if (self.comb.mols_o > 0 or self.oxid.mols_o > 0) and (self.comb.mols_h > 0 or self.oxid.mols_h > 0):
            self.produtos_dissociacao.append([H2O, 0])
            self.produtos_dissociacao.append([OH, 0])
        if (self.comb.mols_h > 0 or self.oxid.mols_h > 0):
            self.produtos_dissociacao.append([H2, 0])
            self.produtos_dissociacao.append([H, 0])
        if (self.comb.mols_o > 0 or self.oxid.mols_o > 0):
            self.produtos_dissociacao.append([O2, 0])
            self.produtos_dissociacao.append([O, 0])
        if (self.comb.mols_n > 0 or self.oxid.mols_n > 0):
            self.produtos_dissociacao.append([N2, 0])
            self.produtos_dissociacao.append([N, 0])
    
        n_total = 0
        # Número de mols dos elementos
        if self.comb.mols_c > 0 or self.oxid.mols_c > 0:
            N_C_reagentes = self.n_comb*self.comb.mols_c + self.n_oxid*self.oxid.mols_c
            N_total_reagentes = N_C_reagentes
            #print(f"Nc:{N_C_reagentes}")
        else:
            N_C_reagentes = 0
        if self.comb.mols_o > 0 or self.oxid.mols_o > 0:
            N_O_reagentes = self.n_comb*self.comb.mols_o + self.n_oxid*self.oxid.mols_o
            N_total_reagentes += N_O_reagentes
            #print(f"No:{N_O_reagentes}")
        else:
            N_O_reagentes = 0
        if self.comb.mols_h > 0 or self.oxid.mols_h > 0:
            N_H_reagentes = self.n_comb*self.comb.mols_h + self.n_oxid*self.oxid.mols_h
            N_total_reagentes += N_H_reagentes
            #print(f"Nh:{N_H_reagentes}")
        else:
            N_H_reagentes = 0
        if self.comb.mols_n > 0 or self.oxid.mols_n > 0:
            N_N_reagentes = self.n_comb*self.comb.mols_n + self.n_oxid*self.oxid.mols_n
            N_total_reagentes += N_N_reagentes
            #print(f"Nn:{N_N_reagentes}")
        else:
            N_N_reagentes = 0
        
        # Calcula as constantes de dissociação
        if (self.comb.mols_o > 0 or self.oxid.mols_o > 0) and (self.comb.mols_c > 0 or self.oxid.mols_c > 0):
            # CO2 --> CO + O
            kp1 = reacao_CO2_para_CO_O.kp(self.temperatura_adiabatica)
            print(f"kp1: {kp1}")
        if (self.comb.mols_o > 0 or self.oxid.mols_o > 0) and (self.comb.mols_h > 0 or self.oxid.mols_h > 0):
            # H2O --> 2H + O
            kp2 = reacao_H2O_para_2H_O.kp(self.temperatura_adiabatica)
            # OH --> H + O
            kp3 = reacao_OH_para_H_O.kp(self.temperatura_adiabatica)
            # H2O --> OH + O
            kp7 = reacao_H2O_para_OH_O.kp(self.temperatura_adiabatica)
            print(f"kp2: {kp2}")
            print(f"kp3: {kp3}")
            print(f"kp7: {kp7}")
        if (self.comb.mols_h > 0 or self.oxid.mols_h > 0):
            # H2 --> 2 H
            kp4 = reacao_H2_para_2H.kp(self.temperatura_adiabatica)
            print(f"kp4: {kp4}")
        if (self.comb.mols_o > 0 or self.oxid.mols_o > 0):
            # O2 --> 2 O
            kp5 = reacao_O2_para_2O.kp(self.temperatura_adiabatica)
            print(f"kp5: {kp5}")
        if (self.comb.mols_n > 0 or self.oxid.mols_n > 0):
            # N2 --> 2 N 
            kp6 = reacao_N2_para_2N.kp(self.temperatura_adiabatica)
            print(f"kp6: {kp6}")

        #kp1 = reacao_CO2_para_CO_05O2.kp(self.temperatura_adiabatica)      
        #kp3 = reacao_H2O_para_H2_05O2.kp(self.temperatura_adiabatica)
        
        p = self.pressao
        y = p / N_total_reagentes
        n_O2 = 0.001
        n_CO2 = -1
        n_CO = -1
        n_H2O = -1
        n_OH = -1
        n_O = -1
        n_H2 = -1
        n_H = -1
        n_N2 = -1
        n_N = -1
        iteracoes = 0
        while (n_CO2<0 or n_CO<0 or n_H2O<0 or n_OH<0 or n_O2<0 or n_O<0 or n_H2<0 or n_H<0 or n_N2<0 or n_N<0):
            n_O = (kp5*n_O2/y)**0.5

            if self.comb.mols_c > 0 or self.oxid.mols_c > 0:
                n_CO2 = (N_C_reagentes*kp5)/((kp1*n_O)+kp5)
                n_CO = N_C_reagentes-n_CO2
            else:
                n_CO = 0
                n_CO2 = 0

            n_H2O = (N_O_reagentes-(2*n_CO2)-n_CO-(2*n_O2)-n_O)/(((n_O*kp7)/(n_O2*kp5))+1)
            n_OH = N_O_reagentes-n_H2O-2*n_CO2-n_CO-2*n_O2-n_O
            n_H = (n_O*n_OH*kp3)/(n_O2*kp5)
            n_H2 = (N_H_reagentes-2*n_H2O-n_OH-n_H)/2

            if self.comb.mols_n > 0 or self.oxid.mols_n > 0:
                n_N_a = (2*n_O2*kp5)/(kp6*n_O**2)
                n_N_b = 1
                n_N_c = -N_N_reagentes
                n_N_r1 = (-n_N_b+((n_N_b**2 - 4*n_N_a*n_N_c)**0.5))/(2*n_N_a)
                n_N_r2 = (-n_N_b-((n_N_b**2 - 4*n_N_a*n_N_c)**0.5))/(2*n_N_a)
                if n_N_r1 > 0:
                    n_N = n_N_r1
                else:
                    n_N = n_N_r2

                n_N2 = ((n_O2*kp5)/(kp6*n_O**2))*n_N**2
            else:
                n_N = 0
                n_N2 = 0

            N_C_produtos = n_CO2 + n_CO
            N_H_produtos = 2*n_H2O + n_OH + 2*n_H2 + n_H
            N_O_produtos = n_H2O + 2*n_CO2 + n_CO + n_OH + 2*n_O2 + n_O
            N_N_produtos = 2*n_N2 + n_N
            N_total_produtos = N_C_produtos + N_H_produtos + N_O_produtos + N_N_produtos
            iteracoes += 1
            print(iteracoes, n_O2)
            n_O2 += 0.001
        #print(f"n:{n_total}, N:{n_total_calc}, {(erro)}")
        print(f" CO2: {n_CO2}, CO: {n_CO}, H2O: {n_H2O}, OH: {n_OH}, O2: {n_O2}, O: {n_O}, H2: {n_H2}, H: {n_H},   N2: {n_N2}, N: {n_N} razao_mist: {self.razao_mistura}")
        #print(f"o2: {N_o2/n_total_calc}, o: {N_o/n_total_calc}, CO2: {N_CO2/n_total_calc}, co: {N_co/n_total_calc}, h: {N_h/n_total_calc}, h2: {N_h2/n_total_calc}, oh: {N_oh/n_total_calc}, H2O: {N_H2O/n_total_calc}, n: {N_n/n_total_calc}, N2: {N_N2/n_total_calc} razao_mist: {self.razao_mistura}")
        print(f"Nc_r:{N_C_reagentes} No_r:{N_O_reagentes} Nh_r:{N_H_reagentes} Nn_r:{N_N_reagentes}")
        print(f"Nc_p:{N_C_produtos} No_p:{N_O_produtos} Nh_p:{N_H_produtos} Nn_p:{N_N_produtos}")   
        
        
        
        


        """
        
        CÁLCULO DA REAÇÃO DE COMBUSTÃO COM DISSOCIAÇÃO
        
        if razao_equiv != 1:
            temp_adiab = 3234.87
            # Número de mols dos Propelentes
            
            print(f"n_comb: {self.n_comb}")
            print(f"n_oxid: {self.n_oxid}")

            self.razao_mistura = self.razao_mistura_estequiometrica / self.razao_equiv

            self.n_comb = (self.n_oxid * self.oxid.massa_molar) / (self.razao_mistura * self.comb.massa_molar)

            self.matriz_estequiometrica = matriz

            # Número de mols dos elementos
            if self.comb.mols_c > 0 or self.oxid.mols_c > 0:
                n_c = self.n_comb*self.comb.mols_c + self.n_oxid*self.oxid.mols_c
                n_total = n_c
                print(f"Nc:{n_c}")
            if self.comb.mols_o > 0 or self.oxid.mols_o > 0:
                n_o = self.n_comb*self.comb.mols_o + self.n_oxid*self.oxid.mols_o
                n_total += n_o
                print(f"No:{n_o}")
            if self.comb.mols_h > 0 or self.oxid.mols_h > 0:
                n_h = self.n_comb*self.comb.mols_h + self.n_oxid*self.oxid.mols_h
                n_total += n_h
                print(f"Nh:{n_h}")
            if self.comb.mols_n > 0 or self.oxid.mols_n > 0:
                n_n = self.n_comb*self.comb.mols_n + self.n_oxid*self.oxid.mols_n
                n_total += n_n
                print(f"Nn:{n_n}")
            print(f"Nc:{n_c/n_total} No:{n_o/n_total} Nh:{n_h/n_total}")

            # Calcula as funções de gibbs
            if (self.comb.mols_c > 0 or self.oxid.mols_c > 0) and (self.comb.mols_o > 0 or self.oxid.mols_o > 0):
                gibbs_CO2 = CO2.funcao_gibbs(temp_adiab)
                gibbs_co = co.funcao_gibbs(temp_adiab)
            if (self.comb.mols_o > 0 or self.oxid.mols_o > 0) and (self.comb.mols_h > 0 or self.oxid.mols_h > 0):
                gibbs_H2O = H2O.funcao_gibbs(temp_adiab)
                gibbs_oh = oh.funcao_gibbs(temp_adiab)
            if (self.comb.mols_h > 0 or self.oxid.mols_h > 0):
                gibbs_h2 = h2.funcao_gibbs(temp_adiab)
                gibbs_h = h.funcao_gibbs(temp_adiab)
            if (self.comb.mols_o > 0 or self.oxid.mols_o > 0):
                gibbs_o2 = o2.funcao_gibbs(temp_adiab)
                gibbs_o = o.funcao_gibbs(temp_adiab)
            if (self.comb.mols_n > 0 or self.oxid.mols_n > 0):
                gibbs_N2 = N2.funcao_gibbs(temp_adiab)
                gibbs_n = n.funcao_gibbs(temp_adiab)

            # Calcula as constantes de dissociação
            if (self.comb.mols_o > 0 or self.oxid.mols_o > 0) and (self.comb.mols_c > 0 or self.oxid.mols_c > 0):
                # CO2 --> CO + O
                kp1 = e**(-(1*gibbs_co + 1*gibbs_o - 1*gibbs_CO2)/(Constantes.const_univ_gases()*temp_adiab))
                print(f"kp1: {kp1}")
                if kp1 < 0.001:
                    print(f"kp1={kp1}<0.001, a dissociação CO2 --> CO + O não irá ocorrer a esta temperatura")
            if (self.comb.mols_o > 0 or self.oxid.mols_o > 0) and (self.comb.mols_h > 0 or self.oxid.mols_h > 0):
                # H2O --> 2H + O
                kp2 = e**(-(2*gibbs_h + 1*gibbs_o - 1*gibbs_H2O)/(Constantes.const_univ_gases()*temp_adiab))
                # OH --> H + O
                kp3 = e**(-(1*gibbs_h + 1*gibbs_o - 1*gibbs_oh)/(Constantes.const_univ_gases()*temp_adiab))
                # H2O --> OH + O
                kp7 = e**(-(1*gibbs_oh + 1*gibbs_o - 1*gibbs_H2O)/(Constantes.const_univ_gases()*temp_adiab))
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
                kp6 = e**(-(2*gibbs_n - 1*gibbs_N2)/(Constantes.const_univ_gases()*temp_adiab))
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
                    N_CO2 = (n_c*kp5)/((kp1*N_o)+kp5)
                    N_co = n_c-N_CO2
                else:
                    N_co = 0
                    N_CO2 = 0

                N_H2O = (n_o-(2*N_CO2)-N_co-(2*N_o2)-N_o)/(((N_o*kp7)/(N_o2*kp5))+1)
                N_oh = n_o-N_H2O-2*N_CO2-N_co-2*N_o2-N_o
                N_h = (N_o*N_oh*kp3)/(N_o2*kp5)
                N_h2 = (n_h-2*N_H2O-N_oh-N_h)/2

                if self.comb.mols_n > 0 or self.oxid.mols_n > 0:
                    N_n_a = (2*N_o2*kp5)/(kp6*N_o**2)
                    N_n_b = 1
                    N_n_c = -n_n
                    N_n = (-N_n_b+((N_n_b**2 - 4*N_n_a*N_n_c)**0.5))/(2*N_n_a)

                    N_N2 = ((N_o2*kp5)/(kp6*N_o**2))*N_n**2
                else:
                    N_n = 0
                    N_N2 = 0

                n_total_calc = N_o2+N_o+N_CO2+N_co+N_h+N_h2+N_oh+N_H2O+N_n+N_N2
                n_o_calc = 2*N_o2+N_o+2*N_CO2+N_co+N_oh+N_H2O
                
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
                #print(f"o2: {N_o2/N_total}, o: {N_o/N_total}, CO2: {N_CO2/N_total}, co: {N_co/N_total}, h: {N_h/N_total}, h2: {N_h2/N_total}, oh: {N_oh/N_total}, H2O: {N_H2O/N_total}, n: {N_n/N_total}, N2: {N_N2/N_total} razao_mist: {razao_mistura}")
            print(f"o2: {N_o2/n_total_calc}, o: {N_o/n_total_calc}, CO2: {N_CO2/n_total_calc}, co: {N_co/n_total_calc}, h: {N_h/n_total_calc}, h2: {N_h2/n_total_calc}, oh: {N_oh/n_total_calc}, H2O: {N_H2O/n_total_calc}, n: {N_n/n_total_calc}, N2: {N_N2/n_total_calc} razao_mist: {razao_mistura}")
                
            # Define os produtos de uma reação com dissociação
            "a*COMB + b+OXID ---> c*CO2 + d*CO + e*H2O + f*OH + g*H2 + h*H + i*O2 + j*O + k*N2 + l*N"
            if (self.comb.mols_c > 0 or self.oxid.mols_c > 0) and (self.comb.mols_o > 0 or self.oxid.mols_o > 0):
                self.produtos_dissociacao.append((CO2,N_CO2/n_total_calc))
                self.produtos_dissociacao.append((co, N_co/n_total_calc))
            if (self.comb.mols_o > 0 or self.oxid.mols_o > 0) and (self.comb.mols_h > 0 or self.oxid.mols_h > 0):
                self.produtos_dissociacao.append((H2O, N_H2O/n_total_calc))
                self.produtos_dissociacao.append((oh, N_oh/n_total_calc))
            if (self.comb.mols_h > 0 or self.oxid.mols_h > 0):
                self.produtos_dissociacao.append((h2, N_h2/n_total_calc))
                self.produtos_dissociacao.append((h, N_h/n_total_calc))
            if (self.comb.mols_o > 0 or self.oxid.mols_o > 0):
                self.produtos_dissociacao.append((o2, N_o2/n_total_calc))
                self.produtos_dissociacao.append((o, N_o/n_total_calc))
            if (self.comb.mols_n > 0 or self.oxid.mols_n > 0):
                self.produtos_dissociacao.append((N2, N_N2/n_total_calc))
                self.produtos_dissociacao.append((n, N_n/n_total_calc))


            #self.produtos_dissociacao_mols = []
            #self.produtos_dissociacao_mols.append(N_CO2)
            #self.produtos_dissociacao_mols.append(N_co)
            #self.produtos_dissociacao_mols.append(N_H2O)
            #self.produtos_dissociacao_mols.append(N_oh)
            #self.produtos_dissociacao_mols.append(N_h2)
            #self.produtos_dissociacao_mols.append(N_h)
            #self.produtos_dissociacao_mols.append(N_o2)
            #self.produtos_dissociacao_mols.append(N_o)

            #self.produtos_dissociacao_fracao_molar = []
            #self.produtos_dissociacao_fracao_molar.append(N_CO2/n_total_calc)
            #self.produtos_dissociacao_fracao_molar.append(N_co/n_total_calc)
            #self.produtos_dissociacao_fracao_molar.append(N_H2O/n_total_calc)
            #self.produtos_dissociacao_fracao_molar.append(N_oh/n_total_calc)
            #self.produtos_dissociacao_fracao_molar.append(N_h2/n_total_calc)
            #self.produtos_dissociacao_fracao_molar.append(N_h/n_total_calc)
            #self.produtos_dissociacao_fracao_molar.append(N_o2/n_total_calc)
            #self.produtos_dissociacao_fracao_molar.append(N_o/n_total_calc)
                #print(f"RME: {razao_mistura_estequiometrica}")
                #print(f"RE: {razao_equiv}")
                #print(f"RE: {razao_mistura}")"""
            
    @property
    def reacao_estequiometrica_resultado(self):
        """Exibe o resultado da reação de combustão com o número de mols de cada elemento"""
        if self.razao_equiv == 1:
            reacao = f"{self.n_comb} {self.propelentes[0]} + %.3f  {self.propelentes[1]} --> " %(self.n_oxid)

            x = 0
            for i in self.produtos_estequiometrico:

                reacao += f"%.3f {self.produtos_estequiometrico[x][0]}" %(self.produtos_estequiometrico[x][1])
                print(x)
                if i is not self.produtos_estequiometrico[-1]:
                    reacao += " + "
                x += 1
            return reacao
        else:
            return "ERRO: para visualizar a reação estequiométrica utilize Razão de Equivalência = 1"
            
        

    @property
    def reacao_dissociacao_resultado(self):
        """Exibe o resultado da reação de combustão com o número de mols de cada elemento"""
        a = self.n_comb
        matriz = self.matriz_estequiometrica

        reacao = f"{a} {self.propelentes[0]} + {self.n_oxid} {self.propelentes[1]} -->"

        print(self.produtos_dissociacao)

        x = 0
        for i in self.produtos_dissociacao:
            reacao += f" {self.produtos_dissociacao[x][1]} "
            reacao += f" {self.produtos_dissociacao[x][0]}"
            if self.produtos_dissociacao[x] == self.produtos_dissociacao[-1]:
                reacao
            else:
                reacao += " + "
            x += 1
        return reacao

    @property
    def a(self):
        """Retorna o número de mols do Combustível"""
        a = self.n_comb
        return a

    @property
    def b(self):
        """Retorna o número de mols do oxidante"""
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
    #    return self.razao_mistura

    #@property
    #def razao_mistura(self):
    #    return self.razao_mistura

    @property
    def razao_equivalencia(self):
        return self.razao_equivalencia
