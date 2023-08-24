from .produtos import *
from .constantes import *
from .reacoes_dissociacao import *

class Motor():
    def __init__(self, comb, oxid, razao_equiv, pressao, pressao_externa=1):
        self.comb = comb
        self.oxid = oxid
        self.razao_equiv = razao_equiv
        self.pressao = pressao
        self.pressao_externa = pressao_externa
        self.propelentes = [comb, oxid]
        print(self.propelentes)

    """
             b                      c             d                      a
    [self.oxid.mols_o, - prod1.mols_o, - prod2.mols_o, - self.comb.mols_o],
    [self.oxid.mols_h, - prod1.mols_h, - prod2.mols_h, - self.comb.mols_h],
    [self.oxid.mols_c, - prod1.mols_c, - prod2.mols_c, - self.comb.mols_c],
    """
    def combustao_estequiometrica(self):
        """
        Executa o cálculo da reação de combustão estequiométrica.
        """
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


        """
        # Massa Molar Média
        """
        self.massa_molar_media_estequiometrica = 0
        self.total_mols_produto_estequiometrico = 0
        x = 0
        for i in self.produtos_estequiometrico:
            self.total_mols_produto_estequiometrico += self.produtos_estequiometrico[x][1]
            x += 1
        x = 0
        for i in self.produtos_estequiometrico:
            produto = self.produtos_estequiometrico[x][0]
            self.massa_molar_media_estequiometrica += (self.produtos_estequiometrico[x][1] / self.total_mols_produto_estequiometrico) * produto.massa_molar
            x += 1
        
        """
        # Calor Específico a Pressão Constante
        """
        self.cp_medio_estequiometrico = 0
        x = 0
        for i in self.produtos_estequiometrico:
            produto = self.produtos_estequiometrico[x][0]
            self.cp_medio_estequiometrico  += (self.produtos_estequiometrico[x][1] / self.total_mols_produto_estequiometrico) * produto.calor_especifico(self.temperatura_adiabatica_estequiometrica)
            x += 1
        self.cp_medio_estequiometrico = self.cp_medio_estequiometrico * 1000 / self.massa_molar_media_estequiometrica

        """
        # Constante dos Gases
        """
        self.constante_gases_estequiometrico = Constantes.const_univ_gases() * 1000 / self.massa_molar_media_estequiometrica


        """
        # Calor Específico a Volume Constante
        """
        self.cv_estequiometrico = self.cp_medio_estequiometrico - self.constante_gases_estequiometrico

        """
        # Razão dos Calores Específicos
        """
        self.k_estequiometrico = self.cp_medio_estequiometrico / self.cv_estequiometrico

    @property
    def combustao_resultado(self):
        """Exibe o resultado da reação de combustão com o número de mols de cada elemento"""
        # Retorna o resultado da reação estequiométrica
        if self.razao_equiv == 1:
            reacao = f"{self.n_comb} {self.propelentes[0]} + %.3f  {self.propelentes[1]} --> " %(self.n_oxid)

            x = 0
            for i in self.produtos_estequiometrico:

                reacao += f"%.3f {self.produtos_estequiometrico[x][0]}" %(self.produtos_estequiometrico[x][1])
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
    def comb_produtos(self):
        if self.razao_equiv == 1:
            comb_produtos = self.produtos_estequiometrico
        return comb_produtos

    @property
    def comb_mols(self):
        comb_mols = f"{self.n_comb : .3f}"
        return comb_mols

    @property
    def oxid_mols(self):
        oxid_mols = f"{self.n_oxid : .3f}"
        return oxid_mols

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
            razao_mistura= f"{self.razao_mistura_estequiometrica : .3f}"
        else:
            razao_mistura = f"{self.razao_mistura_dissociacao : .3f}"
        return razao_mistura
    
    @property
    def massa_molar_media(self):
        if self.razao_equiv == 1:
            massa_molar_media = self.massa_molar_media_estequiometrica
        return massa_molar_media
    
    @property
    def cp_medio(self):
        if self.razao_equiv == 1:
            cp_medio = self.cp_medio_estequiometrico
        return cp_medio
    
    @property
    def constante_gases(self):
        if self.razao_equiv == 1:
            constante_gases = self.constante_gases_estequiometrico
        return constante_gases

    @property
    def cv_medio(self):
        if self.razao_equiv == 1:
            cv_medio = self.cv_estequiometrico
        return cv_medio

    @property
    def k(self):
        if self.razao_equiv == 1:
            k = self.k_estequiometrico
        return k

    """
    #
    #ESCOAMENTO COMPRESSIVEL
    #
    """
    def escoamento_compressivel(self):
        #Ponto 1 - Camara de Combustão
        self.v_1 = 0                                                    #Velocidade no ponto 1 [m/s]
        self.t_1 = self.temperatura_adiabatica_estequiometrica          #Temperatura no ponto 1 [K]
        self.p_1 = self.pressao                                         #Pressao no ponto 1 [Pa]
        self.a_1 = (self.k * self.constante_gases * self.t_1)**(1/2)    #Velocidade do Som no ponto 1 [m/s]
        self.mach_1 = self.v_1 / self.a_1                               #Número de Mach no ponto 1
        self.vol_esp_1 = self.constante_gases * self.t_1 / self.p_1     #Volume Específico no ponto 1
        self.rho_1 = 1 / self.vol_esp_1                                 #Massa Específica no ponto 1

        #Propriedades de Estagnação
        #Como Mach em 1 é 0, as Propriedades de Estagnação serão iguais ao ponto 1
        self.t_0 = self.t_1         #Temperatura de Estagnação [K]
        self.p_0 = self.p_1         #Pressão de Estagnação [Pa]
        self.rho_0 = self.rho_1     #Massa Específica de estagnação

        #Ponto g - Garganta da Camara de Combustao
        self.mach_g = 1        #Número de Mach na garganta
        self.p_g = self.p_0 / ((1 + (((self.k - 1) / 2) * self.mach_g ** 2)) ** (self.k / (self.k -1)))       #Pressão na garganta [Pa]
        self.t_g = self.t_0 / (1 + (((self.k - 1) / 2) * self.mach_g ** 2))                                             #Temperatura na garganta [K]
        self.rho_g = self.rho_0 / ((1 + (((self.k - 1) / 2) * self.mach_g ** 2)) ** (1 / (self.k -1)))             #Pressão na garganta [Pa]
        self.vol_esp_g = 1 / self.rho_g                                                                                      #Volume Específico na garganta
        self.a_g = (self.k * self.constante_gases * self.t_g)**(1/2)                                               #Velocidade do Som na garganta [m/s]
        self.v_g = self.a_g * self.mach_g                                                                                    #Velocidade na garganta [m/s]

        #Ponto 2 - Saída do Bocal
        #Condição otima de expansão p2 = p3
        self.p_3 = self.pressao_externa                                                                                        #Pressao ambiente [Pa]
        self.p_2 = self.p_3                                                                                                         #Pressao no ponto 2 [Pa]
        self.mach_2 = ((((self.p_0 / self.p_2)**((self.k - 1) / self.k)) - 1) / ((self.k - 1) / 2)) ** (1 / 2)       #Numero de Mach no ponto 2
        self.t_2 = self.t_0 / (1 + (((self.k - 1) / 2) * self.mach_2 ** 2))                                         #Temperatura no ponto 2
        self.a_2 = (self.k * self.constante_gases * self.t_2) ** (1 / 2)                                       #Velocidade do som no ponto 2
        self.v_2 = self.a_2 * self.mach_2                                                                                #Velocidade no ponto 2
        self.vol_esp_2 = (self.constante_gases * self.t_2) / self.p_2                                               #Volume especifico no ponto 2
        self.rho_2 = self.rho_0 / ((1 + (((self.k - 1) / 2) * self.mach_2 ** 2)) ** (1 / (self.k - 1)))        #Massa especifica no ponto 2

    @property
    def temperatura_1(self):
        temperatura_1 = f"{self.t_1 : .3f}"
        return temperatura_1
    
    @property
    def temperatura_g(self):
        temperatura_g = f"{self.t_g : .3f}"
        return temperatura_g
    
    @property
    def temperatura_2(self):
        temperatura_2 = f"{self.t_2 : .3f}"
        return temperatura_2

    @property
    def pressao_1(self):
        pressao_1 = f"{self.p_1 : .3f}"
        return pressao_1
    
    @property
    def pressao_g(self):
        pressao_g = f"{self.p_g : .3f}"
        return pressao_g
    
    @property
    def pressao_2(self):
        pressao_2 = f"{self.t_2 : .3f}"
        return pressao_2

    @property
    def velocidade_1(self):
        velocidade_1 = f"{self.v_1 : .3f}"
        return velocidade_1
    
    @property
    def velocidade_g(self):
        velocidade_g = f"{self.v_g : .3f}"
        return velocidade_g
    
    @property
    def velocidade_2(self):
        velocidade_2 = f"{self.v_2 : .3f}"
        return velocidade_2

    @property
    def velocidade_som_1(self):
        velocidade_som_1 = f"{self.a_1 : .3f}"
        return velocidade_som_1
    
    @property
    def velocidade_som_g(self):
        velocidade_som_g = f"{self.a_g : .3f}"
        return velocidade_som_g

    @property
    def velocidade_som_2(self):
        velocidade_som_2 = f"{self.a_2 : .3f}"
        return velocidade_som_2

    @property
    def num_mach_1(self):
        num_mach_1 = f"{self.mach_1 : .3f}"
        return num_mach_1
    
    @property
    def num_mach_g(self):
        num_mach_g = f"{self.mach_g : .3f}"
        return num_mach_g

    @property
    def num_mach_2(self):
        num_mach_2 = f"{self.mach_2 : .3f}"
        return num_mach_2

    @property
    def volume_especifico_1(self):
        volume_especifico_1 = f"{self.vol_esp_1 : .3f}"
        return volume_especifico_1
    
    @property
    def volume_especifico_g(self):
        volume_especifico_g = f"{self.vol_esp_g : .3f}"
        return volume_especifico_g

    @property
    def volume_especifico_2(self):
        volume_especifico_2 = f"{self.vol_esp_2 : .3f}"
        return volume_especifico_2

    @property
    def massa_especifica_1(self):
        massa_especifica_1 = f"{self.rho_1 : .3f}"
        return massa_especifica_1
    
    @property
    def massa_especifica_g(self):
        massa_especifica_g = f"{self.rho_g : .3f}"
        return massa_especifica_g
    
    @property
    def massa_especifica_2(self):
        massa_especifica_2 = f"{self.rho_2 : .3f}"
        return massa_especifica_2







