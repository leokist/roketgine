from .produtos import *
from .constantes import *
from .reacoes_dissociacao import *
from math import pi, tan

class Motor():
    def __init__(self, comb, oxid, razao_equiv, forca_empuxo, comprimento_caracteristico, pressao, pressao_externa=1):
        self._comb = comb
        self._oxid = oxid
        self._razao_equiv = razao_equiv 
        self._pressao = pressao  * Constantes.pressao_atmosferica()                 # Converte a pressão de [atm] para [pa]
        self._pressao_atm = pressao
        self._pressao_externa = pressao_externa * Constantes.pressao_atmosferica()  # Converte a pressão de [atm] para [pa]
        self._propelentes = [comb, oxid]
        self._forca_empuxo = forca_empuxo
        self._comprimento_característico = comprimento_caracteristico
    """
    #
    # Combustão Estequiométrica
    #
    """
    def reacao_estequiometrica(self):
        """
        Executa o cálculo da reação de combustão estequiométrica.
        """
        self._produtos_estequiometrico = []
        self._matriz_estequiometrica = []
        self._n_comb_estequiometrico = 1
        
        """
                b                      c             d                      a
        [self.oxid.mols_o, - prod1.mols_o, - prod2.mols_o, - self.comb.mols_o],
        [self.oxid.mols_h, - prod1.mols_h, - prod2.mols_h, - self.comb.mols_h],
        [self.oxid.mols_c, - prod1.mols_c, - prod2.mols_c, - self.comb.mols_c],
        """

        # Define os produtos de uma reação estequiométrica
        "a*COMB + b+OXID ---> c*H2O + d*CO2 + e*N2"
        if self._razao_equiv != 0 and (self._comb.mols_o > 0 or self._oxid.mols_o > 0) and (self._comb.mols_h > 0 or self._oxid.mols_h > 0):
            self._produtos_estequiometrico.append([H2O, 0])
        if self._razao_equiv != 0 and (self._comb.mols_c > 0 or self._oxid.mols_c > 0) and (self._comb.mols_o > 0 or self._oxid.mols_o > 0):
            self._produtos_estequiometrico.append([CO2, 0])
        if self._razao_equiv != 0 and (self._comb.mols_n > 0 or self._oxid.mols_n > 0):
            self._produtos_estequiometrico.append([N2, 0])
                
        # Obtém a quantidade total de produtos da reação
        n_produtos = len(self._produtos_estequiometrico)

        # Obtem a quantidade total de reagentes da reação
        n_propelentes = len(self._propelentes)

        # Obtém a quantidade total de elementos
        if self._comb.mols_o != 0 or self._oxid.mols_o != 0:
            n_elementos = 1
        if self._comb.mols_h != 0 or self._oxid.mols_h != 0:
            n_elementos += 1
        if self._comb.mols_c != 0 or self._oxid.mols_c != 0:
            n_elementos += 1
        if self._comb.mols_n != 0 or self._oxid.mols_n != 0:
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
                if self._comb.mols_o == 0 and self._oxid.mols_o == 0:
                    lin = 0
                else:
                    while col != (n_especies - 1):
                        if col == 0:
                            matriz[lin].insert(col,self._propelentes[1].mols_o)
                        if col != 0:
                            matriz[lin].insert(col, -1 * self._produtos_estequiometrico[col-1][0].mols_o)
                        if col == (n_produtos - 1):
                            matriz[lin].insert(col+1, -1 * self._propelentes[0].mols_o)
                        col += 1
                    lin += 1
                    col = 0
            elif contador == 1:
                if self._comb.mols_h == 0 and self._oxid.mols_h == 0:
                    lin = 1
                else:
                    while col != (n_especies - 1):
                        if col == 0:
                            matriz[lin].insert(col,self._propelentes[1].mols_h)
                        if col != 0:
                            matriz[lin].insert(col, -1 * self._produtos_estequiometrico[col-1][0].mols_h)
                        if col == (n_produtos - 1):
                            matriz[lin].insert(col+1, -1 * self._propelentes[0].mols_h)
                        col += 1 
                    lin += 1
                    col = 0
            elif contador == 2:
                if self._comb.mols_c == 0 and self._oxid.mols_c == 0:
                    lin = 2
                else:
                    while col != (n_especies - 1):
                        if col == 0:
                            matriz[lin].insert(col,self._propelentes[1].mols_c)
                        if col != 0:
                            matriz[lin].insert(col, -1 * self._produtos_estequiometrico[col-1][0].mols_c)
                        if col == (n_produtos - 1):
                            matriz[lin].insert(col+1, -1 * self._propelentes[0].mols_c)
                        col += 1 
                    lin += 1
                    col = 0
            elif contador == 3:
                if self._comb.mols_n != 0 or self._oxid.mols_n != 0:
                    while col != (n_especies - 1):
                        if col == 0:
                            matriz[lin].insert(col,self._propelentes[1].mols_n)
                        if col != 0:
                            matriz[lin].insert(col, -1 * self._produtos_estequiometrico[col-1][0].mols_n)
                        if col == (n_produtos - 1):
                            matriz[lin].insert(col+1, - 1 * self._propelentes[0].mols_n)
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
        while y < len(matriz)-1:
            self._produtos_estequiometrico[y][1] = matriz[y+1][len(matriz)]
            y += 1
            lin += 1

        self._n_oxid = matriz[0][-1]
                                  
        self._razao_mistura_estequiometrica = (self._n_oxid*self._oxid.massa_molar)/(self._n_comb_estequiometrico*self._comb.massa_molar)
        
        """
        #
        # Cálculo da Temperatura Adiabática de Chama
        # 
        """

        # CALCULO ENTALPIA DOS REAGENTES
        # Como a temperatura do reagente utilizada para o cálculo da combustão
        # será igual a temperatura de referência, teremos:
        # Hr = n_comb (hf + h - h(ref)) + n_oxid (hf + h - h(ref))
        # Hr = n_comb * hf + n_oxid * hf 
        self._entalpia_reagentes_estequiometrico = self._n_comb_estequiometrico * self._comb.entalpia_formacao + self._n_oxid * self._oxid.entalpia_formacao
        #self._entalpia_reagentes_estequiometrico = self._n_comb_estequiometrico * (self._comb.entalpia_formacao + self._comb.entalpia(self._comb.temperatura_referencia) - self._comb.entalpia_referencia) + self._n_oxid * (self._oxid.entalpia_formacao + self._oxid.entalpia(self._oxid.temperatura_referencia) - self._oxid.entalpia_referencia)

        entalpia_produtos = 0
        x = 0
        y = 0
        temp_min = 200
        temp_max = 6000
        temp = 200
        produtos = self._produtos_estequiometrico
        erro = 1
        while abs(erro) > 0.1:
            while x < len(produtos):
                prod = produtos[x][0]
                prod_mols = produtos[x][1]
                #entalpia_produtos += prod_mols * (prod.entalpia_formacao + prod.entalpia(temp) - prod.entalpia_t_referencia)
                entalpia_produtos += prod_mols * (prod.entalpia(temp))

                x += 1
            
            erro = 100*((abs(self._entalpia_reagentes_estequiometrico)-abs(entalpia_produtos))/abs(entalpia_produtos))

            if temp > temp_max:
                break

            if abs(erro) > 0.1:
                entalpia_produtos = 0
                temp += 0.1
                x = 0
                y += 1

        self._temperatura_adiabatica_estequiometrica = temp
        self._entalpia_produtos_estequiometrico = entalpia_produtos
      
        """
        # Massa Molar Média
        """
        self._massa_molar_media_estequiometrica = 0
        self._total_mols_produto_estequiometrico = 0
        x = 0
        for i in self._produtos_estequiometrico:
            self._total_mols_produto_estequiometrico += self._produtos_estequiometrico[x][1]
            x += 1
        x = 0
        for i in self._produtos_estequiometrico:
            produto = self._produtos_estequiometrico[x][0]
            self._massa_molar_media_estequiometrica += (self._produtos_estequiometrico[x][1] / self._total_mols_produto_estequiometrico) * produto.massa_molar
            x += 1
        
        """
        # Calor Específico a Pressão Constante
        """
        self._cp_medio_estequiometrico = 0
        x = 0
        for i in self._produtos_estequiometrico:
            produto = self._produtos_estequiometrico[x][0]
            self._cp_medio_estequiometrico  += (self._produtos_estequiometrico[x][1] / self._total_mols_produto_estequiometrico) * produto.calor_especifico(self._temperatura_adiabatica_estequiometrica)
            x += 1
        self._cp_medio_estequiometrico = self._cp_medio_estequiometrico / self._massa_molar_media_estequiometrica

        """
        # Constante dos Gases
        """
        self._constante_gases_estequiometrico = Constantes.const_univ_gases() / self._massa_molar_media_estequiometrica


        """
        # Calor Específico a Volume Constante
        """
        self._cv_estequiometrico = self._cp_medio_estequiometrico - self._constante_gases_estequiometrico

        """
        # Razão dos Calores Específicos
        """
        self._k_estequiometrico = self._cp_medio_estequiometrico / self._cv_estequiometrico


    """
    #
    # Combustão Com Dissociação
    #
    """
    def reacao_dissociacao(self):
        """
        REACAO COM DISSOCIACAO
        """        
        self._razao_mistura_dissociacao = self._razao_mistura_estequiometrica / self._razao_equiv
        self._n_comb_dissociacao = (self._n_oxid * self._oxid.massa_molar) / (self._razao_mistura_dissociacao * self._comb.massa_molar)
        self._produtos_dissociacao = []

        n_total = 0
        # Número de mols dos elementos
        if self._comb.mols_c > 0 or self._oxid.mols_c > 0:
            N_C_reagentes = self._n_comb_dissociacao*self._comb.mols_c + self._n_oxid*self._oxid.mols_c
            N_total_reagentes = N_C_reagentes
            #print(f"Nc:{N_C_reagentes}")
        else:
            N_C_reagentes = 0
        if self._comb.mols_o > 0 or self._oxid.mols_o > 0:
            N_O_reagentes = self._n_comb_dissociacao*self._comb.mols_o + self._n_oxid*self._oxid.mols_o
            N_total_reagentes += N_O_reagentes
            #print(f"No:{N_O_reagentes}")
        else:
            N_O_reagentes = 0
        if self._comb.mols_h > 0 or self._oxid.mols_h > 0:
            N_H_reagentes = self._n_comb_dissociacao*self._comb.mols_h + self._n_oxid*self._oxid.mols_h
            N_total_reagentes += N_H_reagentes
            #print(f"Nh:{N_H_reagentes}")
        else:
            N_H_reagentes = 0
        if self._comb.mols_n > 0 or self._oxid.mols_n > 0:
            N_N_reagentes = self._n_comb_dissociacao*self._comb.mols_n + self._n_oxid*self._oxid.mols_n
            N_total_reagentes += N_N_reagentes
            #print(f"Nn:{N_N_reagentes}")
        else:
            N_N_reagentes = 0


        entalpia_produtos = 0
        x = 0
        y = 0
        temp_min = 200
        temp_max = 6000
        temp = 500
        produtos = self._produtos_dissociacao
        erro = 1
        yy = 0
        zz = 0 
        while yy < 3:
            print(yy, zz)

            # Calcula as constantes de dissociação
            if (self._comb.mols_o > 0 or self._oxid.mols_o > 0) and (self._comb.mols_c > 0 or self._oxid.mols_c > 0):
                # CO2 --> CO + O
                kp1 = reacao_CO2_para_CO_O.kp(temp)

            if (self._comb.mols_o > 0 or self._oxid.mols_o > 0) and (self._comb.mols_h > 0 or self._oxid.mols_h > 0):
                # H2O --> 2H + O
                kp2 = reacao_H2O_para_2H_O.kp(temp)
                # OH --> H + O
                kp3 = reacao_OH_para_H_O.kp(temp)
                # H2O --> OH + O
                kp7 = reacao_H2O_para_OH_O.kp(temp)

            if (self._comb.mols_h > 0 or self._oxid.mols_h > 0):
                # H2 --> 2 H
                kp4 = reacao_H2_para_2H.kp(20000)

            if (self._comb.mols_o > 0 or self._oxid.mols_o > 0):
                # O2 --> 2 O
                kp5 = reacao_O2_para_2O.kp(20000)

            if (self._comb.mols_n > 0 or self._oxid.mols_n > 0):
                # N2 --> 2 N 
                kp6 = reacao_N2_para_2N.kp(20000)

            
            #print(f"kp1: {kp1: .3f},kp2: {kp2: .3f},kp3: {kp3: .3f},kp4: {kp4: .3f},kp5: {kp5: .3f},kp6: {kp6: .3f}")

            p = self._pressao
            y = p / N_total_reagentes
            n_O2 = 0
            iteracoes = 0

            while zz < 3:
                #(n_CO2<0 or n_CO<0 or n_H2O<0 or n_OH<0 or n_O2<0 or n_O<0 or n_H2<0 or n_H<0 or n_N2<0 or n_N<0) or 
                n_O = (kp5*n_O2/y)**0.5

                if self._comb.mols_c > 0 or self._oxid.mols_c > 0:
                    n_CO2 = (N_C_reagentes*kp5)/((kp1*n_O)+kp5)
                    n_CO = N_C_reagentes-n_CO2
                else:
                    n_CO = 0
                    n_CO2 = 0

                n_H2O = (N_O_reagentes-(2*n_CO2)-n_CO-(2*n_O2)-n_O)/(((n_O*kp7)/(n_O2*kp5))+1)
                n_OH = N_O_reagentes-n_H2O-2*n_CO2-n_CO-2*n_O2-n_O
                n_H = (n_O*n_OH*kp3)/(n_O2*kp5)
                n_H2 = (N_H_reagentes-2*n_H2O-n_OH-n_H)/2

                if self._comb.mols_n > 0 or self._oxid.mols_n > 0:
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
                #print(iteracoes, n_O2)

                print(N_total_reagentes, N_total_produtos)

                erro2 = 100*((abs(N_total_reagentes)-abs(N_total_produtos))/abs(N_total_produtos))

                n_O2 += 0.1
                zz += 1

            # Define os produtos de uma reação com dissociação
            "a*COMB + b+OXID ---> c*CO2 + d*CO + e*H2O + f*OH + g*H2 + h*H + i*O2 + j*O + k*N2 + l*N"
            if (self._comb.mols_c > 0 or self._oxid.mols_c > 0) and (self._comb.mols_o > 0 or self._oxid.mols_o > 0):
                self._produtos_dissociacao.append([CO2, n_CO2])
                self._produtos_dissociacao.append([CO, n_CO])
            if (self._comb.mols_o > 0 or self._oxid.mols_o > 0) and (self._comb.mols_h > 0 or self._oxid.mols_h > 0):
                self._produtos_dissociacao.append([H2O, n_H2O])
                self._produtos_dissociacao.append([OH, n_OH])
            if (self._comb.mols_h > 0 or self._oxid.mols_h > 0):
                self._produtos_dissociacao.append([H2, n_H2])
                self._produtos_dissociacao.append([H, n_H])
            if (self._comb.mols_o > 0 or self._oxid.mols_o > 0):
                self._produtos_dissociacao.append([O2, n_O2])
                self._produtos_dissociacao.append([O, n_O])
            if (self._comb.mols_n > 0 or self._oxid.mols_n > 0):
                self._produtos_dissociacao.append([N2, n_N2])
                self._produtos_dissociacao.append([N, n_N])

            print(f" CO2: {n_CO2: .6f}, CO: {n_CO: .6f}, H2O: {n_H2O: .6f}, OH: {n_OH: .6f}, O2: {n_O2: .6f}, O: {n_O: .6f}, H2: {n_H2: .6f}, H: {n_H: .6f},   N2: {n_N2: .6f}, N: {n_N: .6f} razao_mist: {self.razao_mistura}")

            while x < len(self._produtos_dissociacao):
                prod = self._produtos_dissociacao[x][0]
                prod_mols = self._produtos_dissociacao[x][1]

                entalpia_produtos += prod_mols * (prod.entalpia(temp))

                x += 1
            
            erro = 100*((abs(self.entalpia_reagentes)-abs(entalpia_produtos))/abs(entalpia_produtos))
            print()

            if yy == 2:
                self._temperatura_adiabatica_dissociacao = temp
            else:
                temp += 1
            yy += 1

            if abs(erro) > 0.1:
                self._produtos_dissociacao.clear

            

        #print(f"n:{n_total}, N:{n_total_calc}, {(erro)}")
        print(f" CO2: {n_CO2}, CO: {n_CO}, H2O: {n_H2O}, OH: {n_OH}, O2: {n_O2}, O: {n_O}, H2: {n_H2}, H: {n_H},   N2: {n_N2}, N: {n_N} razao_mist: {self.razao_mistura}")
        #print(f"o2: {N_o2/n_total_calc}, o: {N_o/n_total_calc}, CO2: {N_CO2/n_total_calc}, co: {N_co/n_total_calc}, h: {N_h/n_total_calc}, h2: {N_h2/n_total_calc}, oh: {N_oh/n_total_calc}, H2O: {N_H2O/n_total_calc}, n: {N_n/n_total_calc}, N2: {N_N2/n_total_calc} razao_mist: {self.razao_mistura}")
        print(f"Nc_r:{N_C_reagentes} No_r:{N_O_reagentes} Nh_r:{N_H_reagentes} Nn_r:{N_N_reagentes}")
        print(f"Nc_p:{N_C_produtos} No_p:{N_O_produtos} Nh_p:{N_H_produtos} Nn_p:{N_N_produtos}")

        """
        # Massa Molar Média
        """
        self._massa_molar_media_dissociacao = 0
        self._total_mols_produto_dissociacao = 0
        x = 0
        for i in self._produtos_dissociacao:
            self._total_mols_produto_dissociacao += self._produtos_dissociacao[x][1]
            x += 1
        x = 0
        for i in self._produtos_dissociacao:
            produto = self._produtos_dissociacao[x][0]
            self._massa_molar_media_dissociacao += (self._produtos_dissociacao[x][1] / self._total_mols_produto_dissociacao) * produto.massa_molar
            x += 1
        
        """
        # Calor Específico a Pressão Constante
        """
        self._cp_medio_dissociacao = 0
        x = 0
        for i in self._produtos_dissociacao:
            produto = self._produtos_dissociacao[x][0]
            self._cp_medio_dissociacao += (self._produtos_dissociacao[x][1] / self._total_mols_produto_dissociacao) * produto.calor_especifico(self._temperatura_adiabatica_dissociacao)
            x += 1
        self._cp_medio_dissociacao = self._cp_medio_dissociacao / self._massa_molar_media_dissociacao

        """
        # Constante dos Gases
        """
        self._constante_gases_dissociacao = Constantes.const_univ_gases() / self._massa_molar_media_dissociacao

        """
        # Calor Específico a Volume Constante
        """
        self._cv_dissociacao = self._cp_medio_dissociacao - self._constante_gases_dissociacao

        """
        # Razão dos Calores Específicos
        """
        self._k_dissociacao = self._cp_medio_dissociacao / self._cv_dissociacao

    def reacao_dissociacao_V3(self):
        """
        REACAO COM DISSOCIACAO
        """        
        self._razao_mistura_dissociacao = self._razao_mistura_estequiometrica / self._razao_equiv
        self._n_comb_dissociacao = (self._n_oxid * self._oxid.massa_molar) / (self._razao_mistura_dissociacao * self._comb.massa_molar)
        self._produtos_dissociacao = []
        P = self._pressao_atm

        # Fracao Molar dos Reagentes
        N_total_reagentes = self._n_comb_dissociacao + self._n_oxid
        x_comb = self._n_comb_dissociacao / N_total_reagentes
        x_oxid = self._n_oxid / N_total_reagentes

        # Número de mols dos elementos dos Reagentes
        if self._comb.mols_c > 0 or self._oxid.mols_c > 0:
            X_C_reagentes = x_comb*self._comb.mols_c + x_oxid*self._oxid.mols_c
        else:
            X_C_reagentes = 0
        if self._comb.mols_o > 0 or self._oxid.mols_o > 0:
            X_O_reagentes = x_comb*self._comb.mols_o + x_oxid*self._oxid.mols_o
        else:
            X_O_reagentes = 0
        if self._comb.mols_h > 0 or self._oxid.mols_h > 0:
            X_H_reagentes = x_comb*self._comb.mols_h + x_oxid*self._oxid.mols_h
        else:
            X_H_reagentes = 0
        if self._comb.mols_n > 0 or self._oxid.mols_n > 0:
            X_N_reagentes = x_comb*self._comb.mols_n + x_oxid*self._oxid.mols_n
        else:
            X_N_reagentes = 0
        print(X_N_reagentes, x_comb*self._comb.mols_n, x_oxid*self._oxid.mols_n)
     
  
        # CALCULO ENTALPIA DOS REAGENTES
        # Como a temperatura do reagente utilizada para o cálculo da combustão
        # será igual a temperatura de referência, teremos:
        # Hr = n_comb (hf + h - h(ref)) + n_oxid (hf + h - h(ref))
        # Hr = n_comb * hf + n_oxid * hf 
        self._entalpia_reagentes_dissociacao = x_comb * self._comb.entalpia_formacao + x_oxid * self._oxid.entalpia_formacao

        
        temp_min = 200
        temp_max = 6000
        temp = 3100
        erro = 1
        zz = 0
        while erro > 0.01 and zz <= 20:
            self._produtos_dissociacao.clear()
            # Calcula as constantes de dissociação
            if (self._comb.mols_o > 0 or self._oxid.mols_o > 0) and (self._comb.mols_c > 0 or self._oxid.mols_c > 0):
                # 2CO2 --> 2CO + O2
                kp1 = reacao_2CO2_para_2CO_O2.kp(temp)
            if (self._comb.mols_o > 0 or self._oxid.mols_o > 0) and (self._comb.mols_h > 0 or self._oxid.mols_h > 0):
                # H2O --> H + OH
                kp2 = reacao_H2O_para_H_OH.kp(temp)
                # OH --> H + O
                kp3 = reacao_OH_para_H_O.kp(temp)
            if (self._comb.mols_h > 0 or self._oxid.mols_h > 0):
                # H2 --> 2H
                kp4 = reacao_H2_para_2H.kp(20000)
            if (self._comb.mols_o > 0 or self._oxid.mols_o > 0):
                # O2 --> 2O
                kp5 = reacao_O2_para_2O.kp(20000)
            if (self._comb.mols_n > 0 or self._oxid.mols_n > 0):
                # N2 --> 2 N 
                kp6 = reacao_N2_para_2N.kp(20000)
            
            #print(f"kp1: {kp1: .3f},kp2: {kp2: .3f},kp3: {kp3: .3f},kp4: {kp4: .3f},kp5: {kp5: .3f}, kp6: {kp6: .3f}")
            
            x_O2_max = 1
            x_O2_min = 0
            x_O2 = 0.5
            erro2 = 100
            kk = 0
            while erro2 > 0.01 and kk <= 20:
                p_total = 0
                x_O = (kp5*x_O2/P)**0.5

                # Calculo de x_CO e x_CO2
                if self._comb.mols_c > 0 or self._oxid.mols_c > 0:
                    x_CO = (X_C_reagentes * (kp1/(x_O2*P))**0.5) / (1 + ((kp1/(x_O2*P))**0.5))
                    x_CO2 = X_C_reagentes - x_CO
                else:
                    x_CO = 0
                    x_CO2 = 0

                # Calculo do x_H por bascara
                a_x_H = ((x_O * (P**2)) / kp3) / kp2
                b_x_H = (x_O * P) / kp3
                c_x_H = 2*x_CO2 + x_CO + 2*x_O2 + x_O - X_O_reagentes
                delta_H = (b_x_H**2) - (4 * a_x_H * c_x_H)
                if delta_H < 0:
                    x_H = 0
                else:
                    x_H_1 = (-1 * b_x_H + (delta_H)**0.5) / ( 2 * a_x_H)
                    x_H_2 = (-1 * b_x_H - (delta_H)**0.5) / ( 2 * a_x_H)
                    if x_H_1 > 0:
                        x_H = x_H_1
                    else:               
                        x_H = x_H_2
            
                # Calculo de x_H2, x_OH e x_H2O
                x_H2 = ((x_H**2) * P)/ kp4
                x_OH = (x_H * x_O * P) / kp3
                x_H2O = (x_H * x_OH * P) / kp2

                # Calculo do x_N por bascara
                if self._comb.mols_n > 0 or self._oxid.mols_n > 0:
                    a_x_N = (2 * P) / kp6
                    b_x_N = 1
                    c_x_N = - X_N_reagentes
                    delta_N = (b_x_N**2) - (4 * a_x_N * c_x_N)
                    if delta_N < 0:
                        x_N = 0
                    else:
                        x_N_1 = (-1 * b_x_N + (delta_N)**0.5) / ( 2 * a_x_N)
                        x_N_2 = (-1 * b_x_N - (delta_N)**0.5) / ( 2 * a_x_N)
                        if x_N_1 > 0:
                            x_N = x_N_1
                        else:
                            x_N = x_N_2
                                    
                    # Calculo de n_N2
                    x_N2 = ((x_N**2) * P) / kp6
                else:
                    x_N = 0
                    x_N2 = 0
                

                X_C_produtos = x_CO2 + x_CO
                X_H_produtos = 2*x_H2O + x_OH + 2*x_H2 + x_H
                X_O_produtos = x_H2O + 2*x_CO2 + x_CO + x_OH + 2*x_O2 + x_O
                X_N_produtos = 2*x_N2 + x_N
                N_total_produtos = x_CO2 + x_CO + x_H2O + x_OH + x_H2 + x_H + x_O2 + x_O + x_N2 + x_N
                
                # Calculo da Pressao Total
                P_total = x_CO2*P + x_CO*P + x_H2O*P + x_OH*P + x_H2*P + x_H*P + x_O2*P + x_O*P + x_N2*P + x_N*P

                # Erro entre as pressões
                erro2 = 100 * abs((P_total - P)/P)
                #print(kk, "x_O2_min", f"{x_O2_min : .3f}","x_O2", f"{x_O2 : .3f}","x_O2_max", f"{x_O2_max : .3f}",  "p_total", f"{P_total : .3f}", "p", P, "erro", f"{erro2 : .3f}")
                
                # Definição do novo valor de x_O2
                #if erro2 > 0.01:
                #    x_O2 -= 0.001
                if P_total > P:
                    x_O2_max = x_O2
                    x_O2_min = x_O2_min
                    x_O2 = (x_O2_max + x_O2_min)/2
                else:
                    x_O2_max = x_O2_max
                    x_O2_min = x_O2
                    x_O2 = (x_O2_max + x_O2_min)/2
                kk += 1
            #print(X_N_reagentes, delta_N, x_N, x_N2, kp6, erro2)    

            #print(kk, "x_O2_min", f"{x_O2_min : .3f}","x_O2", f"{x_O2 : .3f}","x_O2_max", f"{x_O2_max : .3f}",  "p_total", f"{P_total : .3f}", "p", P, "erro", f"{erro2 : .3f}")


            # Define os produtos de uma reação com dissociação
            "a*COMB + b+OXID ---> c*CO2 + d*CO + e*H2O + f*OH + g*H2 + h*H + i*O2 + j*O + k*N2 + l*N"
            if (self._comb.mols_c > 0 or self._oxid.mols_c > 0) and (self._comb.mols_o > 0 or self._oxid.mols_o > 0):
                self._produtos_dissociacao.append([CO2, x_CO2])
                self._produtos_dissociacao.append([CO, x_CO])
            if (self._comb.mols_o > 0 or self._oxid.mols_o > 0) and (self._comb.mols_h > 0 or self._oxid.mols_h > 0):
                self._produtos_dissociacao.append([H2O, x_H2O])
                self._produtos_dissociacao.append([OH, x_OH])
            if (self._comb.mols_h > 0 or self._oxid.mols_h > 0):
                self._produtos_dissociacao.append([H2, x_H2])
                self._produtos_dissociacao.append([H, x_H])
            if (self._comb.mols_o > 0 or self._oxid.mols_o > 0):
                self._produtos_dissociacao.append([O2, x_O2])
                self._produtos_dissociacao.append([O, x_O])
            if (self._comb.mols_n > 0 or self._oxid.mols_n > 0):
                self._produtos_dissociacao.append([N2, x_N2])
                self._produtos_dissociacao.append([N, x_N])

            #print(self._produtos_dissociacao)
            entalpia_produtos = 0
            x = 0
            while x < len(self._produtos_dissociacao):
                prod = self._produtos_dissociacao[x][0]
                prod_mols = self._produtos_dissociacao[x][1]
                #print(prod, prod.entalpia(temp))
                entalpia_produtos += prod_mols * (prod.entalpia(temp))
                x += 1
            
            erro = 100 * abs((entalpia_produtos - self._entalpia_reagentes_dissociacao) / self._entalpia_reagentes_dissociacao)
            #print("temp_min:", f"{temp_min : .3f}", "temp:", f"{temp : .3f}","temp_max:", f"{temp_max : .3f}",entalpia_produtos > self._entalpia_reagentes_dissociacao, "H_r ", f"{self._entalpia_reagentes_dissociacao : .3f}", "H_p ", f"{entalpia_produtos : .3f}", "erro ", f"{erro : .3f}", "p_calc", f"{P_total : .3f}")

            # Definição do novo valor de temperatura
            if erro > 0.01:
                if entalpia_produtos > self._entalpia_reagentes_dissociacao :
                    temp_max = temp
                    temp_min = temp_min
                    temp = (temp_max + temp_min)/2
                else:
                    temp_max = temp_max
                    temp_min = temp
                    temp = (temp_max + temp_min)/2
            zz+=1

        print(kk, "x_O2_min", f"{x_O2_min : .3f}","x_O2", f"{x_O2 : .3f}","x_O2_max", f"{x_O2_max : .3f}",  "p_total", f"{P_total : .3f}", "p", P, "erro", f"{erro2 : .3f}")
        #print(f"kp1: {kp1: .3f},kp2: {kp2: .3f},kp3: {kp3: .3f},kp4: {kp4: .3f},kp5: {kp5: .3f}, kp6: {kp6: .3f}")
        print("x_O2:",f"{x_O2: .4f} ","x_O:",f"{x_O : .4f} ","x_CO2:",f"{x_CO2 : .4f} ","x_CO:",f"{x_CO : .4f} ","x_H2O:",f"{x_H2O : .4f} ","x_OH:",f"{x_OH : .4f} ","x_H2:",f"{x_H2 : .4f} ","x_H:",f"{x_H : .4f} ","x_N2:",f"{x_N2 : .4f} ","x_N:",f"{x_N : .4f}",)
        print(zz, "temp_min:", f"{temp_min : .3f}", "temp:", f"{temp : .3f}","temp_max:", f"{temp_max : .3f}",entalpia_produtos > self._entalpia_reagentes_dissociacao, "H_r ", f"{self._entalpia_reagentes_dissociacao : .3f}", "H_p ", f"{entalpia_produtos : .3f}", "erro ", f"{erro : .3f}", "p_calc", f"{P_total : .3f}")
        

        self._entalpia_produtos_dissociacao = entalpia_produtos
        self._temperatura_adiabatica_dissociacao = temp
        self._erro_dissociacao = erro2
        self._erro_temperatura = erro

        """
        # Massa Molar Média
        """
        self._massa_molar_media_dissociacao = 0
        self._total_mols_produto_dissociacao = 0
        x = 0
        for i in self._produtos_dissociacao:
            self._total_mols_produto_dissociacao += self._produtos_dissociacao[x][1]
            x += 1
        x = 0
        for i in self._produtos_dissociacao:
            produto = self._produtos_dissociacao[x][0]
            self._massa_molar_media_dissociacao += (self._produtos_dissociacao[x][1] / self._total_mols_produto_dissociacao) * produto.massa_molar
            x += 1
        
        #print("MMMD", self._massa_molar_media_dissociacao, "TMD", self._total_mols_produto_dissociacao)
        
        """
        # Calor Específico a Pressão Constante
        """
        self._cp_medio_dissociacao = 0
        x = 0
        for i in self._produtos_dissociacao:
            produto = self._produtos_dissociacao[x][0]
            self._cp_medio_dissociacao += (self._produtos_dissociacao[x][1] / self._total_mols_produto_dissociacao) * produto.calor_especifico(self._temperatura_adiabatica_dissociacao)
            x += 1
        self._cp_medio_dissociacao = self._cp_medio_dissociacao / self._massa_molar_media_dissociacao

        """
        # Constante dos Gases
        """
        self._constante_gases_dissociacao = Constantes.const_univ_gases() / self._massa_molar_media_dissociacao

        """
        # Calor Específico a Volume Constante
        """
        self._cv_dissociacao = self._cp_medio_dissociacao - self._constante_gases_dissociacao

        """
        # Razão dos Calores Específicos
        """
        self._k_dissociacao = self._cp_medio_dissociacao / self._cv_dissociacao


    @property
    def status_reacao(self):
        if self._razao_equiv == 1:
            status = "ok"
        else:
            if self._erro_dissociacao > 0.01 or self._erro_temperatura > 0.01:
                status = "erro"
            else:
                status = "ok"
        return status

    @property
    def combustao_resultado(self):
        """Exibe o resultado da reação de combustão com o número de mols de cada elemento"""
        # Retorna o resultado da reação estequiométrica
        if self._razao_equiv == 1:
            reacao = f"{self._n_comb_estequiometrico} {self._propelentes[0]} + %.3f  {self._propelentes[1]} --> " %(self._n_oxid)

            x = 0
            for i in self._produtos_estequiometrico:

                reacao += f"%.3f {self._produtos_estequiometrico[x][0]}" %(self._produtos_estequiometrico[x][1])
                if i is not self._produtos_estequiometrico[-1]:
                    reacao += " + "
                x += 1
            return reacao
        #Retorna o resultado da reação com dissociação
        else:
            a = self._n_comb_dissociacao
            matriz = self._matriz_estequiometrica

            reacao = f"{a} {self._propelentes[0]} + {self._n_oxid} {self._propelentes[1]} -->"

            #print(self._produtos_dissociacao)

            x = 0
            for i in self._produtos_dissociacao:
                reacao += f" {self._produtos_dissociacao[x][1]} "
                reacao += f" {self._produtos_dissociacao[x][0]}"
                if self._produtos_dissociacao[x] == self._produtos_dissociacao[-1]:
                    reacao
                else:
                    reacao += " + "
                x += 1
            return reacao
      
    @property
    def razao_equiv(self):
        """ Razão de Equivalência """
        razao_equiv = self._razao_equiv
        return razao_equiv
    
    @property
    def reacao_produtos(self):
        """ Retorna uma lista com os produtos da reação de combustao [[PROD, MOLS], ...] """
        x = 0
        reacao_produtos = []
        if self._razao_equiv == 1:
            dados_produtos = self._produtos_estequiometrico
        else:
            dados_produtos = self._produtos_dissociacao           
        while x < len(dados_produtos):
            elemento = dados_produtos[x][0]
            valor = f"{ dados_produtos[x][1] : .5f}"
            reacao_produtos.append([elemento, valor])
            x += 1
        return reacao_produtos

    @property
    def comb_mols(self):
        """ Retorna o número de mols de Combustível [mol] """
        if self._razao_equiv == 1:
            comb_mols = f"{self._n_comb_estequiometrico : .3f}"
        else:
            comb_mols = f"{self._n_comb_dissociacao: .3f}"
        return comb_mols

    @property
    def oxid_mols(self):
        """ Retorna o número de mols de Combustível [mol] """
        if self._razao_equiv == 1:
            oxid_mols = f"{self._n_oxid: .3f}"
        else:
            oxid_mols = f"{self._n_oxid: .3f}"
        return oxid_mols

    @property
    def temperatura_adiabatica(self):
        """ Retorna a Temperatura Adiabática de Chama [K] """
        if self._razao_equiv == 1:
            temperatura_adiabatica = f"{self._temperatura_adiabatica_estequiometrica : .3f}"
        else:
            temperatura_adiabatica = f"{self._temperatura_adiabatica_dissociacao : .3f}"
        return temperatura_adiabatica

    @property
    def razao_mistura(self):
        """ Retorna a Razão de Mistura Oxidante/Combustível [-] """
        if self._razao_equiv == 1:
            razao_mistura= f"{self._razao_mistura_estequiometrica : .3f}"
        else:
            razao_mistura = f"{self._razao_mistura_dissociacao : .3f}"
        return eval(razao_mistura)
    
    @property
    def massa_molar_media(self):
        """ Retorna a Massa Molar Média [kg/kmol] """
        if self._razao_equiv == 1:
            massa_molar_media = f"{self._massa_molar_media_estequiometrica : .3f}"
        else:
            massa_molar_media = f"{self._massa_molar_media_dissociacao : .3f}"
        return massa_molar_media
    
    @property
    def cp_medio(self):
        """ Retorna o Calor Específico Médio a Pressão Constante [J/kgK] """
        if self._razao_equiv == 1:
            cp_medio = f"{self._cp_medio_estequiometrico : .3f}"
        else:
            cp_medio = f"{self._cp_medio_dissociacao : .3f}"
        return cp_medio
    
    @property
    def constante_gases(self):
        """ Constante dos Gases produtos da combustão [J/kgK] """
        if self._razao_equiv == 1:
            constante_gases = f"{self._constante_gases_estequiometrico : .3f}"
        else:
            constante_gases = f"{self._constante_gases_dissociacao: .3f}"
        return eval(constante_gases)

    @property
    def cv_medio(self):
        """ Calor Específico Médio a Volume Constante [J/kgK] """
        if self._razao_equiv == 1:
            cv_medio = f"{self._cv_estequiometrico : .3f}"
        else:
            cv_medio = f"{self._cv_dissociacao : .3f}"
        return cv_medio

    @property
    def k(self):
        """ Razão dos Calores Específicos [-] """
        if self._razao_equiv == 1:
            k = f"{self._k_estequiometrico : .3f}"
        else:
            k = f"{self._k_dissociacao : .3f}"
        return eval(k)

    """
    #
    #ESCOAMENTO COMPRESSIVEL
    #
    """
    def escoamento_compressivel(self):        
        #Ponto 1 - Camara de Combustão
        self._v_1 = 0                                                    # Velocidade no ponto 1 [m/s]
        if self.razao_equiv == 1:
            self._t_1 = self._temperatura_adiabatica_estequiometrica     # Temperatura no ponto 1 [K]
        else:
            self._t_1 = self._temperatura_adiabatica_dissociacao
        self._p_1 = self._pressao                                        # Pressao no ponto 1 [Pa]
        self._a_1 = (self.k * self.constante_gases * self._t_1)**(1/2)   # Velocidade do Som no ponto 1 [m/s]
        self._mach_1 = self._v_1 / self._a_1                             # Número de Mach no ponto 1 [-]
        self._vol_esp_1 = self.constante_gases * self._t_1 / self._p_1   # Volume Específico no ponto 1 [m³/kg]
        self._rho_1 = 1 / self._vol_esp_1                                # Massa Específica no ponto 1 [kg/m³]

        #Propriedades de Estagnação
        #Como Mach em 1 é 0, as Propriedades de Estagnação serão iguais ao ponto 1
        self._t_0 = self._t_1         # Temperatura de Estagnação [K]
        self._p_0 = self._p_1         # Pressão de Estagnação [Pa]
        self._rho_0 = self._rho_1     # Massa Específica de estagnação [kg/m³]

        #Ponto g - Garganta da Camara de Combustao
        self._mach_g = 1                                                                                         # Número de Mach na garganta [-]
        self._p_g = self._p_0 / ((1 + (((self.k - 1) / 2) * self._mach_g ** 2)) ** (self.k / (self.k -1)))       # Pressão na garganta [Pa]
        self._t_g = self._t_0 / (1 + (((self.k - 1) / 2) * self._mach_g ** 2))                                   # Temperatura na garganta [K]
        self._rho_g = self._rho_0 / ((1 + (((self.k - 1) / 2) * self._mach_g ** 2)) ** (1 / (self.k -1)))        # Pressão na garganta [Pa]
        self._vol_esp_g = 1 / self._rho_g                                                                        # Volume Específico na garganta [m3/kg]
        self._a_g = (self.k * self.constante_gases * self._t_g)**(1/2)                                           # Velocidade do Som na garganta [m/s]
        self._v_g = self._a_g * self._mach_g                                                                     # Velocidade na garganta [m/s]

        #Ponto 2 - Saída do Bocal
        #Condição otima de expansão p2 = p3
        self._p_3 = self._pressao_externa                                                                          # Pressao ambiente [Pa]
        self._p_2 = self._p_3                                                                                      # Pressao no ponto 2 [Pa]
        self._mach_2 = ((((self._p_0 / self._p_2)**((self.k - 1) / self.k)) - 1) / ((self.k - 1) / 2)) ** (1 / 2)  # Numero de Mach no ponto 2 [-]
        self._t_2 = self._t_0 / (1 + (((self.k - 1) / 2) * self._mach_2 ** 2))                                     # Temperatura no ponto 2 [K]
        self._a_2 = (self.k * self.constante_gases * self._t_2) ** (1 / 2)                                         # Velocidade do som no ponto 2 [m/s]
        self._v_2 = self._a_2 * self._mach_2                                                                       # Velocidade no ponto 2 [m/s]
        self._vol_esp_2 = (self.constante_gases * self._t_2) / self._p_2                                           # Volume especifico no ponto 2 [m³/kg]
        self._rho_2 = self._rho_0 / ((1 + (((self.k - 1) / 2) * self._mach_2 ** 2)) ** (1 / (self.k - 1)))         # Massa especifica no ponto 2 [kg/m³]

    @property
    def t_1(self):
        """ Temperatura 1 (Camara de Combustao) [K]"""
        t_1 = f"{self._t_1 : .3f}"
        return t_1
    
    @property
    def t_g(self):
        """ Temperatura g (Garganta) [K]"""
        t_g = f"{self._t_g : .3f}"
        return t_g
    
    @property
    def t_2(self):
        """ Temperatura 2 (Saida do Bocal) [K]"""
        t_2 = f"{self._t_2 : .3f}"
        return t_2

    @property
    def p_1(self):
        """ Pressao 1 (Camara de Combustao) [kPa]"""
        p_1 = self._p_1 / 1000
        p_1 = f"{p_1 : .3f}"
        return p_1
    
    @property
    def p_g(self):
        """ Pressao g (Garganta) [kPa]"""
        p_g = self._p_g / 1000
        p_g = f"{p_g : .3f}"
        return p_g
    
    @property
    def p_2(self):
        """ Pressao 2 (Saida do Bocal) [kPa]"""
        p_2 = self._p_2 / 1000
        p_2 = f"{p_2 : .3f}"
        return p_2

    @property
    def v_1(self):
        """ Velocidade 1 (Camara de Combustao) [m/s]"""
        v_1 = f"{self._v_1 : .3f}"
        return v_1
    
    @property
    def v_g(self):
        """ Velocidade g (Garganta) [m/s]"""
        v_g = f"{self._v_g : .3f}"
        return v_g
    
    @property
    def v_2(self):
        """ Velocidade 2 (Saida do Bocal) [m/s]"""
        v_2 = f"{self._v_2 : .3f}"
        return v_2

    @property
    def a_1(self):
        """Velocidade do Som 1 (Camara de Combustao) [m/s]"""
        a_1 = f"{self._a_1 : .3f}"
        return a_1
    
    @property
    def a_g(self):
        """Velocidade do Som g (Garganta) [m/s]"""
        a_g = f"{self._a_g : .3f}"
        return a_g

    @property
    def a_2(self):
        """Velocidade do Som 2 (Saida do Bocal) [m/s]"""
        a_2 = f"{self._a_2 : .3f}"
        return a_2

    @property
    def mach_1(self):
        """Numero de Mach em 1 (Camara de Combustao) [-]"""
        mach_1 = f"{self._mach_1 : .3f}"
        return mach_1
    
    @property
    def mach_g(self):
        """Numero de Mach em g (Garganta) [-]"""
        mach_g = f"{self._mach_g : .3f}"
        return mach_g

    @property
    def mach_2(self):
        """Numero de Mach em 2 (Saida do Bocal) [-]"""
        mach_2 = f"{self._mach_2 : .3f}"
        return mach_2

    @property
    def vol_esp_1(self):
        """Volume Especifico em 1 (Camara de Combustao) [m³/kg]"""
        volume_especifico_1 = f"{self._vol_esp_1 : .3f}"
        return volume_especifico_1
    
    @property
    def vol_esp_g(self):
        """Volume Especifico em g (Garganta) [m³/kg]"""
        vol_esp_g = f"{self._vol_esp_g : .3f}"
        return vol_esp_g

    @property
    def vol_esp_2(self):
        """Volume Especifico em 2 (Saida do Bocal) [m³/kg]"""
        vol_esp_2 = f"{self._vol_esp_2 : .3f}"
        return vol_esp_2

    @property
    def rho_1(self):
        """Massa Especifica em 1 (Camara de Combustao) [kg/m³]"""
        rho_1 = f"{self._rho_1 : .3f}"
        return rho_1
    
    @property
    def rho_g(self):
        """Massa Especifica em g (Garganta) [kg/m³]"""
        rho_g = f"{self._rho_g : .3f}"
        return rho_g
    
    @property
    def rho_2(self):
        """Massa Especifica em 2 (Saida do Bocal) [kg/m³]"""
        rho_2 = f"{self._rho_2 : .3f}"
        return rho_2

    """
    #
    #PARÂMETROS DE PERFORMANCE
    #
    """
    def parametros_performance(self):
        self._razao_expansao = (self._mach_g / self._mach_2) * (((1 + (((self.k - 1) / 2)*self._mach_2**2))/(1 + (((self.k - 1) / 2)*self._mach_g**2)))**((self.k+1)/(self.k-1)))**(1/2)
        self._coeficiente_empuxo = (((2*self.k**2)/(self.k-1))*((2/(self.k+1))**((self.k+1)/(self.k-1)))*(1-(self._p_2/self._p_1)**((self.k-1)/self.k)))**(1/2)+self._razao_expansao*((self._p_2-self._p_3)/self._p_1)
        self._area_g = self._forca_empuxo / (self._coeficiente_empuxo * self._p_1)
        self._area_2 = self._area_g * self._razao_expansao
        self._razao_cont = (8*(((self._area_g*4)/pi)**(1/2)*100)**(-0.6))+1.25
        self._area_1 = self._razao_cont * self._area_g
        self._vazao_massica_total_propelente = (self._forca_empuxo-(self._p_2-self._p_3)*self._area_2)/self._v_2
        self._impulso_especifico = self._forca_empuxo/self._vazao_massica_total_propelente*Constantes.aceleracao_grav()
        self._v_efetiva_exaustao = self._impulso_especifico*Constantes.aceleracao_grav()
        self._v_caracteristica = (self._p_1*self._area_g)/self._vazao_massica_total_propelente
    
    @property
    def razao_expansao(self):
        """ Razão de Expansão [-] """
        razao_expansao = f"{self._razao_expansao : .3f}"
        return razao_expansao
    
    @property
    def coeficiente_empuxo(self):
        """ Coeficiente de Empuxo [-] """
        coeficiente_empuxo = f"{self._coeficiente_empuxo : .3f}"
        return coeficiente_empuxo
    
    @property
    def area_g(self):
        area_g = f"{self._area_g : .3f}"
        return area_g
    
    @property
    def area_2(self):
        """ Área da Garganta [m²] """
        area_2 = f"{self._area_2 : .3f}"
        return area_2

    @property
    def razao_contracao(self):
        """ Razão de Contração [-] """
        razao_contracao = f"{self._razao_cont : .3f}"
        return razao_contracao
    
    @property
    def area_1(self):
        """ Área da Câmara de Combustão [m²] """
        area_1 = f"{self._area_1 : .3f}"
        return area_1
    
    @property
    def vazao_massica_total_propelente(self):
        """Vazao Massica Total de Propelentes [kg/s]"""
        vazao_massica_total_propelente = f"{self._vazao_massica_total_propelente : .3f}"
        return vazao_massica_total_propelente
    
    @property
    def impulso_especifico(self):
        """Impulso Específico [s]"""
        impulso_especifico = f"{self._impulso_especifico : .3f}"
        return impulso_especifico

    @property
    def v_efetiva_exaustao(self):
        """Velocidade Efetiva de Exaustao [m/s]"""
        v_efetiva_exaustao = f"{self._v_efetiva_exaustao : .3f}"
        return v_efetiva_exaustao

    @property
    def v_caracteristica(self):
        """Velocidade Caracteristica [m/s]"""
        v_caracteristica = f"{self._v_caracteristica : .3f}"
        return v_caracteristica

    """
    #
    # GEOMETRIA DA CÂMARA DE COMBUSTÃO E BOCAL
    #
    """
    def geometria(self):
        self._r_1 = (self._area_1/pi)**(1/2)    # Raio da câmara de combustão
        self._d_1 = self._r_1 * 2               # Diametro da câmara de combustão
        self._r_2 = (self._area_2/pi)**(1/2)    # Raio da saida do bocal
        self._d_2 = self._r_2 * 2               # Diametro da saida do bocal
        self._r_g = (self._area_g/pi)**(1/2)    # Raio da garganta do bocal
        self._d_g = self._r_g * 2               # Diametro da garganta do bocal
        self._vol_total = self._comprimento_característico * self._area_g    # Volume da câmara de combustão
        self._lg = (self._r_1 - self._r_g)/tan(45*pi/180)               # Comprimento da parte convergente do bocal
        self._lc = (self._vol_total-(self._area_1*self._lg*(1+((self._area_g/self._area_1)**(1/2))+(self._area_g/self._area_1))))/self._area_1  # Comprimento da câmara de combustão
        self._l = (self._r_2-self._r_g)/tan(15*pi/180)   # Comprimento da parte divergente do bocal
        self._l_60 = self._l * 0.6
        self._l_80 = self._l * 0.8
        self._r_3 = 0.4 * self._r_g
        self._r_4 = 1.5 * self._r_g
        self._r_5 = 0.4 * self._r_g

    @property
    def l_caracteristico(self):
        """ Comprimento Característico [m]"""
        l_caracteristico = f"{ self._comprimento_característico : .2f}"
        return l_caracteristico

    @property
    def r_1(self):
        """ Raio da Câmara de Combustão [mm] """
        r_1 = self._r_1 * 1000
        r_1 = f"{ r_1 : .2f}"
        return r_1

    @property
    def r_2(self):
        """ Raio da Saída do Bocal [mm] """
        r_2 = self._r_2 * 1000
        r_2 = f"{r_2 : .2f}"
        return r_2
    
    @property
    def r_g(self):
        """ Raio na Garganta [mm] """
        r_g = self._r_g * 1000
        r_g = f"{r_g : .2f}"
        return r_g
    
    @property
    def r_3(self):
        """ Raio entre a Camara de Combustao e Garganta [mm] """
        r_3 = self._r_3 * 1000
        r_3 = f"{r_3 : .2f}"
        return r_3
    
    @property
    def r_4(self):
        """ Raio da entrada da Garganta [mm] """
        r_4 = self._r_4 * 1000
        r_4 = f"{r_4 : .2f}"
        return r_4
    
    @property
    def r_5(self):
        """ Raio da saída da Garganta [mm] """
        r_5 = self._r_5 * 1000
        r_5 = f"{r_5 : .2f}"
        return r_5
    
    @property
    def d_1(self):
        """ Diâmetro da Câmara de Combustão [mm] """
        d_1 = self._d_1 * 1000
        d_1 = f"{d_1 : .2f}"
        return d_1
    
    @property
    def d_2(self):
        """ Diâmetro da saída do Bocal [mm] """
        d_2 = self._d_2 * 1000
        d_2 = f"{d_2 : .2f}"
        return d_2
    
    @property
    def d_g(self):
        """ Diâmetro da Garganta [mm] """
        d_g = self._d_g * 1000
        d_g = f"{d_g : .2f}"
        return d_g
    
    @property
    def vol_total(self):
        """ Volume Total da Câmara de Combustão [m³] """
        vol_total = self._vol_total
        vol_total = f"{vol_total : .3f}"
        return vol_total
    
    @property
    def lc(self):
        """ Compriento da Câmara de Combustão [mm] """
        lc = self._lc * 1000
        lc = f"{lc : .2f}"
        return lc
    
    @property
    def lg(self):
        """ Compriento da parte Convergente [mm] """
        lg = self._lg * 1000
        lg = f"{lg : .2f}"
        return lg
    
    @property
    def l(self):
        """ Compriento do Bocal Cônico [mm] """
        l = self._l * 1000
        l = f"{l : .2f}"
        return l
    
    @property
    def l_60(self):
        """ Compriento do Bocal de Sino 60% [mm] """
        l_60 = self._l_60 * 1000
        l_60 = f"{l_60 : .2f}"
        return l_60
    
    @property
    def l_80(self):
        """ Compriento do Bocal de Sino 80% [mm] """
        l_80 = self._l_80 * 1000
        l_80 = f"{l_80 : .2f}"
        return l_80

    """
    #
    # INJETORES
    #
    """
    def injetores(self):
        self._vazao_massica_oxid = (self.razao_mistura * self._vazao_massica_total_propelente) / (self.razao_mistura + 1)   # [kg/s]
        self._vazao_massica_comb = self._vazao_massica_total_propelente / (self.razao_mistura + 1)                          # [kg/s]
        self._queda_pressao_oxid = 0.25 * self._p_1       # [Pa]                                                                  
        self._queda_pressao_comb = 0.25 * self._p_1       # [Pa]                                                               
        self._coeficiente_descarga_comb = 0.8                                                                               
        self._coeficiente_descarga_oxid = 0.8

        self._area_total_injetor_oxid = self._vazao_massica_oxid/(self._coeficiente_descarga_oxid*(2*self._oxid.massa_especifica*self._queda_pressao_oxid)**(1/2)) # [???]
        self._vazao_total_oxid = self._vazao_massica_oxid / self._oxid.massa_especifica

        self._area_total_injetor_comb = self._vazao_massica_comb/(self._coeficiente_descarga_comb*(2*self._comb.massa_especifica*self._queda_pressao_comb)**(1/2))
        self._vazao_total_comb = self._vazao_massica_comb / self._comb.massa_especifica

        #self._diametro_injetor_oxid = 0
        #self._diametro_injetor_comb = 0
        self._numero_injetores = 6
        # Quantidade de Injetores ???
        #while (self._diametro_injetor_oxid < 1 or self._diametro_injetor_oxid > 3) and (self._diametro_injetor_comb < 1 or self._diametro_injetor_com > 3):                                                                                 
        #Injetor de Oxidante
        self._area_injetor_oxid = self._area_total_injetor_oxid / self._numero_injetores
        self._diametro_injetor_oxid = (((self._area_injetor_oxid * 4 )/pi)**(1/2))
        self._vazao_injetor_oxid = self._vazao_massica_oxid / self._numero_injetores
        self._v_injetor_oxid = self._vazao_injetor_oxid / self._area_injetor_oxid

        #Injetor de Combustivel
        self._area_injetor_comb = self._area_total_injetor_comb / self._numero_injetores
        self._diametro_injetor_comb = (((self._area_injetor_comb * 4 )/pi)**(1/2))
        self._vazao_injetor_comb = self._vazao_massica_comb / self._numero_injetores
        self._v_injetor_comb = self._vazao_injetor_comb / self._area_injetor_comb

         #   if (self._diametro_injetor_oxid < 1 or self._diametro_injetor_oxid > 3) and (self._diametro_injetor_comb < 1 or self._diametro_injetor_com > 3):       
         #       self._numero_injetores += 1
         #   print(self._numero_injetores, self._diametro_injetor_comb, self._diametro_injetor_oxid)

    @property
    def numero_injetores(self):
        numero_injetores = f"{self._numero_injetores : .3f}"
        return numero_injetores

    # Propriedade Injetores Oxidante
    @property
    def vazao_massica_oxid(self):
        """ Vazão Mássica de Oxidante [kg/s]"""
        vazao_massica_oxid= f"{self._vazao_massica_oxid : .3f}"
        return vazao_massica_oxid

    @property
    def area_total_injetor_oxid(self):
        area_total_injetor_oxid = f"{self._area_total_injetor_oxid : .3f}"
        return area_total_injetor_oxid

    @property
    def vazao_total_oxid(self):
        vazao_total_oxid = f"{self._vazao_total_oxid : .3f}"
        return vazao_total_oxid

    @property
    def area_injetor_oxid(self):
        area_injetor_oxid = f"{self._area_injetor_oxid : .3f}"
        return area_injetor_oxid

    @property
    def diametro_injetor_oxid(self):
        diametro_injetor_oxid = f"{self._diametro_injetor_oxid : .3f}"
        return diametro_injetor_oxid


    @property
    def vazao_injetor_oxid(self):
        vazao_injetor_oxid = f"{self._vazao_injetor_oxid : .3f}"
        return vazao_injetor_oxid

    @property
    def v_injetor_oxid(self):
        v_injetor_oxid = f"{self._v_injetor_oxid : .3f}"
        return v_injetor_oxid

    # Propriedades Injetores de Combustivel
    @property
    def vazao_massica_comb(self):
        """ Vazão Mássica de Combustível [kg/s]"""
        vazao_massica_comb= f"{self._vazao_massica_comb : .3f}"
        return vazao_massica_comb

    @property
    def area_total_injetor_comb(self):
        area_total_injetor_comb = f"{self._area_total_injetor_comb : .3f}"
        return area_total_injetor_comb

    @property
    def vazao_total_comb(self):
        vazao_total_comb = f"{self._vazao_total_comb : .3f}"
        return vazao_total_comb

    @property
    def area_injetor_comb(self):
        area_injetor_comb = f"{self._area_injetor_comb : .3f}"
        return area_injetor_comb

    @property
    def diametro_injetor_comb(self):
        diametro_injetor_comb = f"{self._diametro_injetor_comb : .3f}"
        return diametro_injetor_comb

    @property
    def vazao_injetor_comb(self):
        vazao_injetor_comb = f"{self._vazao_injetor_comb : .3f}"
        return vazao_injetor_comb

    @property
    def v_injetor_comb(self):
        v_injetor_comb = f"{self._v_injetor_comb : .3f}"
        return v_injetor_comb
        



"""
class Combustion():
    def __init__(self, comb, oxid, razao_equiv, pressao):
        self._comb = comb
        self._oxid = oxid
        self._razao_equiv = razao_equiv 
        self._pressao = pressao  * Constantes.pressao_atmosferica()                 # Converte a pressão de [atm] para [pa]
        self._pressao_atm = pressao


class Engine(Combustion):
    def __init__(self, comb, oxid, razao_equiv, pressao, pressao_externa, forca_empuxo, comprimento_caracteristico):
        super().__init__(comb, oxid, razao_equiv, pressao)
        self._pressao_externa = pressao_externa * Constantes.pressao_atmosferica()  # Converte a pressão de [atm] para [pa]
        self._propelentes = [comb, oxid]
        self._forca_empuxo = forca_empuxo
        self._comprimento_característico = comprimento_caracteristico
"""