from math import log, e

class Constantes:
    def const_univ_gases():
        """Retorna a constante universal dos gases em kJ/kmol*K"""
        const_univ_gases = 8.31447
        return const_univ_gases

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


class Gas():
    """Cria um objeto Gás com suas propriedades"""
    def __init__(self, nome, composicao, entalpia_formacao, massa_molar, mols_c, mols_o, mols_h, mols_n):
        self.nome = nome
        self.composicao = composicao
        self.entalpia_formacao = entalpia_formacao
        self.massa_molar = massa_molar
        self.mols_c = mols_c
        self.mols_o = mols_o
        self.mols_h = mols_h
        self.mols_n = mols_n
    
    def __repr__(self):
        return f"{self.composicao}"
        
    def coeficientes_1000_6000(self, temp_max, temp_min, a1, a2, a3, a4, a5, a6, a7, b1, b2):
        """Define os coeficientes de um gás entre as temperaturas de 1000°C a 6000°C"""
        self.temp_max = temp_max
        self.temp_min = temp_min
        self.__a1_temp_alta = a1
        self.__a2_temp_alta = a2
        self.__a3_temp_alta = a3
        self.__a4_temp_alta = a4
        self.__a5_temp_alta = a5
        self.__a6_temp_alta = a6
        self.__a7_temp_alta = a7
        self.__b1_temp_alta = b1
        self.__b2_temp_alta = b2

    def coeficientes_200_1000(self, temp_max, temp_min, a1, a2, a3, a4, a5, a6, a7, b1, b2):
        """Define os coeficientes de um gás entre as temperaturas de 200°C a 1000°C"""
        self.temp_max = temp_max
        self.temp_min = temp_min
        self.__a1_temp_baixa = a1
        self.__a2_temp_baixa = a2
        self.__a3_temp_baixa = a3
        self.__a4_temp_baixa = a4
        self.__a5_temp_baixa = a5
        self.__a6_temp_baixa = a6
        self.__a7_temp_baixa = a7
        self.__b1_temp_baixa = b1
        self.__b2_temp_baixa = b2

    def __coeficiente(self, temperatura):
        """Define qual coeficiente será utilizado com base no valor da temperatura informada"""
        self.temperatura = temperatura
        t = self.temperatura
        if t >= 200 and t <= 200:
            self.a1 = self.__a1_temp_baixa
            self.a2 = self.__a2_temp_baixa
            self.a3 = self.__a3_temp_baixa
            self.a4 = self.__a4_temp_baixa
            self.a5 = self.__a5_temp_baixa
            self.a6 = self.__a6_temp_baixa
            self.a7 = self.__a7_temp_baixa
            self.b1 = self.__b1_temp_baixa
            self.b2 = self.__b2_temp_baixa
        else:
            self.a1 = self.__a1_temp_alta
            self.a2 = self.__a2_temp_alta
            self.a3 = self.__a3_temp_alta
            self.a4 = self.__a4_temp_alta
            self.a5 = self.__a5_temp_alta
            self.a6 = self.__a6_temp_alta
            self.a7 = self.__a7_temp_alta
            self.b1 = self.__b1_temp_alta
            self.b2 = self.__b2_temp_alta

    def entropia(self, temperatura):
        """Executa o cálculo da Entropia gás a uma determinada temperatura"""
        self.temperatura = temperatura
        t = self.temperatura
        self.__coeficiente(t)
        self.s = Constantes.const_univ_gases()*(-(self.a1/(2*t**2))-(self.a2/t)+(self.a3*log(t))+(self.a4*t)+((self.a5*t**2)/2)+((self.a6*t**3)/3)+((self.a7*t**4)/4)+(self.b2))
        return self.s

    def entalpia(self, temperatura):
        """Executa o cálculo da Entalpia do gás a uma determinada temperatura"""
        self.temperatura = temperatura
        t = self.temperatura
        self.__coeficiente(t)
        self.h = Constantes.const_univ_gases()*t*((-self.a1/(t**2))+((self.a2*log(t))/t)+self.a3+((self.a4*t)/2)+((self.a5*(t**2))/3)+((self.a6*(t**3))/4)+((self.a7*(t**4))/5)+(self.b1/t))
        return self.h

    def calor_especifico(self, temperatura):
        """Executa o cálculo do Calor Específico do gás a uma determinada temperatura"""
        self.temperatura = temperatura
        t = self.temperatura
        self.__coeficiente(t)
        self.cp = ((self.a1*t**-2)+(self.a2)+self.a3+(self.a4*t)+(self.a5*t**2)+(self.a6*t**3)+(self.a7*t**4)*Constantes.const_univ_gases())
        return self.cp
    
    def funcao_gibbs(self, temperatura):
        """Executa o cálculo da Função de Gibbs"""
        self.temperatura = temperatura
        t = temperatura
        hf = self.entalpia_formacao
        href = self.entalpia(298.15)
        h = self.entalpia(t)
        #print(f"href: {href}, hf: {hf}, h: {h}")
        s = self.entropia(t)
        self.gibbs = hf + h - href - (t * s)
        return self.gibbs

