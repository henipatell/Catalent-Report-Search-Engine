from flask import Flask, flash, request, redirect, url_for
from config import Config
from flask_mongoengine import MongoEngine
#from flask_bootstrap import Bootstrap

app = Flask(__name__)
# es = Elasticsearch(
#     ['localhost', 'otherhost'],
#     http_auth=('user', 'secret'),
#     scheme="https",
#     port=443,
# )

app.config.from_object(Config)
# app.config.setdefault('ELASTICSEARCH_HOST', 'localhost:9200')
# app.config.setdefault('ELASTICSEARCH_HTTP_AUTH', None)

#Bootstrap(app)

db = MongoEngine()
db.init_app(app)

if __name__ == '__main__':
    app.run()

from application import routes
