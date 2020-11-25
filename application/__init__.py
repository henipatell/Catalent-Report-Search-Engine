from flask import Flask, flash, request, redirect, url_for
from config import Config
from flask_mongoengine import MongoEngine
#from flask_bootstrap import Bootstrap

ALLOWED_EXTENSIONS = {'pdf'}

app = Flask(__name__)
app.config.from_object(Config)

#Bootstrap(app)

app.config['DEBUG'] = True

db = MongoEngine()
db.init_app(app)

from application import routes
