import os
from application import app, db
from flask import render_template, request, json, Response, redirect, flash, url_for, session
from flask_bootstrap import Bootstrap
import sqlite3
from werkzeug.utils import secure_filename
from application.models import User
from application.forms import LoginForm, RegisterForm
from elasticsearch import Elasticsearch

es = Elasticsearch('127.0.0.1', port=9200)

@app.route("/")
def search_term():
    return render_template("search.html")

@app.route("/home", methods=["GET", "POST"])
def home():
    return render_template("home.html", home=True)

# @app.route("/upload", methods=["GET", "POST"])
# def upload():
#     return render_template("upload.html")

@app.route("/search/")
@app.route("/search/<searchTerm>")
def search(searchTerm=None):
    if not session.get('username'):
      return redirect(url_for('login'))
    return render_template("search.html", searchTerm=searchTerm)


@app.route("/search/results", methods=["GET", "POST"])
def search_results():
    # searchTerm = request.form.get('searchTerm')
    # return render_template("search_results.html", searchTerm=searchTerm)
    search_term = request.form.get('searchTerm')
    res = es.search(
    index='data_science_index',
    body={
    "query" : {"match": {"content": search_term}},
    "highlight" : {"pre_tags" : ["<b>"] , "post_tags" : ["</b>"], "fields" : {"content":{}}}})
    res['ST']=search_term
    for hit in res['hits']['hits']:
        hit['good_summary']='….'.join(hit['highlight']['content'][1:])
    return render_template('search_results.html', res=res, user_request=search_term)

@app.route("/register", methods=["GET", "POST"])
def register():
    if session.get('username'):
        return redirect(url_for('home'))

    form = RegisterForm(request.form)

    if request.method == 'POST' and form.validate_on_submit():
        email       = form.email.data
        retyped_email = form.retypedEmail.data
        password    = form.password.data
        confirmed_password = form.confirmPassword.data

        user = User(user_id=user_id, email=email)
        user.set_password(password)
        user.save()
        session['user_id'] = user.user_id
        session['username'] = user.email

        flash("You are successfully registered!","success")
        return redirect(url_for('home'))
    return render_template("register.html",form=form, register=True)

@app.route("/login", methods=["GET", "POST"])
def login():
    if session.get('username'):
        return redirect(url_for('home'))

    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate_on_submit():
        email       = form.email.data
        password    = form.password.data

        user = User.objects(email=email).first()
        if user and user.get_password(password):
            flash("you are successfully logged in!", "success")
            session['user_id'] = user.user_id
            session['username'] = user.email
            return redirect("/home")
        else:
            flash("Something went wrong! Please try later.", "danger")
    return render_template("login.html",form=form, login=True)

@app.route("/logout")
def logout():
    session['user_id'] = False
    session.pop('username',None)
    return redirect(url_for('login'))
 
@app.route("/user")
def user():
    #User(user_id=1, username='henipatel', email='henipatel@gmail.com', retyped_email='henipatel@gmail.com', password='heni1234', confirmed_password='heni1234').save()
    users = User.objects.all()
    return render_template('user.html', users=users)    

