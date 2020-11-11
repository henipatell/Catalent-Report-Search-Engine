import os
from application import app, db
from flask import render_template, request, json, Response, redirect, flash, url_for
from flask_bootstrap import Bootstrap
import sqlite3
from werkzeug.utils import secure_filename
from application.models import User
from application.forms import LoginForm, RegisterForm

@app.route("/")
@app.route("/search/")
@app.route("/search/<searchTerm>")
def search(searchTerm=None):
    return render_template("search.html", searchTerm=searchTerm)

@app.route("/search-results", methods=["POST"])
def search_results():
    searchTerm = request.form.get('searchTerm')
    return render_template("search_results.html", searchTerm=searchTerm)


@app.route("/home", methods=["GET", "POST"])
def home():
    return render_template("home.html", home=True)

@app.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm(request.form)

    if request.method == 'POST' and form.validate_on_submit():
        user_id     = User.objects.count()
        user_id     += 1

        email       = form.email.data
        retyped_email = form.retypedEmail.data
        password    = form.password.data
        confirmed_password = form.confirmPassword.data

        user = User(user_id=user_id, email=email)
        user.set_password(password)
        user.save()
        flash("You are successfully registered!","success")
        return redirect(url_for('home'))

    return render_template("register.html",form=form, register=True)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        #return render_template('home.html', form=form, home=True)

        email       = form.email.data
        password    = form.password.data

        user = User.objects(email=email).first()
        if user and password == user.get_password(password): #user.get_password(password)
            flash("you are successfully logged in!", "success")
            return redirect("/home")
        else:
            flash("Sorry, something went wrong.","danger")

    return render_template("login.html",form=form, login=True)


@app.route("/user")
def user():
    #User(user_id=1, username='henipatel', email='henipatel@gmail.com', retyped_email='henipatel@gmail.com', password='heni1234', confirmed_password='heni1234').save()
    users = User.objects.all()
    return render_template('user.html', users=users)    

