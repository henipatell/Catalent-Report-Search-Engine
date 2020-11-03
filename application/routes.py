from application import app
from flask import render_template

@app.route("/")
@app.route("/search")
def search():
    return render_template("search.html")

@app.route("/home")
def home():
    return render_template("home.html", login=False)

@app.route("/register")
def register():
    return render_template("register.html", login=False)

@app.route("/login")
def login():
    return render_template("login.html", login=False)