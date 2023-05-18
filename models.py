from app import db


class Propelentes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), unique = True, nullable=False)
    composicao_quimica = db.Column(db.String(50), unique = True, nullable=False)
    entalpia_formacao = db.Column(db.String(50), unique = False, nullable=False)
    massa_molecular = db.Column(db.String(50), unique = False, nullable=False)

    def __init__(self, nome, composicao_quimica, entalpia_formacao, massa_molecular):
        self.nome = nome
        self.composicao_quimica = composicao_quimica
        self.entalpia_formacao = entalpia_formacao
        self.massa_molecular = massa_molecular

    def __repr__ (self):
        return f"Nome: {self.nome}, Composição Quimica: {self.composicao_quimica}"


