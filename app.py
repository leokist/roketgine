from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

from views.views import *


if __name__ == '__main__':
    app.run(port=8085, host='0.0.0.0', debug=True, threaded=True)