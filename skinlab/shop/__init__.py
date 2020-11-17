from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:40575526@localhost/skinlab'
app.config['SECRET_KEY'] = "asdasdasdagwerwfvcbdsf"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from shop.admin import routes
