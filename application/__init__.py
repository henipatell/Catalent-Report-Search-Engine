from flask import Flask, flash, request, redirect, url_for
from config import Config
from flask_mongoengine import MongoEngine
#from flask_bootstrap import Bootstrap

ALLOWED_EXTENSIONS = {'pdf'}

app = Flask(__name__)
app.config.from_object(Config)

#Bootstrap(app)

app.config['DEBUG'] = True
app.config['PDF_DIR_LOC'] = './app/static/'
app.config['PDF_DIR'] = './pdf/' 
app.config['DB_PATH'] = './app/sql/'
app.config['MAX_CONTENT_LENGTH'] = 10 * 1024 * 1024 #10 Mo size max for upload
app.config['ALLOW_UPLOAD'] = True
app.config['UPLOAD_FOLDER'] = './app/uploads'

db = MongoEngine()
db.init_app(app)

from application import routes
