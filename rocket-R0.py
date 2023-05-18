from math import log

class Constantes():
    def const_univ_gases():
        """Retorna a constante universal dos gases em kJ/kmol*K"""
        const_univ_gases = 8.31447
        return const_univ_gases

class Propelente:
    def __init__(self,  nome, composicao, massa_molar, entalpia_formacao, mols_c, mols_o, mols_h, mols_n):
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

o2_L = Propelente("Oxigênio Líquido", "O2", 31.99880, -12979, 0, 2, 0, 0)
c2h5oh_L = Propelente("Etanol", "C2H5OH", 46.06844, -277510, 2, 1, 6, 0)
h2_L = Propelente("Hidrogênio", "H2", 0, 0, 0, 0, 2, 0)
c8h18_L = Propelente("Gasolina", "C8H18", 114.22852, -250260, 8, 0, 18, 0)
ar_G = Propelente("Ar", "(O2+3,76N2)", 28.9651159, -125.53, 0, 2, 0, 7.52)
c3h8_L = Propelente("", "C3H8", 0, 0, 3, 0, 8, 0)
h2o2_L = Propelente("", "H2O2", 0, 0, 0, 2, 2, 0)


class Gas():
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
        return self.composicao
        
    def coeficientes_1000_6000(self, temp_max, temp_min, a1, a2, a3, a4, a5, a6, a7, b1, b2):
        self.temp_max = temp_max
        self.temp_min = temp_min
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.a4 = a4
        self.a5 = a5
        self.a6 = a6
        self.a7 = a7
        self.b1 = b1
        self.b2 = b2

    def entropia(self, temperatura):
        self.temperatura = temperatura
        t = self.temperatura
        self.s = Constantes.const_univ_gases()*(-(self.a1/(2*t**2))-(self.a2/t)+(self.a3*log(t))+(self.a4*t)+((self.a5*t**2)/2)+((self.a6*t**3)/3)+((self.a7*t**4)/4)+(self.b2))
        return self.s

    def entalpia():
        pass

    def calor_especifico():
        pass

    

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
n2 = Gas("", "N2", 28.0134, 0, 0, 0, 0, 2)


"a*COMB + b+OXID ---> c*H2O + d*CO2 + e*N2 + f*CO + g*H2 + h*O2 + i*OH + j*O + k*H"

class Combustao():
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
    def reacao_combustao(self, tipo="estequiometrica", razao_mistura=1):
        self.tipo = tipo
        self.razao_mistura = razao_mistura
        self.produtos = []
        self.matriz = []

        # Define os produtos de uma reação estequiométrica
        if tipo == "estequiometrica" and (self.combustivel.mols_o > 0 or self.oxidante.mols_o > 0):
            self.produtos.append(h2o)
        if tipo == "estequiometrica" and (self.combustivel.mols_c > 0 or self.oxidante.mols_c > 0):
            self.produtos.append(co2)
        if tipo == "estequiometrica" and (self.combustivel.mols_n > 0 or self.oxidante.mols_n > 0):
            self.produtos.append(n2)
        
        # Obtém a quantidade total de produtos da reação
        n_produtos = len(self.produtos)

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
        
        matriz = self.matriz
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
                        matriz[lin].insert(col, -1 * self.produtos[col-1].mols_o)
                    if col == (n_produtos - 1):
                        matriz[lin].insert(col+1, -1 * self.propelentes[0].mols_o)
                elif lin == 1:
                    if col == 0:
                        matriz[lin].insert(col,self.propelentes[1].mols_h)
                    if col != 0:
                        matriz[lin].insert(col, -1 * self.produtos[col-1].mols_h)
                    if col == (n_produtos - 1):
                        matriz[lin].insert(col+1, -1 * self.propelentes[0].mols_h)
                elif lin == 2:
                    if col == 0:
                        matriz[lin].insert(col,self.propelentes[1].mols_c)
                    if col != 0:
                        matriz[lin].insert(col, -1 * self.produtos[col-1].mols_c)
                    if col == (n_produtos - 1):
                        matriz[lin].insert(col+1, -1 * self.propelentes[0].mols_c)
                elif lin == 3:
                    if col == 0:
                        matriz[lin].insert(col,self.propelentes[1].mols_n)
                    if col != 0:
                        matriz[lin].insert(col, -1 * self.produtos[col-1].mols_n)
                    if col == (n_produtos - 1):
                        matriz[lin].insert(col+1, - 1 * self.propelentes[0].mols_n)
                
                col += 1
            col = 0
            lin += 1

        """
        Cálculo do numero de mol de cada produto e propelente
        Cálculo efetuado pelo método de Eliminação de Gauss
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
        

    
    @property
    def reacao_combustao_resultado(self):
        """Gera a reação de combustão com o número de mols de cada elemento"""
        a = 1
        reacao = f"{a} {self.propelentes[0]} + {self.matriz[0][-1]} {self.propelentes[1]} -->"
        x = 0
        for i in self.produtos:
            reacao += f" {self.matriz[x+1][-1]} {i}"
            if i is not self.produtos[-1]:
                reacao += " + "
            x += 1
        return reacao

    def a(self):
        """Retorna o número de mols do combustível"""
        self.a = 1.0
        print(self.a)

    def b(self):
        """Retorna o número de mols do oxidante"""
        l=len(self.matriz)
        self.b = self.matriz[0][l]
        print(self.b)
    
    def c(self):
        """Retorna o número de mols do produto da combustão"""
        l=len(self.matriz)
        self.c = self.matriz[1][l]
        print(self.c)
    
    def d(self):
        """Retorna o número de mols do produto da combustão"""
        l=len(self.matriz)
        if l >= 3:
            self.d = self.matriz[2][l]
        else:
            self.d = "Elemento inexistente"
        print(self.d)
    
    def e(self):
        """Retorna o número de mols do produto da combustão"""
        l=len(self.matriz)
        if l >= 4:
            self.e = self.matriz[3][l]
        else:
            self.e = "Elemento inexistente"
        print(self.e)



comb = c2h5oh_L
oxid = ar_G
comb2 = Combustao(comb, oxid)
comb2.reacao_combustao()
print(comb2.reacao_combustao_resultado)
