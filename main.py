from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/home")

def home():
    return "<h1>Its a Home Page</h2>"