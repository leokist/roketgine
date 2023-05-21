import os
from app import app

from flask_wtf import FlaskForm
from wtforms import SlectField, StringField, validators, SubmitField, PasswordField

class FormDadosEntrada(FlaskForm):
    combustivel = SelectField('Combustível', choices=[
        ("c2h5oh_L", "Etanol [c2h5oh_L]"),
        ("h2_L","Hidrogênio [h2_L]"),
        ("c8h18_L", "Gasolina [c8h18_L]"),
        ("c3h8_L", "Propano [c3h8_L]"),
        ("c2h8n2_L", "Dimetil-hidrazina Assimétrica [c2h8n2_L]"),
        ("c42h72o14_L", "RG1 - Ginsenosido [c42h72o14_L]"),
        ("nh3_L", "Amônia [nh3_L]")
    ])
