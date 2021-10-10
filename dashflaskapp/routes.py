from flask import render_template, redirect, url_for
from flask_login import login_user, current_user 
from dashflaskapp import server
from dashflaskapp import bcrypt, db
from dashflaskapp.models import User
from dashflaskapp.forms import LoginForm 
from dashflaskapp.dashplotly import dashapp1, dashapp2


@server.route('/')
def home():
    if current_user.is_authenticated:
        return redirect('/dashapp1')
    else:
        return redirect(url_for("login"))


@server.route('/login', methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect('/dashapp1')
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect('/dashapp1')
    return render_template("login.html", form=form)