from application import app
from flask import render_template, request, json, Response

@app.route("/")
@app.route("/search/")
@app.route("/search/<searchTerm>")
def search(searchTerm=None):
    return render_template("search.html", searchTerm=searchTerm)

@app.route("/search-results", methods=["POST"])
def search_results():
    searchTerm = request.form.get('searchTerm')
    print(searchTerm)
    return render_template("search_results.html", searchTerm=searchTerm)


@app.route("/home")
def home():
    return render_template("home.html", home=True)

@app.route("/register")
def register():
    return render_template("register.html", register=True)

@app.route("/login")
def login():
    return render_template("login.html", login=True)