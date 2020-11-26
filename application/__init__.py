from flask import Flask, flash, request, redirect, url_for
from config import Config
from flask_mongoengine import MongoEngine
#from flask_bootstrap import Bootstrap

UPLOAD_FOLDER = 'D:\Internship-Project\TempProject\sample_pdf_files'
ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'docs'}
MAX_CONTENT_LENGTH = 16 * 1024 * 1024

app = Flask(__name__)
app.config.from_object(Config)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = MAX_CONTENT_LENGTH
app.config['ALLOWED_EXTENSIONS'] = ALLOWED_EXTENSIONS
app.config['DEBUG'] = True

db = MongoEngine()
db.init_app(app)
#Bootstrap(app)

from application import routes