h = Gas("Hidrogênio", "H", 217998.828, 1.00794, 0, 0 , 1, 0)
h.coeficientes_1000_6000(6000, 1000, 6.07877425E+01, -1.81935442E-01, 2.50021182E+00, -1.22651286E-07, 3.73287633E-11, -5.68774456E-15, 3.41021020E-19, 2.54748640E+04, -4.481917770E-01)
h2 = Gas("", "H2", 0.000, 2.01588, 0, 0 , 1, 0)
h2.coeficientes_1000_6000(6000, 1000, 5.60812801E+05, -8.37150474E+02, 2.97536453E+00, 1.25224912E-03, -3.74071619E-07, 5.93662520E-11, -3.60699410E-15, 5.33982441E+03, -2.202774769E+00)
h2o = Gas("aguá", "H2O", -241826.000, 18.01528, 0, 1, 2, 0)
h2o.coeficientes_1000_6000(6000, 1000, 1.03497210E+06, -2.41269856E+03, 4.64611078E+00, 2.29199831E-03, -6.83683048E-07, 9.42646893E-11, -4.82238053E-15, -1.38428651E+04, -7.978148510E+00)
o = Gas("", "O", 249175.003, 15.99940, 0, 1, 0, 0)
o.coeficientes_1000_6000(6000, 1000, 2.61902026E+05, -7.29872203E+02, 3.31717727E+00, -4.28133436E-04, 1.03610459E-07, -9.43830433E-12, 2.72503830E-16, 3.39242806E+04, -6.679585350E-01)
o2 = Gas("", "O2", 0.000, 31.99880, 0, 2, 0, 0)
o2.coeficientes_1000_6000(6000, 1000, -1.03793902E+06, 2.34483028E+03, 1.81973204E+00, 1.26784758E-03, -2.18806799E-07, 2.05371957E-11, -8.19346705E-16, -1.68901093E+04, 1.738716506E+01)
oh = Gas("", "OH", 37278.206, 17.00734, 0, 1, 1, 0)
oh.coeficientes_1000_6000(6000, 1000, 1.01739338E+06, -2.50995728E+03, 5.11654786E+00, 1.30529993E-04, -8.28432226E-08, 2.00647594E-11, -1.55699366E-15, 2.01964021E+04, -1.101282337E+01)
co = Gas("", "CO", -110535.196, 28.01010, 1, 1, 0, 0)
co.coeficientes_1000_6000(6000, 1000, 4.61919725E+05, -1.94470486E+03, 5.91671418E+00, -5.66428283E-04, 1.39881454E-07, -1.78768036E-11, 9.62093557E-16, -2.46626108E+03, -1.387413108E+01)
co2 = Gas("", "CO2", -393510.000, 44.00950, 1, 2, 0, 0)
co2.coeficientes_1000_6000(6000, 1000, 1.17696242E+05, -1.78879148E+03, 8.29152319E+00, -9.22315678E-05, 4.86367688E-09, -1.89105331E-12, 6.33003659E-16, -3.90835059E+04, -2.652669281E+01)
co2.coeficientes_200_1000(1000, 200, 4.94365054E+04, -6.26411601E+02, 5.30172524E+00, 2.50381382E-03, -2.12730873E-07, -7.68998878E-10, 2.84967780E-13, -4.52819846E+04, -7.048279440E+00)
n2 = Gas("", "N2", 28.0134, 0, 0, 0, 0, 2)
n = Gas("", "N", 11111, 0, 0, 0, 0, 1)



