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
        print(self.propelentes)

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
        while y < len(matriz)-1:
            self.produtos_estequiometrico[y][1] = matriz[y+1][len(matriz)]
            y += 1
            lin += 1

        self.n_oxid = matriz[0][-1]
                                  
        self.razao_mistura_estequiometrica = (self.n_oxid*self.oxid.massa_molar)/(self.n_comb*self.comb.massa_molar)
        
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
        self.entalpia_reagentes = self.n_comb * self.comb.entalpia_formacao + self.n_oxid * self.oxid.entalpia_formacao
        #self.entalpia_reagentes = self.n_comb * (self.comb.entalpia_formacao + self.comb.entalpia(self.comb.temperatura_referencia) - self.comb.entalpia_referencia) + self.n_oxid * (self.oxid.entalpia_formacao + self.oxid.entalpia(self.oxid.temperatura_referencia) - self.oxid.entalpia_referencia)

        entalpia_produtos = 0
        x = 0
        y = 0
        temp_min = 200
        temp_max = 6000
        temp = 200
        produtos = self.produtos_estequiometrico
        erro = 1
        while abs(erro) > 0.1:
            while x < len(produtos):
                prod = produtos[x][0]
                prod_mols = produtos[x][1]
                #entalpia_produtos += prod_mols * (prod.entalpia_formacao + prod.entalpia(temp) - prod.entalpia_t_referencia)
                entalpia_produtos += prod_mols * (prod.entalpia(temp))

                x += 1
            
            erro = 100*((abs(self.entalpia_reagentes)-abs(entalpia_produtos))/abs(entalpia_produtos))

            if temp > temp_max:
                break

            if abs(erro) > 0.1:
                entalpia_produtos = 0
                temp += 0.1
                x = 0
                y += 1
        self.temperatura_adiabatica_estequiometrica = temp
        self.entalpia_produtos = entalpia_produtos
        

    def reacao_dissociacao(self, razao_equiv, pressao):
        """
        REACAO COM DISSOCIACAO
        """        
        self.pressao = pressao
        self.razao_equiv = razao_equiv
        self.razao_mistura_dissociacao = self.razao_mistura_estequiometrica / self.razao_equiv
        self.n_comb = (self.n_oxid * self.oxid.massa_molar) / (self.razao_mistura_dissociacao * self.comb.massa_molar)
        self.produtos_dissociacao = []

        print("RME:",self.razao_mistura_estequiometrica,"RM:", self.razao_mistura, "n_comb:", self.n_comb)


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


        entalpia_produtos = 0
        x = 0
        y = 0
        temp_min = 200
        temp_max = 6000
        temp = 500
        produtos = self.produtos_estequiometrico
        erro = 1
        yy = 0
        zz = 0 
        while yy < 3:
            print(yy, zz)

            # Calcula as constantes de dissociação
            if (self.comb.mols_o > 0 or self.oxid.mols_o > 0) and (self.comb.mols_c > 0 or self.oxid.mols_c > 0):
                # CO2 --> CO + O
                kp1 = reacao_CO2_para_CO_O.kp(temp)

            if (self.comb.mols_o > 0 or self.oxid.mols_o > 0) and (self.comb.mols_h > 0 or self.oxid.mols_h > 0):
                # H2O --> 2H + O
                kp2 = reacao_H2O_para_2H_O.kp(temp)
                # OH --> H + O
                kp3 = reacao_OH_para_H_O.kp(temp)
                # H2O --> OH + O
                kp7 = reacao_H2O_para_OH_O.kp(temp)

            if (self.comb.mols_h > 0 or self.oxid.mols_h > 0):
                # H2 --> 2 H
                kp4 = reacao_H2_para_2H.kp(temp)

            if (self.comb.mols_o > 0 or self.oxid.mols_o > 0):
                # O2 --> 2 O
                kp5 = reacao_O2_para_2O.kp(temp)

            if (self.comb.mols_n > 0 or self.oxid.mols_n > 0):
                # N2 --> 2 N 
                kp6 = reacao_N2_para_2N.kp(temp)

            
            #print(f"kp1: {kp1: .3f},kp2: {kp2: .3f},kp3: {kp3: .3f},kp4: {kp4: .3f},kp5: {kp5: .3f},kp6: {kp6: .3f}")

            p = self.pressao
            y = p / N_total_reagentes
            n_O2 = 0
            iteracoes = 0

            while zz < 3:
                #(n_CO2<0 or n_CO<0 or n_H2O<0 or n_OH<0 or n_O2<0 or n_O<0 or n_H2<0 or n_H<0 or n_N2<0 or n_N<0) or 
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
                #print(iteracoes, n_O2)

                print(N_total_reagentes, N_total_produtos)

                erro2 = 100*((abs(N_total_reagentes)-abs(N_total_produtos))/abs(N_total_produtos))

                n_O2 += 0.1
                zz += 1



            # Define os produtos de uma reação com dissociação
            "a*COMB + b+OXID ---> c*CO2 + d*CO + e*H2O + f*OH + g*H2 + h*H + i*O2 + j*O + k*N2 + l*N"
            if (self.comb.mols_c > 0 or self.oxid.mols_c > 0) and (self.comb.mols_o > 0 or self.oxid.mols_o > 0):
                self.produtos_dissociacao.append([CO2, n_CO2])
                self.produtos_dissociacao.append([CO, n_CO])
            if (self.comb.mols_o > 0 or self.oxid.mols_o > 0) and (self.comb.mols_h > 0 or self.oxid.mols_h > 0):
                self.produtos_dissociacao.append([H2O, n_H2O])
                self.produtos_dissociacao.append([OH, n_OH])
            if (self.comb.mols_h > 0 or self.oxid.mols_h > 0):
                self.produtos_dissociacao.append([H2, n_H2])
                self.produtos_dissociacao.append([H, n_H])
            if (self.comb.mols_o > 0 or self.oxid.mols_o > 0):
                self.produtos_dissociacao.append([O2, n_O2])
                self.produtos_dissociacao.append([O, n_O])
            if (self.comb.mols_n > 0 or self.oxid.mols_n > 0):
                self.produtos_dissociacao.append([N2, n_N2])
                self.produtos_dissociacao.append([N, n_N])

            print(f" CO2: {n_CO2: .6f}, CO: {n_CO: .6f}, H2O: {n_H2O: .6f}, OH: {n_OH: .6f}, O2: {n_O2: .6f}, O: {n_O: .6f}, H2: {n_H2: .6f}, H: {n_H: .6f},   N2: {n_N2: .6f}, N: {n_N: .6f} razao_mist: {self.razao_mistura}")

            while x < len(self.produtos_dissociacao):
                prod = self.produtos_dissociacao[x][0]
                prod_mols = self.produtos_dissociacao[x][1]

                entalpia_produtos += prod_mols * (prod.entalpia(temp))

                x += 1
            
            erro = 100*((abs(self.entalpia_reagentes)-abs(entalpia_produtos))/abs(entalpia_produtos))
            print()

            if yy == 2:
                self.temperatura_adiabatica_dissociacao = temp
            else:
                temp += 1
            yy += 1

            if abs(erro) > 0.1:
                self.produtos_dissociacao.clear

            

        #print(f"n:{n_total}, N:{n_total_calc}, {(erro)}")
        print(f" CO2: {n_CO2}, CO: {n_CO}, H2O: {n_H2O}, OH: {n_OH}, O2: {n_O2}, O: {n_O}, H2: {n_H2}, H: {n_H},   N2: {n_N2}, N: {n_N} razao_mist: {self.razao_mistura}")
        #print(f"o2: {N_o2/n_total_calc}, o: {N_o/n_total_calc}, CO2: {N_CO2/n_total_calc}, co: {N_co/n_total_calc}, h: {N_h/n_total_calc}, h2: {N_h2/n_total_calc}, oh: {N_oh/n_total_calc}, H2O: {N_H2O/n_total_calc}, n: {N_n/n_total_calc}, N2: {N_N2/n_total_calc} razao_mist: {self.razao_mistura}")
        print(f"Nc_r:{N_C_reagentes} No_r:{N_O_reagentes} Nh_r:{N_H_reagentes} Nn_r:{N_N_reagentes}")
        print(f"Nc_p:{N_C_produtos} No_p:{N_O_produtos} Nh_p:{N_H_produtos} Nn_p:{N_N_produtos}")   
        

    @property
    def combustao_resultado(self):
        """Exibe o resultado da reação de combustão com o número de mols de cada elemento"""
        # Retorna o resultado da reação estequiométrica
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
        #Retorna o resultado da reação com dissociação
        else:
            a = self.n_comb
            matriz = self.matriz_estequiometrica

            reacao = f"{a} {self.propelentes[0]} + {self.n_oxid} {self.propelentes[1]} -->"

            #print(self.produtos_dissociacao)

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
    def temperatura_adiabatica(self):
        if self.razao_equiv == 1:
            temperatura_adiabatica = self.temperatura_adiabatica_estequiometrica
        else:
            temperatura_adiabatica = self.temperatura_adiabatica_dissociacao
        return temperatura_adiabatica
    
    @property
    def razao_mistura(self):
        if self.razao_equiv == 1:
            razao_mistura= self.razao_mistura_estequiometrica
        else:
            razao_mistura = self.razao_mistura_dissociacao
        return razao_mistura

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
    #def razao_equivalencia(self):
    #    return self.razao_equivalencia

    #@property
    #def massa_molar_media(self):

