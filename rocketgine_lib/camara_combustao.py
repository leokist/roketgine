from .constantes import *

class CamaraCombustao():
    """Cria um objeto Gás com suas propriedades
    massa_molar: [kg/mol] | entalpia_formacao: [J/mol] | entalpia_t_referência [J/mol]
    """
    def __init__(self, forca_empuxo, comp_caracteristico, temp, pressao):
        self.forca_empuxo = forca_empuxo
        self.comp_caracteristico = comp_caracteristico
        self.temp = temp
        self.pressao = pressao
    
    def escoamento_compressivel(self):
        self.v_1 = 0
        self.t_1 = self.temp
        self.p_1 = self.pressao
        self.a_1 = 1