from flask import Flask, redirect, url_for
from dash import Dash
from werkzeug.middleware.dispatcher import DispatcherMiddleware 
from flask_login import current_user 
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from functools import wraps
from dashflaskapp.config import *

def login_required(f):
    @wraps(f)
    def check_function(*args, **kwargs):

        if not(current_user.is_authenticated):
            return redirect(url_for("login"))

        return f(*args, **kwargs)

    return check_function


server = Flask(__name__)
dash_app1 = Dash(__name__, server = server, url_base_pathname='/dashapp1/')
dash_app2 = Dash(__name__, server = server, url_base_pathname='/dashapp2/')


# This part is meant for setting up configuration of different server environments
# The variable 'envir' can be set up to get information from environment variables or any other method
# If you have no interest on differentiating environment variable, you can remove this part or just leave it as is and it will work just fine
try:
    envir = 'development' 
    if envir == 'staging':
        server.config.from_object(StagingConfig())
    elif envir == 'production':
        server.config.from_object(ProductionConfig())
    else:
        server.config.from_object(DevelopmentConfig())
except:
    server.config.from_object(DevelopmentConfig())


db = SQLAlchemy(server)
bcrypt=Bcrypt(server)
login_manager = LoginManager(server)


from dashflaskapp import routes

for view_func in server.view_functions:
    if view_func.startswith('/dashapp1/'):
        server.view_functions[view_func] = login_required(server.view_functions[view_func])
    if view_func.startswith('/dashapp2/'):
        server.view_functions[view_func] = login_required(server.view_functions[view_func])

app = DispatcherMiddleware(server, {
    '/dash1': dash_app1.server,
    '/dash2': dash_app2.server
})

