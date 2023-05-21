from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rocketgine.sqlite3'
app.config['SECRET_KEY'] = "random string"


db = SQLAlchemy(app)

from views.views import *
from models import *


if __name__ == '__main__':
    app.run(port=8085, host='0.0.0.0', debug=True, threaded=True)