#print(co2.entropia(1500))
#print(co2.entropia(298.15))

#print(co2.entalpia(1500))28.0134
#print(co2.calor_especifico(298.15))

#print(co2.funcao_gibbs(3215.00563621521))

"a*COMB + b+OXID ---> c*H2O + d*CO2 + e*N2 + f*CO + g*H2 + h*O2 + i*OH + j*O + k*H"

class Combustao():
    """Define os reagentes da combustão"""
    def __init__(self, combustivel, oxidante):
        self.combustivel = combustivel
        self.oxidante = oxidante
        self.propelentes = [combustivel, oxidante]

    """
             b                      c             d                      a
    [self.oxidante.mols_o, - prod1.mols_o, - prod2.mols_o, - self.combustivel.mols_o],
    [self.oxidante.mols_h, - prod1.mols_h, - prod2.mols_h, - self.combustivel.mols_h],
    [self.oxidante.mols_c, - prod1.mols_c, - prod2.mols_c, - self.combustivel.mols_c],
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
        if razao_equiv != 0 and (self.combustivel.mols_o > 0 or self.oxidante.mols_o > 0) and (self.combustivel.mols_h > 0 or self.oxidante.mols_h > 0):
            self.produtos_estequiometrico.append(h2o)
        if razao_equiv != 0 and (self.combustivel.mols_c > 0 or self.oxidante.mols_c > 0) and (self.combustivel.mols_o > 0 or self.oxidante.mols_o > 0):
            self.produtos_estequiometrico.append(co2)
        if razao_equiv != 0 and (self.combustivel.mols_n > 0 or self.oxidante.mols_n > 0):
            self.produtos_estequiometrico.append(n2)
              
        print(self.produtos_estequiometrico)

        # Obtém a quantidade total de produtos da reação
        n_produtos = len(self.produtos_estequiometrico)

        # Obtem a quantidade total de reagentes da reação
        n_propelentes = len(self.propelentes)

        # Obtém a quantidade total de elementos
        if self.combustivel.mols_o != 0 or self.oxidante.mols_o != 0:
            n_elementos = 1
        if self.combustivel.mols_h != 0 or self.oxidante.mols_h != 0:
            n_elementos += 1
        if self.combustivel.mols_c != 0 or self.oxidante.mols_c != 0:
            n_elementos += 1
        if self.combustivel.mols_n != 0 or self.oxidante.mols_n != 0:
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
        razao_mistura_estequiometrica = (self.matriz_estequiometrica[0][-1]*self.oxidante.massa_molar)/(1*self.combustivel.massa_molar)
        razao_mistura = razao_mistura_estequiometrica / self.razao_equiv

        """
        CÁLCULO DA REAÇÃO DE COMBUSTÃO COM DISSOCIAÇÃO
        """
        if razao_equiv != 1:
            temp_adiab = 3400
            # Número de mols dos Propelentes
            n_comb = (self.matriz_estequiometrica[0][-1] * oxid.massa_molar) / (razao_mistura * comb.massa_molar)
            n_oxid = self.matriz_estequiometrica[0][-1]

            # Número de mols dos elementos
            if self.combustivel.mols_c > 0 or self.oxidante.mols_c > 0:
                n_c = n_comb*comb.mols_c + n_oxid*oxid.mols_c
            if self.combustivel.mols_o > 0 or self.oxidante.mols_o > 0:
                n_o = n_comb*comb.mols_o + n_oxid*oxid.mols_o
            if self.combustivel.mols_h > 0 or self.oxidante.mols_h > 0:
                n_h = n_comb*comb.mols_h + n_oxid*oxid.mols_h
            if self.combustivel.mols_n > 0 or self.oxidante.mols_n > 0:
                n_n = n_comb*comb.mols_n + n_oxid*oxid.mols_n
        
            # Define os produtos de uma reação com dissociação
            "a*COMB + b+OXID ---> c*CO2 + d*CO + e*H2O + f*OH + g*H2 + h*H + i*O2 + j*O + k*N2 + l*N"
            if (self.combustivel.mols_c > 0 or self.oxidante.mols_c > 0) and (self.combustivel.mols_o > 0 or self.oxidante.mols_o > 0):
                self.produtos_dissociacao.append(co2)
                self.produtos_dissociacao.append(co)
            if (self.combustivel.mols_o > 0 or self.oxidante.mols_o > 0) and (self.combustivel.mols_h > 0 or self.oxidante.mols_h > 0):
                self.produtos_dissociacao.append(h2o)
                self.produtos_dissociacao.append(oh)
            if (self.combustivel.mols_h > 0 or self.oxidante.mols_h > 0):
                self.produtos_dissociacao.append(h2)
                self.produtos_dissociacao.append(h)
            if (self.combustivel.mols_o > 0 or self.oxidante.mols_o > 0):
                self.produtos_dissociacao.append(o2)
                self.produtos_dissociacao.append(o)
            if (self.combustivel.mols_n > 0 or self.oxidante.mols_n > 0):
                self.produtos_dissociacao.append(n2)
                self.produtos_dissociacao.append(n)

            # Calcula as funções de gibbs
            if (self.combustivel.mols_c > 0 or self.oxidante.mols_c > 0) and (self.combustivel.mols_o > 0 or self.oxidante.mols_o > 0):
                gibbs_co2 = co2.funcao_gibbs(temp_adiab)
                gibbs_co = co.funcao_gibbs(temp_adiab)
            if (self.combustivel.mols_o > 0 or self.oxidante.mols_o > 0) and (self.combustivel.mols_h > 0 or self.oxidante.mols_h > 0):
                gibbs_h2o = h2o.funcao_gibbs(temp_adiab)
                gibbs_oh = oh.funcao_gibbs(temp_adiab)
            if (self.combustivel.mols_h > 0 or self.oxidante.mols_h > 0):
                gibbs_h2 = h2.funcao_gibbs(temp_adiab)
                gibbs_h = h.funcao_gibbs(temp_adiab)
            if (self.combustivel.mols_o > 0 or self.oxidante.mols_o > 0):
                gibbs_o2 = o2.funcao_gibbs(temp_adiab)
                gibbs_o = o.funcao_gibbs(temp_adiab)
            if (self.combustivel.mols_n > 0 or self.oxidante.mols_n > 0):
                gibbs_n2 = n2.funcao_gibbs(temp_adiab)
                gibbs_n = n.funcao_gibbs(temp_adiab)

            # Calcula as constantes de dissociação
            if (self.combustivel.mols_o > 0 or self.oxidante.mols_o > 0) and (self.combustivel.mols_h > 0 or self.oxidante.mols_h > 0):
                # H2O --> H2 + 0.5 O2
                kp2 = e**(-(1*gibbs_h2 + 0.5*gibbs_o2 - 1*gibbs_h2o)/(Constantes.const_univ_gases()*temp_adiab))
                # H2O --> OH + 0.5 H2
                # kp3 = e**(-(1*gibbs_oh + 0.5*gibbs_h2 - 1*gibbs_h2o)/(Constantes.const_univ_gases()*temp_adiab))
                # OH --> H + O
                kp3 = e**(-(1*gibbs_h + 1*gibbs_o - 1*gibbs_oh)/(Constantes.const_univ_gases()*temp_adiab))
            if (self.combustivel.mols_o > 0 or self.oxidante.mols_o > 0) and (self.combustivel.mols_c > 0 or self.oxidante.mols_c > 0):
                # CO2 --> CO + O
                kp1 = e**(-(1*gibbs_co + 1*gibbs_o - 1*gibbs_co2)/(Constantes.const_univ_gases()*temp_adiab))
            if (self.combustivel.mols_o > 0 or self.oxidante.mols_o > 0):
                # O2 --> 2 O
                kp5 = e**(-(2*gibbs_o - 1*gibbs_o2)/(Constantes.const_univ_gases()*temp_adiab))
            if (self.combustivel.mols_h > 0 or self.oxidante.mols_h > 0):
                # H2 --> 2 H
                kp4 = e**(-(2*gibbs_h - 1*gibbs_h2)/(Constantes.const_univ_gases()*temp_adiab))
            if (self.combustivel.mols_n > 0 or self.oxidante.mols_n > 0):
                # N2 --> 2 N 
                kp6 = e**(-(2*gibbs_n - 1*gibbs_n2)/(Constantes.const_univ_gases()*temp_adiab))
        
            y = 0.4422
            p = 15
            n = p/y

            N_o2 = 1

            N_o = ((kp5*N_o2)/y)**0.5

            if self.combustivel.mols_c > 0 or self.oxidante.mols_c > 0:
                N_co2 = n_c*N_o/((kp1/y)+N_o)
                N_co = n_c-N_co2
            else:
                N_co = 0
                N_co2 = 0

            N_h_a = (N_o/kp2)*y**2
            N_h_b = (N_o/kp3)*y
            N_h_c = 2*N_co2+N_co+2*N_o2+N_o-n_o
            N_h = (-N_h_b+((N_h_b**2 - 4*N_h_a*N_h_c)**0.5))/(2*N_h_a)

            N_h2 = (n_h-N_h*((N_o*y/kp3)+1))/((2*kp4*y*N_o/kp2)+2)
            N_oh = N_h*N_o*y/kp3
            N_h2o = ((N_h**2)*N_o*(y**2))/kp2


            if self.combustivel.mols_n > 0 or self.oxidante.mols_n > 0:
                N_n_a = 2*y/kp6
                N_n_b = 1
                N_n_c = -n_n
                N_n = (-N_n_b+((N_n_b**2 - 4*N_n_a*N_n_c)**0.5))/(2*N_n_a)

                N_n2 = ((N_n**2)*y)/kp6
            else:
                N_n = 0
                N_n2 = 0

            print(f"o2: {N_o2}, o: {N_o}, co2: {N_co2}, co: {N_co}, h: {N_h}, h2: {N_h2}, oh: {N_oh}, h2o: {N_h2o}, n: {N_n}, n2: {N_n2} razao_mist: {razao_mistura}")
            print(kp1, kp2, kp3, kp4)
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
        """Retorna o número de mols do Oxidante"""
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

def modo_iterativo():
    print(10*"+"+" Bem vindo ao Modo Iterativo "+10*"+")
    

comb = c2h5oh_L
oxid = o2_L 
comb2 = Combustao(comb, oxid)
comb2.reacao_combustao(razao_equiv=1.4)
print(comb2.reacao_combustao_resultado)
#print(comb2.a)
#print(comb2.b)
#print(comb2.c)
#print(comb2.d)
#print(comb2.e)
#print(comb2.razao_mistura)
#print(comb2.razao_mistura_estequiometrica)
#print(comb2.razao_equivalencia)
modo_iterativo()