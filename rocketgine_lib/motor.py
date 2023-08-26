from .produtos import *
from .constantes import *
from .reacoes_dissociacao import *
from math import pi, tan

class Motor():
    def __init__(self, comb, oxid, razao_equiv, forca_empuxo, comprimento_caracteristico,pressao, pressao_externa=1):
        self.comb = comb
        self.oxid = oxid
        self.razao_equiv = razao_equiv
        self.pressao = pressao
        self.pressao_externa = pressao_externa
        self.propelentes = [comb, oxid]
        self._forca_empuxo = forca_empuxo
        self._comprimento_característico = comprimento_caracteristico
    """
    #
    # Combustão Estequiométrica
    #
    """
    def combustao_estequiometrica(self):
        """
        Executa o cálculo da reação de combustão estequiométrica.
        """
        self.produtos_estequiometrico = []
        self.matriz_estequiometrica = []
        self.n_comb = 1
        
        """
                b                      c             d                      a
        [self.oxid.mols_o, - prod1.mols_o, - prod2.mols_o, - self.comb.mols_o],
        [self.oxid.mols_h, - prod1.mols_h, - prod2.mols_h, - self.comb.mols_h],
        [self.oxid.mols_c, - prod1.mols_c, - prod2.mols_c, - self.comb.mols_c],
        """

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

    """
    #
    # Combustão Com Dissociação
    #
    """


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
        self._v_1 = 0                                                    #Velocidade no ponto 1 [m/s]
        self._t_1 = self.temperatura_adiabatica_estequiometrica          #Temperatura no ponto 1 [K]
        self._p_1 = self.pressao                                         #Pressao no ponto 1 [Pa]
        self._a_1 = (self.k * self.constante_gases * self._t_1)**(1/2)    #Velocidade do Som no ponto 1 [m/s]
        self._mach_1 = self._v_1 / self._a_1                               #Número de Mach no ponto 1
        self._vol_esp_1 = self.constante_gases * self._t_1 / self._p_1     #Volume Específico no ponto 1
        self._rho_1 = 1 / self._vol_esp_1                                 #Massa Específica no ponto 1

        #Propriedades de Estagnação
        #Como Mach em 1 é 0, as Propriedades de Estagnação serão iguais ao ponto 1
        self._t_0 = self._t_1         #Temperatura de Estagnação [K]
        self._p_0 = self._p_1         #Pressão de Estagnação [Pa]
        self._rho_0 = self._rho_1     #Massa Específica de estagnação

        #Ponto g - Garganta da Camara de Combustao
        self._mach_g = 1        #Número de Mach na garganta
        self._p_g = self._p_0 / ((1 + (((self.k - 1) / 2) * self._mach_g ** 2)) ** (self.k / (self.k -1)))       #Pressão na garganta [Pa]
        self._t_g = self._t_0 / (1 + (((self.k - 1) / 2) * self._mach_g ** 2))                                             #Temperatura na garganta [K]
        self._rho_g = self._rho_0 / ((1 + (((self.k - 1) / 2) * self._mach_g ** 2)) ** (1 / (self.k -1)))             #Pressão na garganta [Pa]
        self._vol_esp_g = 1 / self._rho_g                                                                                      #Volume Específico na garganta
        self._a_g = (self.k * self.constante_gases * self._t_g)**(1/2)                                               #Velocidade do Som na garganta [m/s]
        self._v_g = self._a_g * self._mach_g                                                                                    #Velocidade na garganta [m/s]

        #Ponto 2 - Saída do Bocal
        #Condição otima de expansão p2 = p3
        self._p_3 = self.pressao_externa                                                                                        #Pressao ambiente [Pa]
        self._p_2 = self._p_3                                                                                                         #Pressao no ponto 2 [Pa]
        self._mach_2 = ((((self._p_0 / self._p_2)**((self.k - 1) / self.k)) - 1) / ((self.k - 1) / 2)) ** (1 / 2)       #Numero de Mach no ponto 2
        self._t_2 = self._t_0 / (1 + (((self.k - 1) / 2) * self._mach_2 ** 2))                                         #Temperatura no ponto 2
        self._a_2 = (self.k * self.constante_gases * self._t_2) ** (1 / 2)                                       #Velocidade do som no ponto 2
        self._v_2 = self._a_2 * self._mach_2                                                                                #Velocidade no ponto 2
        self._vol_esp_2 = (self.constante_gases * self._t_2) / self._p_2                                               #Volume especifico no ponto 2
        self._rho_2 = self._rho_0 / ((1 + (((self.k - 1) / 2) * self._mach_2 ** 2)) ** (1 / (self.k - 1)))        #Massa especifica no ponto 2

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
        p_1 = f"{self._p_1 : .3f}"
        return p_1
    
    @property
    def p_g(self):
        """ Pressao g (Garganta) [kPa]"""
        p_g = f"{self._p_g : .3f}"
        return p_g
    
    @property
    def p_2(self):
        """ Pressao 2 (Saida do Bocal) [kPa]"""
        p_2 = f"{self._p_2 : .3f}"
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
        razao_expansao = f"{self._razao_expansao : .3f}"
        return razao_expansao
    
    @property
    def coeficiente_empuxo(self):
        coeficiente_empuxo = f"{self._coeficiente_empuxo : .3f}"
        return coeficiente_empuxo
    
    @property
    def area_g(self):
        area_g = f"{self._area_g : .3f}"
        return area_g
    
    @property
    def area_2(self):
        area_2 = f"{self._area_2 : .3f}"
        return area_2

    @property
    def razao_contracao(self):
        razao_contracao = f"{self._razao_cont : .3f}"
        return razao_contracao
    
    @property
    def area_1(self):
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
        print(self._lc, self._vol_total, self._area_1, self._area_g, self._lg)
        self._l = (self._r_2-self._r_g)/tan(15*pi/180)   # Comprimento da parte divergente do bocal
        self._l_60 = self._l * 0.6
        self._l_80 = self._l * 0.8
        self._r_3 = 0.4 * self._r_g
        self._r_4 = 1.5 * self._r_g
        self._r_5 = 0.4 * self._r_g

    @property
    def r_1(self):
        r_1 = f"{self._r_1 : .3f}"
        return r_1

    @property
    def r_2(self):
        r_2 = f"{self._r_2 : .3f}"
        return r_2
    
    @property
    def r_g(self):
        r_g = f"{self._r_g : .3f}"
        return r_g
    
    @property
    def r_3(self):
        r_3 = f"{self._r_3 : .3f}"
        return r_3
    
    @property
    def r_4(self):
        r_4 = f"{self._r_4 : .3f}"
        return r_4
    
    @property
    def r_5(self):
        r_5 = f"{self._r_5 : .3f}"
        return r_5
    
    @property
    def d_1(self):
        d_1 = f"{self._d_1 : .3f}"
        return d_1
    
    @property
    def d_2(self):
        d_2 = f"{self._d_2 : .3f}"
        return d_2
    
    @property
    def d_g(self):
        d_g = f"{self._d_g : .3f}"
        return d_g
    
    @property
    def vol_total(self):
        vol_total = f"{self._vol_total: .3f}"
        return vol_total
    
    @property
    def lc(self):
        lc = f"{self._lc: .3f}"
        return lc
    
    @property
    def lg(self):
        lg = f"{self._lg : .3f}"
        return lg
    
    @property
    def l(self):
        l = f"{self._l : .3f}"
        return l
    
    @property
    def l_60(self):
        l_60 = f"{self._l_60 : .3f}"
        return l_60
    
    @property
    def l_80(self):
        l_80 = f"{self._l_80 : .3f}"
        return l_80




