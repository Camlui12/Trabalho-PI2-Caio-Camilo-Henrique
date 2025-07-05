from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_pyfile('database.py')

db = SQLAlchemy(app)

from views.index import *
from views.auth import *
from views.veiculos import *
from views.tarifa import *
from views.mensalistas import *
from views.core import *

from models import *

from models.database import init_db
init_db()

if __name__ == '__main__':
    app.run(debug=True)