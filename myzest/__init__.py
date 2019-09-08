from flask import Flask
from flask_pymongo import PyMongo
from flask_bcrypt import Bcrypt
import os
from os import path

app = Flask(__name__)

app.config['SECRET_KEY'] = os.environ.get('secret_key')
app.config['RECIPE_PIC_DIR'] = path.join(path.dirname(path.realpath(__file__)), 'static/img/recipes')

bcrypt = Bcrypt(app)

"""
Set MongoDB URI for Testing and Dev ENV 
for testing ENV run 'TEST_FLAG=true python -m unittest'
"""

app.config['MONGO_URI'] = os.environ.get('mongo_uri')

mongo = PyMongo(app)

from myzest import routes
